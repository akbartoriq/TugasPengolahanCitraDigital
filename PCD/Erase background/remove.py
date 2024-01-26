from rembg import remove
from PIL import Image
img = Image.open("C:\\Users\\UP\\Desktop\\bg hapus\\desktop-wallpaper-pin-oleh-aury-otaku-di-doraemon-dengan-gambar-doraemon-kartun-yellow-doraemon.jpg")
R = remove (img)
R.save("img1.png")