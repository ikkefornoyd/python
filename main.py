# -*- coding:utf-8 -*-
import os
import time
import random
import sys
import requests
import webbrowser
from fonksiyonlar import *
secim = int(input(f"""
        \033[31mKodlet Asistan\033[0m | \033[33m0.0.1\033[0m

    1)Başla
    2)Yardım
    3)Emeği Geçenler
    4)Çıkış


>>> """))
if secim == 1:
    hitap = input("Sana nasıl hitap etmeliyim ?")
    # kural = {}

    girdi = input(f"""\033[31m{hitap}\033[0m neler yapmak istiyorsun ?

    Sana Hava Durumunu söyleyebilirim.   => havadurumu
    Sana Para Birimlerini getirebilirim. => döviz
    Senin için bir şeyler arayabilirim.  => ara
    Seninle sohbet edebilirim.           => sohbet
    >>>""")

    if "hava"and"durumu" in girdi:
        print("Hava 19 derece Clear")

    elif "ara"or'arama'or'arama yap' in girdi:
        arama_girdi = input("Ne aramak istediniz ? ")
        aramayap(arama_girdi)

    elif 'döviz'or'doviz' in girdi:
        p_b = input("Para Birimi: ")
        doviz(p_b)

    elif 'sohbet' in girdi:
        sohbet(hitap)



    if secim == "4":
        sys.exit("Asistan kapatılıyor...")

if secim == 3:
    print("Emeği geçenler:\n\n\033[31m@raifpy\033[0m")

if secim == 4:
    sys.exit('Asistan Kapatılıyor...')
    time.sleep(1.55)
