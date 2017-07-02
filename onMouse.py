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
        self.lables=[0,1,2,3]
        self.iter=0
    def on_mouse(self,event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.pt0=(x,y)
            self.drawing=False
            #self.bboxes.clear()
        elif event==cv2.EVENT_LBUTTONUP:
            if self.drawing:
                self.bboxes.append([self.pt0,self.pt1])
            self.drawing=False
        elif event==cv2.EVENT_RBUTTONDOWN:
            pass
        elif event==cv2.EVENT_RBUTTONUP:
            for (pt0,pt1) in self.bboxes:
                if x>pt0[0] and x< pt1[0] and y>pt0[1] and y<pt1[1]:
                    self.bboxes.remove([pt0,pt1])
        elif event==cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):            
            if x< self.pt0[0] or y<self.pt0[1]:
                print("Please begin paint from left-up corner")
                self.drawing=False
            else:
                self.pt1=(x,y)
                self.drawing=True
        elif event==cv2.EVENT_FLAG_RBUTTON:
            pass
        elif event==cv2.EVENT_MOUSEWHEEL:
            print(flags)
            if flags>0:                
                if 0==self.iter:
                    self.iter=3
                else:
                    self.iter-=1
            else:
                if 3==self.iter:
                    self.iter=0
                else:
                    self.iter+=1
            print(self.lables[self.iter])
    def drawBox(self):
        self.tepImg=self.img.copy()
        for (pt0,pt1) in self.bboxes:
            cv2.rectangle(self.tepImg,pt0,pt1,(0,0,255),2)
        if self.drawing:
            cv2.rectangle(self.tepImg,self.pt0,self.pt1,(0,0,255),2)
    def saveimages(self):
        self.tepImg=self.img.copy()
        for (pt0,pt1) in self.bboxes:
            img=self.tepImg[pt0[0]:pt1[0],pt0[1]:pt1[1],:]
            cv2.imwrite("",img)
    def start(self):
        cv2.namedWindow('lena',cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('lena',self.on_mouse)
        self.img=cv2.imread(self.imgPath)
        self.tepImg=self.img.copy()
        key=0
        while key!=27:
            self.drawBox()
            cv2.imshow('lena',self.tepImg)
            key=cv2.waitKey(1)
            "防止误点窗口关闭"
            if 8==key:
                self.bboxes.clear()
            elif 115==key:
                self.saveimages()
            cv2.setMouseCallback('lena',self.on_mouse)
            
        cv2.destroyAllWindows()
if __name__=='__main__':
    srcPath='./lena.jpg'
    bbox=BBoxDrawing(srcPath)
    bbox.start()
    
