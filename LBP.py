import cv2
import numpy as np

img = cv2.imread("/home/pi/Desktop/road3.jpg",0)


x = img.shape; #image size

dst = np.zeros(img.shape,np.uint8) # output

#print(x[0])
#LBP_Array = [[0]*x[1] for i in range(x[0])]
    
for i in range(x[0]):
    for j in range(x[1]):
        i1 =i
        j1 =j
        if( (i1+2 > x[0]) or (i1-2 < 0) or (j1+2 >x[1]) or (j1-2 < 0)):
            continue
        LBPPoint = 0
        color = img[i,j]
        com1= img [i+1,j]
        com2= img [i+1,j+1]
        com3= img [i,j-1]
        com4= img [i-1,j-1]
        com5= img [i-1,j]
        com6= img [i-1,j+1]
        com7= img [i,j+1]
        com8= img [i+1,j+1]
        if(color>com1):
            LBPPoint += 1
        if(color >com2):
            LBPPoint += 2
        if(color > com3):
            LBPPoint += 4
        if(color >com4):
            LBPPoint += 8
        if(color >com5):
            LBPPoint += 16
        if(color >com6):
            LBPPoint += 32
        if(color >com7):
            LBPPoint += 64
        if(color >com8):
            LBPPoint += 128
        dst[i,j] =LBPPoint
        
        

cv2.imshow("abc",dst)


cv2.waitKey()
