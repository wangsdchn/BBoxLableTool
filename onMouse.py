import numpy as np
import cv2
def on_mouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print x,y
    elif event==cv2.EVENT_LBUTTONUP:
        print x,y
    elif event==cv2.EVENT_RBUTTONDOWN:
        print x,y
    elif event==cv2.EVENT_RBUTTONUP:
        print x,y
if __name__=='__main__':
    src=cv2.imread('./lena.jpg')
    cv2.namedWindow('lena')
    cv2.setMouseCallback('lena',on_mouse)
    while True:
        cv2.imshow('lena',src)
        if 27==cv2.waitKey(0)&0xff:
	    exit()
