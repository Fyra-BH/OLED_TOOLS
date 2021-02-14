import cv2 as cv
import my_cvt
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : python", sys.argv[0] + " filename(eg : XXX.mp4)")
        exit(0)
    video = cv.VideoCapture(sys.argv[1])
    fps = video.get(cv.CAP_PROP_FPS)
    size = (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
    os.system("mkdir out")
    video_writer = cv.VideoWriter('out/outputVideo.mp4', cv.VideoWriter_fourcc(*'XVID'), fps, size)
    # 将视频文件初始化为VideoCapture对象
    success, frame = video.read()
    # read()方法读取视频下一帧到frame，当读取不到内容时返回false!
    while success and cv.waitKey(1) & 0xFF != ord('q'):
        # 等待1毫秒读取键键盘输入，最后一个字节是键盘的ASCII码。ord()返回字母的ASCII码
        frame = my_cvt.dilate_demo(frame)
        video_writer.write(frame)
        cv.imshow('frame', frame)
        print(frame.shape)
        success, frame = video.read()

    cv.destroyAllWindows()
    video.release()
    video_writer.release()

# video = cv2.VideoCapture("street.mp4")
# fps = video.get(cv2.CAP_PROP_FPS)
# size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# # opencv支持不同的编码格式
# video_writer = cv2.VideoWriter('outputVideo.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, size)
# video = cv2.VideoCapture("street.mp4")
# success, frame = video.read()
# while success:
#     video_writer.write(frame)
#     success, frame = video.read()
