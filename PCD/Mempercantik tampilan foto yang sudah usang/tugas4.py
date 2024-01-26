import cv2

img = cv2.imread("3.jpg")

# Aplikasikan filter Gaussian
gaussian = cv2.GaussianBlur(img, (1, 1), 0)

# Menampilkan gambar asli dan hasilnya
cv2.imshow("Original Image", img)
cv2.imshow("Improved Image", gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()