import matplotlib.pyplot as plt#Mengimpor modul matplotlib.pyplot yang digunakan untuk membuat visualisasi plot.

from skimage import data#Mengimpor modul data dari scikit-image yang berisi beberapa citra contoh.
from skimage.io import imread# Mengimpor fungsi imread dari scikit-image.io yang digunakan untuk membaca citra dari file.
from skimage.color import rgb2gray#Mengimpor fungsi rgb2gray dari scikit-image.color yang digunakan untuk mengubah citra menjadi skala abu-abu (grayscale).
import numpy as np#Mengimpor modul numpy yang digunakan untuk operasi matematika dan manipulasi array.
citra1 = imread(fname="mobil.tif")# Membaca citra dengan menggunakan fungsi imread dan menyimpannya ke variabel citra1. Citra tersebut dibaca dari file "mobil.tif".
citra2 = imread(fname="boneka2.tif")#Membaca citra dengan menggunakan fungsi imread dan menyimpannya ke variabel citra2. Citra tersebut dibaca dari file "boneka2.tif".

print('Shape citra 1 : ', citra1.shape)#Mencetak dimensi citra 1 menggunakan atribut shape untuk mengetahui ukuran citra tersebut.
print('Shape citra 1 : ', citra2.shape)# Mencetak dimensi citra 2 menggunakan atribut shape untuk mengetahui ukuran citra tersebut.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Membuat objek figure dan axes untuk menampilkan plot. Parameter (1, 2) menunjukkan bahwa akan ada 1 baris dan 2 kolom subplot. figsize=(10, 10) mengatur ukuran gambar plot.
ax = axes.ravel()#Mengubah objek axes menjadi array 1 dimensi menggunakan fungsi ravel() agar lebih mudah diakses.

ax[0].imshow(citra1, cmap = 'gray')#Menampilkan citra 1 pada subplot pertama dengan menggunakan imshow(). Parameter cmap = 'gray' mengatur skala warna plot menjadi grayscale.
ax[0].set_title("Citra 1")#Mengatur judul untuk subplot pertama.
ax[1].imshow(citra2, cmap = 'gray')#Menampilkan citra 2 pada subplot kedua dengan menggunakan imshow().
ax[1].set_title("Citra 2")#Mengatur judul untuk subplot kedua.

copyCitra1 = citra1.copy()#Membuat salinan citra 1 menggunakan fungsi copy().
copyCitra2 = citra2.copy()#Membuat salinan citra 2 menggunakan fungsi copy().

m1,n1 = copyCitra1.shape#Menyimpan dimensi citra 1 (jumlah baris dan kolom) ke dalam variabel m1 dan n1.
output1 = np.empty([m1, n1])#Membuat array kosong dengan ukuran yang sama dengan citra 1 menggunakan fungsi empty() dari numpy.

m2,n2 = copyCitra2.shape#Menyimpan dimensi citra 2 (jumlah baris dan kolom) ke dalam variabel m2 dan n2.
output2 = np.empty([m2, n2])#Membuat array kosong dengan ukuran yang sama dengan citra 2 menggunakan fungsi empty().
print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)

print('m1 : ',m1)
print('n1 : ',n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()

for baris in range(0, m1 - 1):# Melakukan perulangan untuk setiap baris pada citra 1.
    for kolom in range(0, n1 - 1):#Melakukan perulangan untuk setiap kolom pada citra 1.

        a1 = baris#Menyimpan nilai baris ke dalam variabel a1.
        b1 = kolom#Menyimpan nilai baris ke dalam variabel a1.

        arr = np.array([copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1, b1 + 1], \
                        copyCitra1[a1, b1 - 1], copyCitra1[a1, b1 + 1], copyCitra1[a1 + 1, b1 - 1], \
                        copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]])

        minPiksel = np.amin(arr);#p.amin(arr): Menemukan nilai piksel terkecil dalam array menggunakan fungsi amin() dari numpy.
        maksPiksel = np.amax(arr);#Menemukan nilai piksel terbesar dalam array menggunakan fungsi amax().

        if copyCitra1[baris, kolom] < minPiksel:#ggunakan kondisi untuk menentukan nilai piksel pada output citra 1 berdasarkan nilai piks
            output1[baris, kolom] = minPiksel
        else:
            if copyCitra1[baris, kolom] > maksPiksel:
                output1[baris, kolom] = maksPiksel
            else:
                output1[baris, kolom] = copyCitra1[baris, kolom]
for baris1 in range(0, m2 - 1):#elakukan perulangan untuk setiap baris pada citra 2.
    for kolom1 in range(0, n2 - 1):#Melakukan perulangan untuk setiap kolom pada citra 2.

        a1 = baris1# Menyimpan nilai baris1 ke dalam variabel a1.
        b1 = kolom1#Menyimpan nilai kolom1 ke dalam variabel b1.

        arr = np.array([copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1, b1 + 1],#embuat array dengan menggunakan nilai piksel dari citra 2 pada posisi yang ditentukan.
                        copyCitra2[a1, b1 - 1], copyCitra2[a1, b1 + 1], copyCitra2[a1 + 1, b1 - 1],
                        copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]])

        minPiksel = np.amin(arr);#Menemukan nilai piksel terkecil dalam array menggunakan fungsi amin() dari numpy.
        maksPiksel = np.amax(arr);# Menemukan nilai piksel terbesar dalam array menggunakan fungsi amax().

        if copyCitra2[baris1, kolom1] < minPiksel:#enggunakan kondisi untuk menentukan nilai piksel pada output citra 2 berdasarkan nilai piksel pada citra 2 dan nilai piksel terkecil dan terbesar yang telah ditemukan sebelumnya.
            output2[baris1, kolom1] = minPiksel
        else:
            if copyCitra2[baris1, kolom1] > maksPiksel:
                output2[baris1, kolom1] = maksPiksel
            else:
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))#Membuat objek figure dan axes baru untuk menampilkan plot dengan grid 2x2 (2 baris, 2 kolom) dan ukuran gambar plot 10x10.
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 2")

ax[2].imshow(output1, cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")
plt.show()