import numpy as np
import cv2

def sembunyikan_pesan(img, pesan):
    array_gambar = np.array(img)
    tinggi, lebar, _ = array_gambar.shape
    pesan_biner = ''.join(format(ord(char), '08b') for char in pesan)
    pesan_biner = pesan_biner.ljust(tinggi * lebar * 3, '0')

    k = 0
    for i in range(tinggi):
        for j in range(lebar):
            for saluran in range(3):
                array_gambar[i, j, saluran] = (array_gambar[i, j, saluran] & 0b11111110) | int(pesan_biner[k])
                k += 1

    return array_gambar

if __name__ == '__main__':
    pesan = input('Masukkan Pesan Untuk Disembunyikan Ke gambar:')
    gambar = cv2.imread('cat.jpg')

    if gambar is None:
        print("Error: Tidak dapat membaca file gambar.")
    else:
        gambar_tersembunyi = sembunyikan_pesan(gambar, pesan)
        cv2.imwrite('x1.jpg', gambar_tersembunyi)
        print("Pesan telah berhasil disembunyikan.")
