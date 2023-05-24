import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load input images
citra1 = cv2.imread('Bandung.png')#Membaca citra 'Bandung.png' menggunakan fungsi cv2.imread() dan hasilnya disimpan dalam variabel citra1. Citra ini akan digunakan dalam proses selanjutnya.
print(citra1.shape)#Menampilkan bentuk (shape) citra citra1 menggunakan atribut shape. Hasilnya berupa tuple yang menyatakan dimensi citra dalam format (tinggi, lebar, jumlah_channel).

plt.imshow(citra1, cmap='gray')# Menampilkan citra citra1 menggunakan fungsi plt.imshow(). Argumen citra1 digunakan untuk menampilkan citra, sedangkan cmap='gray' digunakan untuk menampilkan citra dalam skala abu-abu.

kernel = np.array([[-1, 0, -1],#Membuat kernel/filter 3x3 dengan menggunakan numpy array. Kernel ini digunakan untuk melakukan operasi konvolusi pada citra.
                   [0, 4, 0],
                   [-1, 0, -1]])#Nilai-nilai pada kernel akan mempengaruhi hasil akhir dari operasi konvolusi.

citraOutput = cv2.filter2D(citra1, -1, kernel)#Melakukan operasi konvolusi pada citra citra1 menggunakan fungsi cv2.filter2D()

fig, axes = plt.subplots(1, 2, figsize=(12, 12))#Membuat figure dengan dua subplot menggunakan fungsi plt.subplots(). Argumen pertama adalah jumlah baris subplot, argumen kedua adalah jumlah kolom subplot, dan argumen ketiga adalah ukuran figure dalam satuan inch.
ax = axes.ravel()#Membuat variabel ax yang merupakan versi flat dari axes. Hal ini berguna untuk mempermudah pengindeksan saat melakukan plotting pada setiap subplot.

ax[0].imshow(citra1, cmap = 'gray')# Menampilkan citra image pada subplot pertama (ax[0]) dengan menggunakan colormap gray.
ax[0].set_title("Citra Input")#Mengatur judul subplot pertama menjadi "Citra input"
ax[1].imshow(citraOutput, cmap = 'gray')# Menampilkan citra image pada subplot pertama (ax[0]) dengan menggunakan colormap gray.
ax[1].set_title("Citra Output")#Mengatur judul subplot pertama menjadi "Citra output"
plt.show()