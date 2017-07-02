import cv2
k=0
while k!=27:
    src=cv2.imread('./lena.jpg')
    cv2.imshow('lena',src)
    k=cv2.waitKey(1)  
    print(k)
cv2.destroyAllWindows()