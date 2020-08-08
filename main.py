import requests



url = "https://www.translate.com/translator/ajax_translate"

a = requests.post(url,data={"text_to_translate":"Merhaba arkadaşlar benim adım serkan"})
cek = a.json()
print(cek["translated_text"])