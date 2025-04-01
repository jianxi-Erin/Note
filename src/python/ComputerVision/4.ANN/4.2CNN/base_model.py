# 定义了一个简单的CNN卷积神经网络模型
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # 第一层卷积层
        # 输入通道数为3（例如RGB图像），输出通道数为32，卷积核大小为3x3，padding为1
        # padding=1的作用是保持特征图的尺寸在卷积操作后不变
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        
        # 第二层卷积层
        # 输入通道数为32（上一层的输出通道数），输出通道数为64，卷积核大小为3x3，padding为1
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        
        # 第三层卷积层
        # 输入通道数为64，输出通道数为128，卷积核大小为3x3，padding为1
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1) 
        
        # 池化层(平均或最大的无数字卷积层)
        # 使用最大池化，池化窗口大小为2x2，步长为2
        # 池化的作用是降低特征图的空间维度，减少计算量，同时保留重要特征
        self.pool = nn.MaxPool2d(2, 2)
        
        # 第一层全连接层
        # 输入特征数为128 * 4 * 4（假设输入图像经过前面的卷积和池化后，特征图大小为4x4）
        # 输出特征数为512
        self.fc1 = nn.Linear(128 * 4 * 4, 512)
        
        # 第二层全连接层
        # 输入特征数为512，输出特征数为256
        self.fc2 = nn.Linear(512, 256)
        
        # 第三层全连接层（输出层）
        # 输入特征数为256，输出特征数为10（假设是10分类问题）
        self.fc3 = nn.Linear(256, 10)
        
        # Dropout层
        # Dropout率设置为0.5，用于防止过拟合
        # 在训练过程中，随机丢弃一部分神经元的输出，增强模型的泛化能力
        self.dropout = nn.Dropout(0.5)
        
    def forward(self, x):
        # 第一次卷积 + ReLU激活 + 池化
        # 对输入图像进行卷积操作，然后通过ReLU激活函数引入非线性，最后进行池化操作
        x = self.pool(nn.functional.relu(self.conv1(x)))
        
        # 第二次卷积 + ReLU激活 + 池化
        x = self.pool(nn.functional.relu(self.conv2(x)))
        
        # 第三次卷积 + ReLU激活 + 池化
        x = self.pool(nn.functional.relu(self.conv3(x)))
        
        # 展平操作
        # 将三维的特征图展平为一维的向量，以便输入到全连接层
        # 假设经过前面的操作后，特征图的大小为128 * 4 * 4
        x = x.view(-1, 128 * 4 * 4)
        
        # 第一层全连接层 + Dropout + ReLU激活
        # 全连接层对特征进行进一步的组合和学习，然后通过Dropout防止过拟合，最后通过ReLU激活
        x = self.dropout(nn.functional.relu(self.fc1(x)))
        
        # 第二层全连接层 + Dropout + ReLU激活
        x = self.dropout(nn.functional.relu(self.fc2(x)))
        
        # 第三层全连接层（输出层）
        # 最后一层全连接层输出最终的分类结果
        x = self.fc3(x)
        
        return x