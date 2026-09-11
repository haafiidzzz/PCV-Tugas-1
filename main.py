import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    red_frame = frame.copy()

    tinggi, lebar, channel = frame.shape

    for y in range(tinggi):
        for x in range(lebar):
            B, G, R = frame[y, x]
            red_frame[y, x] = [0, 0, R]

    cv2.imshow("Webcam Filter Merah", red_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()