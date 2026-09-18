import cv2
import numpy as np

# baca gambar
img = cv2.imread('gambar.jpg')

if img is None:
    print("gambar tidak ditemukan")
    exit()

# tampilkan gambar asli
cv2.imshow('Gambar Asli', img)
cv2.waitKey(0)

# convert ke hsv buat filter warna
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# range warna merah (ada 2 range soalnya merah ada di ujung awal & akhir hue)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

hasil = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Mask', mask)
cv2.imshow('Hasil Filter Warna Merah', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ---------------- filter warna di video (webcam) ----------------

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    hasil = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Video Asli', frame)
    cv2.imshow('Filter Warna Merah', hasil)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()