
def aramayap(aratilacak):
    import webbrowser
    url = "https://www.google.com/search?q="+aratilacak
    webbrowser.get().open(url)

def doviz(kur):
    import requests
    from bs4 import BeautifulSoup


    r = requests.get('https://dolar.tlkur.com/')

    soup = BeautifulSoup(r.content,'html.parser')

    data = soup.find('td',{'valign':'top'})
    veriler = data.find('div',{'class':'data-charts'})
    yeni = veriler.find('table',{'class':'data-file'})
    cek = yeni.find_all('tr')
    metin = list()
    gond = ""
    for i in cek:
        a = i.find_all('td')
        for x in a:
            metin.append(x)
    dolar = metin[1].text+" "+metin[2].text   # Dolar
    euro =metin[7].text+" "+metin[8].text   # Euro
    pound = metin[13].text+" "+metin[14].text # Pound
    btc = metin[19].text+" "+metin[20].text # Bitcoin
    ruble = metin[61].text+" "+metin[62].text # Ruble
    dirhem = metin[73].text+" "+metin[74].text # Dirhem
    etc = metin[91].text+" "+metin[92].text # Ethereum
    if "dolar" in kur:
        print(dolar)
    elif "euro" in kur:
        print(euro)
    elif "sterlin"or"pound" in kur:
        print(pound)
    elif "bitcoin"or"btc" in kur:
        print(btc)
    elif "ruble" in kur:
        print(ruble)
    elif "dirhem" in kur:
        print(dirhem)
    elif "etc"or"ether"or'ethereum'or'etherium' in kur:
        print(etc)
    
def sohbet(isim):
    merhaba_text = input(f"Merhaba {isim} nasılsın ?\n>>> ")
    if 'iyi'or'iyiyim' in merhaba_text:
        print(f'İyi olmana sevindim.Hayat nasıl gidiyor{isim} ? ')
        merhaba1_text = input(" ")
        if 'iyi' in merhaba1_text:
            print("Pekala görüşürüz.")