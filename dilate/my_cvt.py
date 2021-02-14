import cv2 as cv
import numpy as np
import sys

def dilate_demo(image):  #膨胀
    global s
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
    shape = binary.shape
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (6, 6))
    dst = cv.dilate(binary, kernel)
    dst = dst[..., np.newaxis] + np.zeros(image.shape)
    return dst.astype(np.uint8)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : python", sys.argv[0] + " filename(eg : XXX.jpg)")
        exit(0)
    src = cv.imread(sys.argv[1])  # 读取图片
    cv.namedWindow("input image")    # 创建GUI窗口,形式为自适应
    cv.imshow("input image", src)    # 通过名字将图像和窗口联系
    dst = dilate_demo(src)
    print(dst.shape)
    cv.imshow("output image", dst)    # 通过名字将图像和窗口联系
    cv.waitKey(0)   # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
    cv.destroyAllWindows()  # 销毁所有窗口
    input()
