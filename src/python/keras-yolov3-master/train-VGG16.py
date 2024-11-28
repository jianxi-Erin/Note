import keras.backend as K
import numpy as np
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from keras.layers import Input, Lambda
from keras.models import Model
from keras.optimizers import Adam

from yolo3.model_vgg16_x1x2 import preprocess_true_boxes, yolo_body, tiny_yolo_body, yolo_loss
# from yolov3_mobilenet.base_model.mobilenetv3_base import yolo_body
# from yolov3_mobilenet.base_model.model import yolo_body
#from loss import yolo_loss
from yolo3.utils import get_random_data
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
#---------------------------------------------------#
#   获得类和先验框
#---------------------------------------------------#
def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)
#---------------------------------------------------#
#   训练数据生成器
#   传入标注好的训练集图片
#---------------------------------------------------#
def data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        box_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
            # get_random_data是用来做数据增强的（翻转，缩放，位移等等）
            # 返回一个增强后的image（416,416,3），以及根据图像做对等变换的box:(n,5)
            # n代表有多少个box,一个物体一个box
            image, box = get_random_data(annotation_lines[i], input_shape, random=True)

            image_data.append(image)  #
            box_data.append(box)
            i = (i+1) % n
        # 将数据转换为矩阵的形式
        image_data = np.array(image_data)
        box_data = np.array(box_data)
        '''''''''
        返回
        image_data[batchsize,h,w,channel]
        box_data[batchsize,n,5]
        '''''''''
        # preprocess_true_boxes是数据预处理
        # 返回的y_true就是需要预测这个物体的先验框（每个物体只有一个）
        y_true = preprocess_true_boxes(box_data, input_shape, anchors, num_classes)
        yield [image_data, *y_true], np.zeros(batch_size)

#---------------------------------------------------#
#   数据预处理
#   true_boxes就上上面的boxes[batchsize,n,5]
#   input_shape[416,416]
#---------------------------------------------------#
def preprocess_true_boxes(true_boxes, input_shape, anchors, num_classes):

    assert (true_boxes[..., 4]<num_classes).all(), 'class id must be less than num_classes'
    # 一共有三个特征层数
    num_layers = len(anchors)//3
    # 先验框
    anchor_mask = [[6,7,8], [3,4,5], [0,1,2]] if num_layers==3 else [[3,4,5], [1,2,3]]
    true_boxes = np.array(true_boxes, dtype='float32')
    input_shape = np.array(input_shape, dtype='int32') # 416,416

    # 读出xy轴，读出长宽
    # 输入的true_boxes中的框是左上角右下角点，需要把它转化为中心点
    boxes_xy = (true_boxes[..., 0:2] + true_boxes[..., 2:4]) // 2   #(batch_size,n,2)
    boxes_wh = true_boxes[..., 2:4] - true_boxes[..., 0:2]      #(batch_size,n,2)
    # 计算比例（把坐标长宽/416）（归一到0-1之间）
    true_boxes[..., 0:2] = boxes_xy/input_shape[:]
    true_boxes[..., 2:4] = boxes_wh/input_shape[:]

    # m张图，等于bitch_size
    m = true_boxes.shape[0]
    # 得到网格的shape为[13x13;  26x26;  52x52]
    grid_shapes = [input_shape//{0:32, 1:16, 2:8}[l] for l in range(num_layers)]
    # y_true的格式为(m,13,13,3,25)  (m,26,26,3,25)  (m,52,52,3,25)
    y_true = [np.zeros((m,grid_shapes[l][0],grid_shapes[l][1],len(anchor_mask[l]),5+num_classes),
        dtype='float32') for l in range(num_layers)]

    # 对先验框扩增，方便计算
    anchors = np.expand_dims(anchors, 0)   # (1,9,2)
    anchor_maxes = anchors / 2.
    anchor_mins = -anchor_maxes
    # 长宽要大于0才有效
    # 该步骤是方式异常值的出现
    valid_mask = boxes_wh[..., 0]>0

    for b in range(m):
        # 对每一张图进行处理，方便与先验框计算，去掉一些没有物体的数据
        wh = boxes_wh[b, valid_mask[b]]  #（n,2）
        if len(wh)==0: continue
        # [n,1,2]
        wh = np.expand_dims(wh, -2)
        box_maxes = wh / 2.
        box_mins = -box_maxes

        # 计算真实框和哪个先验框最契合
        intersect_mins = np.maximum(box_mins, anchor_mins)
        intersect_maxes = np.minimum(box_maxes, anchor_maxes)
        intersect_wh = np.maximum(intersect_maxes - intersect_mins, 0.)
        # 先验框与真实框交集面积
        intersect_area = intersect_wh[..., 0] * intersect_wh[..., 1]
        # 真实框面积
        box_area = wh[..., 0] * wh[..., 1]
        # 先验框面积
        anchor_area = anchors[..., 0] * anchors[..., 1]
        # 计算IOU
        iou = intersect_area / (box_area + anchor_area - intersect_area)
        # 只选出每个achor下的box中IOU最大的那个，决定使用哪一个achor
        # 返回一个使用最大的anchor的下标
        best_anchor = np.argmax(iou, axis=-1)

        # 找到由哪个特征层的哪个网格预测的
        for t, n in enumerate(best_anchor):
            for l in range(num_layers):
                if n in anchor_mask[l]:
                    # floor用于向下取整
                    # 把x映射到特征层上（13*13特征层）
                    # true_boxes是除以416归一化后的结果
                    i = np.floor(true_boxes[b,t,0]*grid_shapes[l][1]).astype('int32')
                    # 把y映射到特征层上（13*13特征层）
                    j = np.floor(true_boxes[b,t,1]*grid_shapes[l][0]).astype('int32')
                    # 找到真实框在特征层l中第b副图像对应的位置
                    #第几个anchor
                    k = anchor_mask[l].index(n)
                    # class id
                    c = true_boxes[b,t, 4].astype('int32')
                    y_true[l][b, j, i, k, 0:4] = true_boxes[b,t, 0:4]
                    # 置信度为1，表示有物体
                    y_true[l][b, j, i, k, 4] = 1
                    y_true[l][b, j, i, k, 5+c] = 1
    # 这样就把真实图片上标注好坐标，转换到对应的特征层上（13*13）
    return y_true

#if __name__ == "__main__":
def _main():
    # 标签的位置
    annotation_path = 'train.txt'
    # 获取classes和anchor的位置
    classes_path = 'model_data/voc_classes.txt'
    anchors_path = 'model_data/yolo_anchors.txt'
    # # 预训练模型的位置
    # weights_path = 'model_data/yolov3.h5'
    # 获得classes和anchor
    class_names = get_classes(classes_path)
    anchors = get_anchors(anchors_path)
    # 一共有多少类
    num_classes = len(class_names)
    num_anchors = len(anchors)
    # 训练后的模型保存的位置
    log_dir = 'logs/'
    # 输入的shape大小
    input_shape = (416, 416)
    # 清除session
    K.clear_session()
    # 输入的图像为
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    # 创建yolo模型
    print('Create YOLOv3 base_model with {} anchors and {} classes.'.format(num_anchors, num_classes))
    model_body = yolo_body(image_input, num_anchors // 3, num_classes)

    # # 载入预训练权重
    # print('Load weights {}.'.format(weights_path))
    # model_body.load_weights(weights_path, by_name=True, skip_mismatch=True)

    # y_true为13,13,3,85
    # 26,26,3,85
    # 52,52,3,85
    y_true = [Input(shape=(h // {0: 32, 1: 16, 2: 8}[l], w // {0: 32, 1: 16, 2: 8}[l], \
                           num_anchors // 3, num_classes + 5)) for l in range(3)]
    # 输入为*model_body.input, *y_true
    # 输出为model_loss
    loss_input = [*model_body.output, *y_true]
    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
                        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.5})(loss_input)
    model = Model([model_body.input, *y_true], model_loss)
    # 训练参数设置
    # 1保存地址 2每过2个周期进行一次保存 3loss值不下降的话调整学习率 4出现过拟合提前停止
    logging = TensorBoard(log_dir=log_dir)
    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
                                 monitor='val_loss', save_weights_only=True, save_best_only=False, period=1)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
    #reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, verbose=1)
    #early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=1000, verbose=1)
    # 0.1用于验证，0.9用于训练
    val_split = 0.1
    with open(annotation_path) as f:
        lines = f.readlines()
    np.random.seed(10101)
    np.random.shuffle(lines)
    np.random.seed(None)
    num_val = int(len(lines) * val_split)
    num_train = len(lines) - num_val

    # 第一次训练，对之前的层（249）冻结，训练
    # 这是粗略的训练
    if True:
        model.compile(optimizer=Adam(lr=1e-3), loss={
            'yolo_loss': lambda y_true, y_pred: y_pred})
        # 批次大小，显存小就调小
        # 调整为2的次幂，如2,4,8,16,32,64
        batch_size = 8
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator(lines[:num_train], batch_size, input_shape, anchors, num_classes),
                            steps_per_epoch=max(1, num_train // batch_size),
                            validation_data=data_generator(lines[num_train:], batch_size, input_shape, anchors,
                                                           num_classes),
                            validation_steps=max(1, num_val // batch_size),
                            epochs=100,
                            initial_epoch=0,
                            callbacks=[logging,checkpoint],
                            #callbacks=[logging,checkpoint,reduce_lr,early_stopping],
                            verbose=1)
        model.save_weights(log_dir + 'yolov3_self_20000.h5')
    # Unfreeze and continue training, to fine-tune.
    # Train longer if the result is not good.
    if True:
        for i in range(len(model.layers)):
            model.layers[i].trainable = True
        model.compile(optimizer=Adam(lr=1e-4), loss={'yolo_loss': lambda y_true, y_pred: y_pred}) # recompile to apply the change
        print('Unfreeze all of the layers.')

        batch_size = 4 # note that more GPU memory is required after unfreezing the body
        print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
        model.fit_generator(data_generator(lines[:num_train], batch_size, input_shape, anchors, num_classes),
            steps_per_epoch=max(1, num_train//batch_size),
            validation_data=data_generator(lines[num_train:], batch_size, input_shape, anchors, num_classes),
            validation_steps=max(1, num_val//batch_size),
            epochs=200,
            initial_epoch=50,
            callbacks=[logging, checkpoint, reduce_lr, early_stopping])
        model.save_weights(log_dir + 'trained_weights_VGG16x1x2Cluster_20000.h5')

    # Further training if needed.


def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)


def create_model(input_shape, anchors, num_classes, load_pretrained=False, freeze_body=2,
            weights_path='model_data/ep088-loss5.418-val_loss5.999.h5'):
    '''create the training model'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)

    y_true = [Input(shape=(h//{0:32, 1:16, 2:8}[l], w//{0:32, 1:16, 2:8}[l], \
        num_anchors//3, num_classes+5)) for l in range(3)]

    model_body = yolo_body(image_input, num_anchors//3, num_classes)
    print('Create YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))

    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze darknet53 body or freeze all but 3 output layers.
            num = (185, len(model_body.layers)-3)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = True
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))

    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.5})(
        [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)

    return model

def create_tiny_model(input_shape, anchors, num_classes, load_pretrained=True, freeze_body=2,
            weights_path='model_data/ep088-loss5.418-val_loss5.999.h5'):
    '''create the training model, for Tiny YOLOv3'''
    K.clear_session() # get a new session
    image_input = Input(shape=(None, None, 3))
    h, w = input_shape
    num_anchors = len(anchors)

    y_true = [Input(shape=(h//{0:32, 1:16}[l], w//{0:32, 1:16}[l], \
        num_anchors//2, num_classes+5)) for l in range(2)]

    model_body = tiny_yolo_body(image_input, num_anchors//2, num_classes)
    print('Create Tiny YOLOv3 model with {} anchors and {} classes.'.format(num_anchors, num_classes))

    if load_pretrained:
        model_body.load_weights(weights_path, by_name=True, skip_mismatch=True)
        print('Load weights {}.'.format(weights_path))
        if freeze_body in [1, 2]:
            # Freeze the darknet body or freeze all but 2 output layers.
            num = (20, len(model_body.layers)-2)[freeze_body-1]
            for i in range(num): model_body.layers[i].trainable = False
            print('Freeze the first {} layers of total {} layers.'.format(num, len(model_body.layers)))

    model_loss = Lambda(yolo_loss, output_shape=(1,), name='yolo_loss',
        arguments={'anchors': anchors, 'num_classes': num_classes, 'ignore_thresh': 0.7})(
        [*model_body.output, *y_true])
    model = Model([model_body.input, *y_true], model_loss)

    return model

def data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes):
    '''data generator for fit_generator'''
    n = len(annotation_lines)
    i = 0
    while True:
        image_data = []
        box_data = []
        for b in range(batch_size):
            if i==0:
                np.random.shuffle(annotation_lines)
            image, box = get_random_data(annotation_lines[i], input_shape, random=True)
            image_data.append(image)
            box_data.append(box)
            i = (i+1) % n
        image_data = np.array(image_data)
        box_data = np.array(box_data)
        y_true = preprocess_true_boxes(box_data, input_shape, anchors, num_classes)
        yield [image_data, *y_true], np.zeros(batch_size)

def data_generator_wrapper(annotation_lines, batch_size, input_shape, anchors, num_classes):
    n = len(annotation_lines)
    if n==0 or batch_size<=0: return None
    return data_generator(annotation_lines, batch_size, input_shape, anchors, num_classes)

if __name__ == '__main__':
    _main()

