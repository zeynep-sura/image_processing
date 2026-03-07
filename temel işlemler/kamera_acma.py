import cv2

vid = cv2.VideoCapture(0)

print(vid.get(3))
print(vid.get(4))

# vid.set(3,320)
# vid.set(4,240)

while True:
    ret, frame = vid.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    kInp = cv2.waitKey(1)
    cv2.imshow('frame', frame)
    
    if kInp == ord('q'):
        break
    
vid.release()
cv2.destqroyWindow()