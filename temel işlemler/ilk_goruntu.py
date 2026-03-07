import cv2


#resmi okuu

img = cv2.imread("deneme.jpg")

# ----------------------
# 2. Griye çevir
# ----------------------
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ----------------------
# 3. Blur uygula
# ----------------------
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)

# ----------------------
# 4. Kenar tespiti (Canny)
# ----------------------
img_edges = cv2.Canny(img_blur, 50, 150)

# ----------------------
# 5. Hepsini ekranda göster
# ----------------------
cv2.imshow("Orijinal", img)
cv2.imshow("Gri", img_gray)
cv2.imshow("Blur", img_blur)
cv2.imshow("Kenarlar", img_edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

