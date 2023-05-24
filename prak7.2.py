import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Bandung.png')#Membaca gambar dengan nama file 'Bandung.png' menggunakan fungsi cv2.imread() dan menyimpannya dalam variabel img.

row, column, _ = img.shape#Mendapatkan ukuran baris, kolom, dan jumlah saluran warna (biasanya 3 untuk gambar RGB) dari img.shape dan menyimpannya dalam variabel row, column, dan _.

img1 = np.zeros((row, column), dtype=np.uint8)#embuat matriks kosong dengan ukuran yang sama dengan gambar img menggunakan np.zeros() dan menyimpannya dalam variabel img1

min_range = 10#Menentukan rentang nilai minimum dan maksimum untuk setiap saluran warna (BGR) yang akan digunakan untuk memfilter gambar.
max_range = 60#Nilai piksel yang berada di dalam rentang ini akan diberi nilai 255, sedangkan nilai piksel di luar rentang akan diberi nilai 0.

for i in range(row):#Melakukan perulangan untuk setiap piksel dalam gambar menggunakan nested loop.
    for j in range(column):
        if min_range < img[i, j, 0] < max_range and min_range < img[i, j, 1] < max_range and min_range < img[i, j, 2] < max_range:
            img1[i, j] = 255#Pada setiap iterasi, dilakukan pengecekan apakah nilai piksel di setiap saluran warna (BGR) berada dalam rentang yang ditentukan.
        else:
            img1[i, j] = 0#ika ya, nilai piksel dalam img1 diatur menjadi 255 (putih), jika tidak, diatur menjadi 0 (hitam).

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()# Membuat sebuah figure dengan 2 baris dan 2 kolom untuk menampung subplot. Ukuran figure ditentukan sebagai 12x12.

ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))#Citra input ditampilkan dengan menggunakan imshow()
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')#sementara histogram input ditampilkan dengan menggunakan hist()

ax[2].imshow(img1, cmap='gray')#Citra output ditampilkan dengan menggunakan imshow()
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')#sementara histogram output ditampilkan dengan menggunakan hist()

plt.show()
