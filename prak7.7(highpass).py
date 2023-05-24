# Highpass Filter

# sebenarnya kita tidak perlu melakukan filtering lagi. Cukup sekali saja
# di bagian awal, selama notebook ini tetap terhubung
import cv2
import numpy as np
from matplotlib import pyplot as plt


# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('aadc.jpeg',0)

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (10,10)


# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')#Baris ini menentukan subplot pertama dalam grid 2x2. Fungsi plt.subplot() digunakan untuk membuat subplot dengan parameter (jumlah baris, jumlah kolom, nomor subplot).
plt.title('Original'), plt.xticks([]), plt.yticks([])#plt.title('Original'), plt.xticks([]), plt.yticks([]): Baris ini menambahkan judul 'Original' pada subplot pertama menggunakan fungsi plt.title(). Fungsi plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan tanda sumbu (ticks) pada subplot pertama.
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')#ungsi plt.imshow() digunakan untuk menampilkan gambar laplacian (hasil Laplacian filtering) dalam subplot tersebut dengan colormap 'gray'.
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])#Fungsi plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan tanda sumbu (ticks) pada subplot kedua.
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')#Fungsi plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan tanda sumbu (ticks) pada subplot kedua.
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])#Baris ini menentukan subplot ketiga dalam grid 2x2. Fungsi plt.subplot() digunakan untuk membuat subplot dengan parameter (jumlah baris, jumlah kolom, nomor subplot).
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')#Baris ini menambahkan judul 'Sobel X' pada subplot ketiga menggunakan fungsi plt.title()
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])#Baris ini menentukan subplot keempat dalam grid 2x2. Fungsi plt.subplot() digunakan untuk membuat subplot dengan parameter (jumlah baris, jumlah kolom, nomor subplot).
plt.show()

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('aadc.jpeg',0)

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,50,100)

plt.subplot(121),plt.imshow(img,cmap = 'gray')#Baris ini menentukan subplot pertama dalam grid 1x2. Fungsi plt.subplot() digunakan untuk membuat subplot dengan parameter (jumlah baris, jumlah kolom, nomor subplot).
plt.title('Original Image'), plt.xticks([]), plt.yticks([])#Baris ini menambahkan judul 'Original Image' pada subplot pertama menggunakan fungsi plt.title(). Fungsi plt.xticks([]) dan plt.yticks([]) digunakan untuk menghilangkan tanda sumbu (ticks) pada subplot pertama.
plt.subplot(122),plt.imshow(edges,cmap = 'gray')# Baris ini menentukan subplot kedua dalam grid 1x2. Fungsi plt.subplot() digunakan untuk membuat subplot dengan parameter (jumlah baris, jumlah kolom, nomor subplot).
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#plt.title('Edge Image'), plt.xticks([]), plt.yticks([]): Baris ini menambahkan judul 'Edge Image' pada subplot kedua menggunakan fungsi plt.title().

plt.show()
# membaca gambar baymax
img = cv2.imread('aadc.jpeg',0)

# Hitungan threshold.
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#Baris ini menggunakan fungsi cv2.threshold() untuk menerapkan binary thresholding pada citra img
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#mirip dengan baris sebelumnya, tetapi kali ini diterapkan binary inverse thresholding. Piksel dengan intensitas di atas ambang batas diatur menjadi 0 (hitam), sedangkan piksel dengan intensitas di bawah ambang batas diatur menjadi 255 (putih)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#Baris ini menerapkan truncation thresholding pada citra img. Piksel dengan intensitas di atas ambang batas diatur menjadi ambang batas itu sendiri (127 dalam hal ini), sedangkan piksel dengan intensitas di bawah ambang batas tidak mengalami perubahan.
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#Baris ini menerapkan thresholding to zero pada citra img. Piksel dengan intensitas di bawah ambang batas diatur menjadi 0 (hitam), sedangkan piksel dengan intensitas di atas atau sama dengan ambang batas tidak mengalami perubahan.
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#: Baris ini mirip dengan baris sebelumnya, tetapi kali ini diterapkan thresholding to zero inverse.

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# menampilkan beberapa gambar sekaligus
for i in range(6):
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# masih menggunakan variabel img yang sama
#img = cv2.imread('images/baymax.jpg',0)

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

# menampilkan hasil
for i in range(4):#Melakukan iterasi sebanyak 4 kali, karena terdapat 4 gambar yang akan ditampilkan.
    plt.subplot(2,2,i+1)#Membuat subplot dengan grid 2x2 (2 baris, 2 kolom) dan mengatur posisi subplot yang akan digunakan pada iterasi saat ini.
    plt.imshow(images[i],'gray')#nampilkan gambar dengan menggunakan fungsi imshow().
    plt.title(titles[i])#Memberikan judul pada subplot berdasarkan judul yang ada pada indeks i dari daftar titles.
    plt.xticks([]),plt.yticks([])#Menghilangkan label sumbu x dan y pada subplot.
plt.show()