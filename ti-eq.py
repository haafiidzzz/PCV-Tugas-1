import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("gambar.jpg", cv2.IMREAD_GRAYSCALE)


def negative(img):
    L = 256
    return (L - 1) - img


def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    out = c * np.log(1 + img.astype(np.float64))
    return out.astype(np.uint8)


def power_law(img, gamma, c=1):
    norm = img.astype(np.float64) / 255
    out = c * (norm ** gamma) * 255
    return out.astype(np.uint8)


def get_histogram(img):
    hist = np.zeros(256, dtype=int)
    for val in img.ravel():
        hist[val] += 1
    return hist


def histogram_equalization(img):
    hist = get_histogram(img)
    total_pixel = img.size

    cdf = np.zeros(256, dtype=float)
    running = 0
    for i in range(256):
        running += hist[i]
        cdf[i] = running

    cdf_norm = cdf / total_pixel
    lut = np.round(cdf_norm * 255).astype(np.uint8)

    out = lut[img]
    return out, hist, get_histogram(out)


neg = negative(img)
log_img = log_transform(img)
gamma_img = power_law(img, gamma=0.5)
eq_img, hist_before, hist_after = histogram_equalization(img)

fig, ax = plt.subplots(2, 3, figsize=(14, 8))

ax[0, 0].imshow(img, cmap="gray")
ax[0, 0].set_title("Original")

ax[0, 1].imshow(neg, cmap="gray")
ax[0, 1].set_title("Negative")

ax[0, 2].imshow(log_img, cmap="gray")
ax[0, 2].set_title("Log Transform")

ax[1, 0].imshow(gamma_img, cmap="gray")
ax[1, 0].set_title("Power Law (gamma=0.5)")

ax[1, 1].imshow(eq_img, cmap="gray")
ax[1, 1].set_title("Histogram Equalization")

ax[1, 2].bar(range(256), hist_before, color="gray", alpha=0.6, label="before")
ax[1, 2].bar(range(256), hist_after, color="red", alpha=0.4, label="after")
ax[1, 2].set_title("Histogram Before vs After")
ax[1, 2].legend()

for a in ax.ravel()[:5]:
    a.axis("off")

plt.tight_layout()
plt.show()