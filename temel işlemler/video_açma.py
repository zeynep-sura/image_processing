import cv2 

cap = cv2.VideoCapture('video.mp4')

if cap.isOpened() == False:
    print('videoya erişilemedi')

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('frame', frame)
        
        kInp = cv2.waitKey(30)
        if kInp == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()

