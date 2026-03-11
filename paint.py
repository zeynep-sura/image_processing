import cv2
import numpy as np
import math
cizim = False
mod = False
xi,yi = -1,-1

def draw(event,x,y,flags,param):
    global cizim,xi,yi,mod

    if event== cv2.EVENT_LBUTTONDOWN:
        xi,yi = x,y
        cizim = True     
    elif event == cv2.EVENT_MOUSEMOVE:
        
        if cizim == True:
            if mod:
                radius = math.sqrt((x-xi)**2 + (y-yi)**2)
                cv2.circle(img,(xi,yi),int(radius),(0,0,0),-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),(155,155,155),-1)
        else:
            pass
    
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False        
        
    

img = np.ones((1024,1024,3),np.uint8) * 255
cv2.namedWindow("paint")
cv2.setMouseCallback("paint",draw)

while(1):
    cv2.imshow("paint",img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break
    elif k == ord("m"):
        mod = not mod
        
cv2.destroyAllWindows()