import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("resim")

cv2.createTrackbar("R", "resim",0,255,nothing)
cv2.createTrackbar("G", "resim",0,255,nothing)
cv2.createTrackbar("B", "resim",0,255,nothing)
cv2.createTrackbar("On/Off","resim",0,1,nothing)

while(1):
    cv2.imshow("resim",img)

    
    r = cv2.getTrackbarPos("R","resim")
    g = cv2.getTrackbarPos("G","resim")
    b = cv2.getTrackbarPos("B","resim")
    
    switch = cv2.getTrackbarPos("On/Off","resim")
    
    if switch:
        img[:] = [b,g,r]
    else:
        img[:] = 0
    
    
    if cv2.waitKey(1)& 0xFF ==27:
        break
    
        
cv2.destroyAllWindows()
    