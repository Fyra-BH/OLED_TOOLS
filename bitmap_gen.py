import cv2
import json
import os

# flat 函数用于将多维list转为一维list
def flat(l):
    for k in l:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)

f = open("settings.json")
js = json.loads(f.read())

cap = cv2.VideoCapture(js["input file"])
f_out = open(js["output file"],"wb")

while cap.isOpened():
        ret, frame = cap.read()
    # try:
        print('frame.shape:', frame.shape)
        cv2.imshow('frame', frame)    
        key = cv2.waitKey(delay=1)
        img = cv2.resize(frame,(128,64))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,img_out = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        point_map = list(flat(img_out.tolist()))  
        for i in range(len(point_map)):
            point_map[i] = 0 if point_map[i] == 0 else 1
        btary = []
        for k in range(8):
            for j in  range(128):
                bt = 0
                for i in range(8):
                    bt = bt * 2 + point_map[k * 128 * 8 + 128 * (7-i) + j]
                btary.append(bt)
        f_out.write(bytearray(btary))
    # except:break

f_out.close()
cap.release()
cv2.destroyAllWindows()
exit()
   