import cv2

img = cv2.imread('deneme.jpg')
img_gray = cv2.imread('deneme.jpg', 0)

#      # item == renklerin oranları gibi bir değer

# print('blue: ', img.item(10,10,0))
# print('green: ', img.item(10,10,1))
# print('red: ' ,img.item(10,10,2))

# print(img[10,10])

 
       # itemset = herhangi bir noktadaki değeri değiştirmeye yarayan yapı 
       #bu çalışmıyo güncel haliyel yaptım


# for y in range(50):
#     for x in range(50):
#         img[y,x,0] = 0
#         img[y,x,1] = 0

# cv2.imshow('deneme', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#shape = bpyut gösterir

# print(img.shape)


# ROI Presimden parça alıuo

roi = img[250:300, 200: 250]
cv2.imshow('parca', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()