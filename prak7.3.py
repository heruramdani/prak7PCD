import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load citra
citra1 = cv2.imread('Bandung.png')#Membaca  gambar, 'Bandung.png'
citra2 = cv2.imread('aadc.jpeg')#Membaca  gambar, 'aadc.jpeg',

# Tampilkan shape citra
print('Shape citra 1:', citra1.shape)# Menampilkan bentuk (shape) dari  gambar menggunakan atribut shape pada objek citra.
print('Shape citra 2:', citra2.shape)# Menampilkan bentuk (shape) dari gambar menggunakan atribut shape pada objek citra.

# Tampilkan citra
fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Membuat sebuah figure dengan 1 baris dan 2 kolom untuk menampung subplot. Ukuran figure ditentukan sebagai 10x10.
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[0]) dengan menggunakan colormap gray.
ax[0].set_title("Citra 1")#Mengatur judul subplot pertama menjadi "Citra 1".
ax[1].imshow(citra2, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[1]) dengan menggunakan colormap gray.
ax[1].set_title("Citra 2")#Mengatur judul subplot pertama menjadi "Citra 2".

# Buat salinan citra sebagai tipe data float
copyCitra1 = citra1.copy().astype(float)# Membuat salinan citra pertama dan kedua dengan tipe data float. Salinan ini akan digunakan untuk proses filter dan pemrosesan selanjutnya.
copyCitra2 = citra2.copy().astype(float)#Menggunakan metode copy() untuk menghindari perubahan pada citra asli, dan astype(float) untuk mengonversi tipe data menjadi float.

# Buat array kosong untuk menyimpan output
m1, n1, _ = copyCitra1.shape#Menggunakan atribut shape untuk mendapatkan dimensi citra
output1 = np.empty([m1, n1])#lalu menginisialisasi array dengan np.empty() berdasarkan dimensi citra.

m2, n2, _ = copyCitra2.shape#Menggunakan atribut shape untuk mendapatkan dimensi citra
output2 = np.empty([m2, n2])#lalu menginisialisasi array dengan np.empty() berdasarkan dimensi citra.

# Proses filter rerata untuk citra 1
for baris in range(1, m1 - 1):#Melakukan iterasi pada setiap baris dan kolom dalam rentang tertentu pada citra kedua
    for kolom in range(1, n1 - 1):#Melakukan proses filter rerata pada citra pertama. Pada setiap piksel citra, diambil nilai piksel sekitarnya dan disimpan dalam dataA sebagai list.
        dataA = [copyCitra1[baris - 1, kolom - 1], copyCitra1[baris - 1, kolom], copyCitra1[baris - 1, kolom + 1],#Pada setiap iterasi, nilai piksel sekitar pada citra kedua diambil dan disimpan dalam dataA sebagai list. Nilai piksel tersebut diambil dari 9 lokasi yang berdekatan dalam citra kedua.
                 copyCitra1[baris, kolom - 1], copyCitra1[baris, kolom], copyCitra1[baris, kolom + 1],
                 copyCitra1[baris + 1, kolom - 1], copyCitra1[baris + 1, kolom], copyCitra1[baris + 1, kolom + 1]]

        output1[baris, kolom] = np.mean(dataA)#emudian, rata-rata dari nilai piksel di dataA dihitung menggunakan np.mean(), dan hasilnya disimpan pada piksel yang sesuai di output1.

# Proses filter rerata untuk citra 2
for baris in range(1, m2 - 1):#Melakukan iterasi pada setiap baris dan kolom dalam rentang tertentu pada citra kedua
    for kolom in range(1, n2 - 1):# Rentangnya adalah dari baris 1 hingga m2 - 1 (dimensi citra dikurangi 1) dan dari kolom 1 hingga n2 - 1 (dimensi citra dikurangi 1).
        dataA = [copyCitra2[baris - 1, kolom - 1], copyCitra2[baris - 1, kolom], copyCitra2[baris - 1, kolom + 1],
                 copyCitra2[baris, kolom - 1], copyCitra2[baris, kolom], copyCitra2[baris, kolom + 1],
                 copyCitra2[baris + 1, kolom - 1], copyCitra2[baris + 1, kolom], copyCitra2[baris + 1, kolom + 1]]
#Menyimpan hasil rata-rata pada piksel yang sesuai dalam output2.
        output2[baris, kolom] = np.mean(dataA)#Menghitung rata-rata dari nilai piksel dalam dataA menggunakan np.mean().

# Tampilkan hasil
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[0]) dengan menggunakan colormap gray.
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[1]) dengan menggunakan colormap gray.
ax[1].set_title("Input Citra 2")#Mengatur judul subplot pertama menjadi "Citra 2"

ax[2].imshow(output1, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[2]) dengan menggunakan colormap gray.
ax[2].set_title("Output Citra 1")#Mengatur judul subplot pertama menjadi "Citra 3"
ax[3].imshow(output2, cmap='gray')# Menampilkan citra image pada subplot pertama (ax[3]) dengan menggunakan colormap gray.
ax[3].set_title("Output Citra 2")#Mengatur judul subplot pertama menjadi "Citra 4"

plt.show()
