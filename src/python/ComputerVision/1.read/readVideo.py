import cv2

# 读取视频
video_path = 0  # 替换为你的视频路径|0,1,2表示摄像头索引
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("视频加载失败，请检查路径是否正确")
else:
    while True:
        # 逐帧读取
        ret, frame = cap.read()
        if not ret:
            print("视频播放完毕或读取失败")
            break

        # 显示当前帧
        cv2.imshow('Video', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()