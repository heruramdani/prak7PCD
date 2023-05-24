import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('aadc.jpeg')# Membaca citra 'aadc.jpeg' menggunakan fungsi cv2.imread() dan hasilnya disimpan dalam variabel img. Citra ini akan digunakan dalam proses selanjutnya.

# Konversi BGR ke RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#engonversi format warna citra dari BGR (Blue-Green-Red) menjadi RGB (Red-Green-Blue) menggunakan fungsi cv2.cvtColor().

# Buat kernel: matriks berukuran 3 x 5
kernel = np.ones((3, 5), np.float32) * 0.04#Membuat kernel/filter dengan menggunakan numpy array. Kernel ini berukuran 3x5 dan diisi dengan nilai 0.04.
print(kernel)#Kernel ini akan digunakan dalam operasi filtering.

# Lakukan filtering
filtered_img = cv2.filter2D(img, -1, kernel)#Melakukan operasi filtering pada citra img menggunakan fungsi cv2.filter2D()

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15, 15)#Mengatur ukuran figure yang akan digunakan untuk plotting menggunakan matplotlib. Angka (15, 15) menunjukkan ukuran figure dalam satuan inch.

# plot pertama, gambar asli
plt.subplot(221), plt.imshow(rgb_img), plt.title('Original')#Membuat subplot pertama dengan menggunakan fungsi plt.subplot(). Angka (221) menunjukkan letak subplot dalam bentuk grid 2x2, yaitu pada baris pertama dan kolom pertama. plt.imshow() digunakan untuk menampilkan citra rgb_img pada subplot tersebut. plt.title() digunakan untuk memberikan judul pada subplot.
plt.xticks([]), plt.yticks([])#plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan penanda sumbu pada plot.

# Hitung histogram gambar asli
hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])#Menghitung histogram citra menggunakan fungsi cv2.calcHist(). Argumen pertama adalah citra yang akan dihitung histogramnya (img).

plt.subplot(222), plt.plot(hist_img, color='r')#embuat subplot kedua dengan menggunakan fungsi plt.subplot(). Angka (222) menunjukkan letak subplot dalam bentuk grid 2x2, yaitu pada baris pertama dan kolom kedua. plt.plot() digunakan untuk menggambar plot histogram dengan menggunakan data hist_img. color='r' digunakan untuk mengatur warna garis plot menjadi merah.
plt.title('Histogram Original')#plt.title() digunakan untuk memberikan judul pada subplot.
plt.xlim([0, 256])#plt.xlim([0, 256]) digunakan untuk mengatur batas sumbu x pada plot histogram.

# Ubah warna hasil filter menjadi asli (BGR)
filtered_rgb_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)#Mengonversi format warna citra hasil filtering dari BGR menjadi RGB menggunakan fungsi cv2.cvtColor()

# kedua, hasil filter
plt.subplot(223), plt.imshow(filtered_rgb_img), plt.title('Averaging')##Membuat subplot pertama dengan menggunakan fungsi plt.subplot(). Angka (221) menunjukkan letak subplot dalam bentuk grid 2x2, yaitu pada baris pertama dan kolom pertama. plt.imshow() digunakan untuk menampilkan citra rgb_img pada subplot tersebut. plt.title() digunakan untuk memberikan judul pada subplot.
plt.xticks([]), plt.yticks([])#plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan penanda sumbu pada plot.

# Hitung histogram gambar hasil filter
hist_filtered_img = cv2.calcHist([filtered_img], [0], None, [256], [0, 256])#: Menghitung histogram dari citra hasil filtering (filtered_img) menggunakan fungsi cv2.calcHist(). Argumen pertama adalah citra yang akan dihitung histogramnya, yaitu filtered_img.

plt.subplot(224), plt.plot(hist_filtered_img, color='r')#embuat subplot kedua dengan menggunakan fungsi plt.subplot(). Angka (222) menunjukkan letak subplot dalam bentuk grid 2x2, yaitu pada baris pertama dan kolom kedua. plt.plot() digunakan untuk menggambar plot histogram dengan menggunakan data hist_img. color='r' digunakan untuk mengatur warna garis plot menjadi merah.
plt.title('Histogram Filtered')#plt.title() digunakan untuk memberikan judul pada subplot.
plt.xlim([0, 256])#plt.xlim([0, 256]) digunakan untuk mengatur batas sumbu x pada plot histogram.

# Plot!
plt.tight_layout()#Mengatur layout plot agar lebih rapi menggunakan fungsi plt.tight_layout()
plt.show()#enampilkan semua plot yang telah dibuat menggunakan fungsi plt.show().
