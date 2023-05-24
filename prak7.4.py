import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np

citra1 = imread(fname="mobil.tif")#Citra pertama dimuat dari file "mobil.tif" dan disimpan dalam variabel citra1
citra2 = imread(fname="boneka2.tif")#citra kedua dimuat dari file "boneka2.tif" dan disimpan dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)#citra kedua dimuat dari file "boneka2.tif" dan disimpan dalam variabel citra2.
print('Shape citra 1 : ', citra2.shape)# Informasi dimensi mencakup jumlah baris, jumlah kolom, dan jumlah saluran warna (channel) dari citra.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Kode ini membuat sebuah figure dengan dua subplot (1 baris, 2 kolom) menggunakan subplots dari matplotlib. Ukuran figure ditentukan sebagai (10, 10) menggunakan figsize.
ax = axes.ravel()#. Setiap subplot direpresentasikan oleh elemen-elemen dalam variabel ax

ax[0].imshow(citra1, cmap = 'gray')#Pada subplot pertama (ax[0]), citra pertama (citra1) ditampilkan menggunakan imshow dengan colormap 'gray',
ax[0].set_title("Citra 1")# judul subplot diatur sebagai "Citra 1" menggunakan set_title
ax[1].imshow(citra2, cmap = 'gray')# Pada subplot kedua (ax[1]), citra kedua (citra2) ditampilkan dan diatur judulnya sebagai "Citra 2".
ax[1].set_title("Citra 2")# diatur judulnya sebagai "Citra 2".

copyCitra1 = citra1.copy()#Kode di atas menggunakan metode copy() pada citra pertama
copyCitra2 = citra2.copy()#dilakukan inisialisasi array kosong dengan ukuran yang sesuai menggunakan np.empty()

m1,n1 = copyCitra1.shape#Kode ini mengambil dimensi (shape) dari citra yang telah digandakan
output1 = np.empty([m1, n1])# Dimensi tersebut ditugaskan ke m1, n1 (untuk copyCitra1)

m2,n2 = copyCitra2.shape#Kode ini mengambil dimensi (shape) dari citra yang telah digandakan
output2 = np.empty([m2, n2])#dilakukan inisialisasi array kosong dengan ukuran yang sesuai menggunakan np.empty()
print('Shape copy citra 1 : ', copyCitra1.shape)#Kode ini mencetak dimensi (shape) dari citra yang telah digandakan (copyCitra1)
print('Shape output citra 1 : ', output1.shape)#dimensi dari array kosong (output1) yang telah diinisialisasi.

print('m1 : ',m1)# dimensi citra copyCitra1.
print('n1 : ',n1)# dimensi citra copyCitra1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)#mencetak juga dimensi citra copyCitra2
print('Shape output citra 3 : ', output2.shape)#dimensi dari array output2.
print('m2 : ',m2)#Informasi ini berguna untuk memahami jumlah baris
print('n2 : ',n2)#mlah kolom (n) dari citra atau array.
print()

for baris in range(0, m1 - 1):# dilakukan iterasi melalui setiap elemen pada citra copyCitra1 menggunakan nested loop for
    for kolom in range(0, n1 - 1):
        a1 = baris#
        b1 = kolom# Untuk setiap elemen, diambil elemen tetangganya dengan memanfaatkan indeks a1 dan b1
        dataA = [copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1 - 1, b1 + 1], #elemen-elemen tersebut disimpan dalam list dataA
                 copyCitra1[a1, b1 - 1], copyCitra1[a1, b1], copyCitra1[a1, b1 + 1], \
                 copyCitra1[a1 + 1, b1 - 1], copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]]

        # Urutkan
        for i in range(1, 8):#ilakukan proses pengurutan elemen-elemen tersebut menggunakan nested loop for
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j] = tmpA;

        output1[a1, b1] = dataA[5]# Elemen yang terurut kemudian disimpan di output1 pada indeks yang sesuai.
for baris in range(0, m2 - 1):
    for kolom in range(0, n2 - 1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1 - 1, b1 + 1], \
                 copyCitra2[a1, b1 - 1], copyCitra2[a1, b1], copyCitra2[a1, b1 + 1], \
                 copyCitra2[a1 + 1, b1 - 1], copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j] = tmpA;

        output2[a1, b1] = dataA[5]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))#Kode di atas menghasilkan plot dengan menggunakan subplots dengan 2 baris dan 2 kolom.
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')#
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')#Citra pertama (citra1) ditampilkan pada ax[0]
ax[1].set_title("Input Citra 1")# citra kedua (citra2) ditampilkan pada ax[1]

ax[2].imshow(output1, cmap = 'gray')#
ax[2].set_title("Output Citra 1")#output1 ditampilkan pada ax[2]

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")#output2 ditampilkan pada ax[3]

plt.show()# Setiap subplot diberi judul sesuai dengan citra yang ditampilkan. Akhirnya, plot ditampilkan menggunakan plt.show()


