import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
from skimage import data

image = cv2.imread('Bandung.png', cv2.IMREAD_GRAYSCALE)  # Ubah ke citra ke skala keabuan
equalizer = cv2.equalizeHist(image)  # Menerapkan equalisasi histogram

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # Membuat objek CLAHE dengan parameter yang sesuai
image_clahe = clahe.apply(image)  # Menerapkan CLAHE pada citra

# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')

# Apply Min-Max Contrasting
# Create an empty array to store the final output
output = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')

# Apply Min-Max Contrasting
# Menghitung nilai minimum dan maksimum dari gambar
min_value = np.min(image)
max_value = np.max(image)

# Melakukan perulangan untuk setiap elemen dalam gambar
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # Mengaplikasikan rumus Min-Max Contrasting untuk mengubah nilai piksel
        output[i, j] = 255 * (image[i, j] - min_value) / (max_value - min_value)

# Membuat salinan gambar asli dan mengubah tipenya menjadi float
copyCamera = image.copy().astype(float)

# Mendapatkan dimensi dari copyCamera
m1, n1 = copyCamera.shape

# Membuat array kosong dengan dimensi m1 x n1
output1 = np.empty([m1, n1])


for baris in range(0, m1-1):#Melakukan perulangan untuk setiap nilai dalam rentang 0 hingga m1-2 (m1 dikurangi 1). Rentang ini mengacu pada indeks baris dalam matriks copyCamera.
    for kolom in range(0, n1-1):#Melakukan perulangan untuk setiap nilai dalam rentang 0 hingga n1-2 (n1 dikurangi 1). Rentang ini mengacu pada indeks kolom dalam matriks copyCamera.
        a1 = baris#Menyimpan nilai saat ini dari variabel baris ke variabel a1 dan menyimpan nilai saat ini dari variabel kolom ke variabel b1.
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9#Mengalikan nilai piksel pada posisi (baris, kolom) dalam matriks copyCamera dengan 1.9, dan hasilnya disimpan pada posisi (a1, b1) dalam matriks output1.
fig, axes = plt.subplots(5, 2, figsize=(20, 20))#Membuat sebuah figure dengan 5 baris dan 2 kolom untuk menampung subplot. Ukuran figure ditentukan sebagai 20x20.
ax = axes.ravel()#Mendapatkan sumbu/subplot dari figure yang telah dibuat dan menyimpannya dalam variabel ax. ravel()

ax[0].imshow(image, cmap=plt.cm.gray)# Menampilkan citra image pada subplot pertama (ax[0]) dengan menggunakan colormap gray.
ax[0].set_title("Citra Input")#Mengatur judul subplot pertama menjadi "Citra Input".
ax[1].hist(image.ravel(), bins=256)#Menampilkan histogram dari image pada subplot kedua (ax[1]) dengan menggunakan 256 bins.
ax[1].set_title('Histogram Input')#Mengatur judul subplot kedua menjadi "Histogram Input".

ax[2].imshow(equalizer, cmap=plt.cm.gray)# Menampilkan citra image pada subplot pertama (ax[2]) dengan menggunakan colormap gray.
ax[2].set_title("Citra Output HE")#Mengatur judul subplot pertama menjadi "Citra output".
ax[3].hist(equalizer.ravel(), bins=256)#Menampilkan histogram dari image pada subplot kedua (ax[2]) dengan menggunakan 256 bins.
ax[3].set_title('Histogram Output HE Method')#Mengatur judul subplot kedua menjadi "Histogram output".

ax[4].imshow(image_cs, cmap=plt.cm.gray)# Menampilkan citra image pada subplot pertama (ax[4]) dengan menggunakan colormap gray.
ax[4].set_title("Citra Output CS")#Mengatur judul subplot pertama menjadi "Citra output".
ax[5].hist(image_cs.ravel(), bins=256)#Menampilkan histogram dari image pada subplot kedua (ax[5]) dengan menggunakan 256 bins.
ax[5].set_title('Histogram Output CS Method')#Mengatur judul subplot kedua menjadi "Histogram output".

ax[6].imshow(image_clahe, cmap=plt.cm.gray)# Menampilkan citra image pada subplot pertama (ax[6]) dengan menggunakan colormap gray.
ax[6].set_title("Citra Grayscale CLAHE")#Mengatur judul subplot pertama menjadi "Citra output".
ax[7].hist(image_clahe.ravel(), bins=256)#Menampilkan histogram dari image pada subplot kedua (ax[7]) dengan menggunakan 256 bins.
ax[7].set_title('Histogram Output CLAHE Method')#Mengatur judul subplot kedua menjadi "Histogram output".

ax[8].imshow(output1, cmap=plt.cm.gray)# Menampilkan citra image pada subplot pertama (ax[8]) dengan menggunakan colormap gray.
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#Mengatur judul subplot pertama menjadi "Citra output".
ax[9].hist(output1.ravel(), bins=256)#Menampilkan histogram dari image pada subplot kedua (ax[9]) dengan menggunakan 256 bins.
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#Mengatur judul subplot kedua menjadi "Histogram output".

fig.tight_layout()#Langkah yang sama dilakukan untuk citra output1 dan histogramnya dengan menggunakan subplot kesembilan dan kesepuluh.
plt.show()
