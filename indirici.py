from __future__ import print_function
from cgi import print_form
from pytube import YouTube

link = input("İndirmek İstediğiniz Bağlantı Adresini Giriniz: ")

yt = YouTube(link) 
ys = yt.streams.get_highest_resolution()

print("Video indiriliyor.")
ys.download()
print("Video indirildi.")
