import numpy as np
import cv2
import base64

def ungkap_pesan(img):
    array_gambar = np.array(img)
    tinggi, lebar, _ = array_gambar.shape
    pesan_biner = ''

    for i in range(tinggi):
        for j in range(lebar):
            for saluran in range(3):
                pesan_biner += str(array_gambar[i, j, saluran] & 1)

    byte_pesan = [int(pesan_biner[i:i+8], 2) for i in range(0, len(pesan_biner), 8)]
    pesan_terungkap = base64.b64encode(bytes(byte_pesan)).decode('utf-8')
    return pesan_terungkap

if __name__ == '__main__':
    gambar_tersembunyi = cv2.imread('x1.jpg')

    if gambar_tersembunyi is None:
        print("Error: Tidak dapat membaca file gambar.")
    else:
        pesan_terungkap = ungkap_pesan(gambar_tersembunyi)
        print("Pesan yang disembunyikan:", pesan_terungkap)
