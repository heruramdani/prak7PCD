import cv2
import numpy as np
from matplotlib import pyplot as plt

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('aadc.jpeg', 0)

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (12, 8)

# Membagi layout menjadi 2 baris dan 3 kolom
fig, axs = plt.subplots(2, 3)

# Menampilkan gambar asli
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 0].axis('off')

# Menampilkan histogram gambar asli
axs[1, 0].hist(img.ravel(), 256, [0, 256], color='blue')
axs[1, 0].set_title('Histogram - Original')

# Menampilkan gambar Laplacian
axs[0, 1].imshow(laplacian, cmap='gray')
axs[0, 1].set_title('Laplacian')
axs[0, 1].axis('off')

# Menampilkan histogram Laplacian
axs[1, 1].hist(laplacian.ravel(), 256, [0, 256], color='blue')
axs[1, 1].set_title('Histogram - Laplacian')

# Menampilkan gambar Sobel X
axs[0, 2].imshow(sobelx, cmap='gray')
axs[0, 2].set_title('Sobel X')
axs[0, 2].axis('off')

# Menampilkan histogram Sobel X
axs[1, 2].hist(sobelx.ravel(), 256, [0, 256], color='blue')
axs[1, 2].set_title('Histogram - Sobel X')

# Atur jarak antar subplot menjadi 0.5
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# Menampilkan plot
plt.show()
