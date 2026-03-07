import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# düz çizgi çekmek için

cv2.line(img,(0,0),(511,511),(255,0,0),5) #sırayla:üzerine çizilecek görsel, başlangıç-bitiş koordinatları,renk,piksel
cv2.line(img,(50,400),(400,50),(255,255,255),19)

# dörtgen çizmek için

cv2.rectangle(img,(19,19),(200,200),(0,0,255),5)
cv2.rectangle(img,(200,200),(511, 511),(0,0,255),-1) #-1 içini boyamasını sağlar

#çember - daire çizmek için
cv2.circle(img,(55,55),55,(190,190,190),2) #3.parametre yarıçap. 
cv2.circle(img,(190,190),90,(190,190,190),-1) #-1 içini doldurur

#elips çizmek için
cv2.ellipse(img,(200,200),(100,50),0,0,180,(0,0,0),3)

#çokgen çizmek için

pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2 = pts.reshape(-1,1,2) #4 tane grup, her grupta 1 nokta ve her noktanın 2 koordinatı var
# neden reshape?
#veriyi standart olan (Nokta Sayısı, 1, 2) formatına getirmek amacıyla kullanılır.
cv2.polylines(img,[pts2],True,(200,200,200),3)


#yazı yazmka için

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'Zeynep',(0,300),font,4,(0,155,155),2,cv2.LINE_AA)



cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()