import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('aadc.jpeg')

# Konversi BGR ke RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Buat kernel: matriks berukuran 3 x 5
kernel = np.ones((3, 5), np.float32) * 0.09
print(kernel)

# Lakukan filtering
filtered_img = cv2.filter2D(img, -1, kernel)

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15, 15)

# plot pertama, gambar asli
plt.subplot(121), plt.imshow(rgb_img), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Ubah warna hasil filter menjadi asli (BGR)
filtered_rgb_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)

# kedua, hasil filter
plt.subplot(122), plt.imshow(filtered_rgb_img), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Plot!
plt.show()

blur = cv2.blur(img,(5,5))#Baris ini menghasilkan gambar yang telah di-blur menggunakan metode rata-rata dengan ukuran kernel 5x5.
cv2.imshow('blur Image', blur)# Fungsi cv2.imshow() digunakan untuk menampilkan gambar dalam jendela.
cv2.waitKey(0)#Baris ini akan menunggu tombol keyboard ditekan. Angka 0 menunjukkan bahwa program akan berhenti dan menunggu hingga tombol keyboard ditekan.

kernel = np.matrix([#: Baris ini mendefinisikan sebuah matriks kernel dengan ukuran 3x3. Kernel ini digunakan untuk filtering gambar dengan metode filter2D.
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)#Baris ini mencetak matriks kernel ke konsol. Ini berguna untuk melihat nilai-nilai dalam matriks kernel.

# buat lagi filteringnya
filter = cv2.filter2D(img,-1,kernel)#Baris ini menerapkan operasi filter 2D pada gambar img menggunakan kernel yang telah ditentukan sebelumnya. -1 menunjukkan bahwa kedalaman gambar output harus sama dengan kedalaman gambar input.

# tampilkan
cv2.imshow('blur Image', filter)#Baris ini menampilkan gambar hasil filtering ke dalam jendela yang bernama 'blur Image'.
cv2.waitKey(0)#Baris ini akan menunggu tombol keyboard ditekan. Program akan berhenti dan menunggu hingga tombol keyboard ditekan sebelum keluar.