import numpy as np
import cv2

class BBoxDrawing:
    def __init__(self,imgPath,pt0=(-1,-1),pt1=(-1,-1)):
        self.pt0=pt0
        self.pt1=pt1
        self.drawing=False
        self.imgPath=imgPath
        self.img=None
        self.tepImg=None
        self.bboxes=[]
    def on_mouse(self,event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.pt0=(x,y)
            self.drawing=False
            #self.bboxes.clear()
        elif event==cv2.EVENT_LBUTTONUP:
            self.drawing=False
            self.bboxes.append([self.pt0,self.pt1])
        elif event==cv2.EVENT_RBUTTONDOWN:
            pass
        elif event==cv2.EVENT_RBUTTONUP:
            for (pt0,pt1) in self.bboxes:
                if x>pt0[0] and x< pt1[0] and y>pt0[1] and y<pt1[1]:
                    self.bboxes.remove([pt0,pt1])
        elif event==cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
            self.pt1=(x,y)
            self.drawing=True
        elif event==cv2.EVENT_FLAG_RBUTTON:
            pass
    def drawBox(self):
        self.tepImg=self.img.copy()
        for (pt0,pt1) in self.bboxes:
            cv2.rectangle(self.tepImg,pt0,pt1,(0,0,255),2)
        if self.drawing:
            cv2.rectangle(self.tepImg,self.pt0,self.pt1,(0,0,255),2)
    def start(self):
        cv2.namedWindow('lena')
        cv2.setMouseCallback('lena',self.on_mouse)
        self.img=cv2.imread(self.imgPath)
        self.tepImg=self.img.copy()
        while True:
            self.drawBox()
            cv2.imshow('lena',self.tepImg)
            
            if 27==cv2.waitKey(1)&0xff:
                break
            "防止误点窗口关闭"
            cv2.namedWindow('lena')
            cv2.setMouseCallback('lena',self.on_mouse)
            
        cv2.destroyAllWindows()
if __name__=='__main__':
    srcPath='./lena.jpg'
    bbox=BBoxDrawing(srcPath)
    bbox.start()
    
