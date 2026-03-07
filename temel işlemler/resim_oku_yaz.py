import cv2
   
   
#    #okumaaa
# img = cv2.imread('deneme.jpg',cv2.IMREAD_GRAYSCALE)  #bu grileştirir. sadece 0 da aynnı işlem

# cv2.imshow('resimmmm', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


     #yazmaaaa
     
img = cv2.imread('deneme.jpg',0)

cv2.imwrite('deneme2.jpg', img)