import requests
import time

cevirilecek = input('Çevirmek istediğiniz Kelime/Cümle: ')


url = "https://www.translate.com/translator/ajax_translate"

if lang == "tr":
    cevir = requests.post(url,data={"text_to_translate":cevirilecek,"source_lang":lang,"translated_lang":"en"})

else:
    cevir = requests.post(url,data={"text_to_translate":cevirilecek,"source_lang":lang,"translated_lang":"tr"})

cek = cevir.json()

if cek["result"] == "success":
    print(cek["translated_text"])

elif cek["result"] == "error":
    print("Üzgünüm çeviremedim ")

else:
    pass