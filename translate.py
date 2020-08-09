import requests
import time

cevirilecek = input('Çevirmek istediğiniz Kelime/Cümle: ')

data1= {"detect_new_text":0,
       "rtk_priv":"none",
       "rtk_p":"%7B%7D",
       "_gat_gtag_UA_3411294_31":1,
       "text_to_translate":cevirilecek}

abc = requests.post("https://www.translate.com/translator/ajax_lang_auto_detect",data=data1).json()

lang = abc["language"]

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
