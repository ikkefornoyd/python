

import time
import random
import platform
import os
import requests
from bs4 import BeautifulSoup


platform = platform.system()
questionTitle_list = list()
questionList = list()
acceptedAnswer = dict()
suggestedAnswer = dict()

# renk = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
renk = random.choice(["\033[35m"])

def yazdir():
    if platform == "Windows":
        os.system("cls")
        time.sleep(1)
    else:
        os.system("clear")
    yaz = renk+"""
    ▄████████     ███        ▄████████  ▄████████    ▄█   ▄█▄  ▄██████▄   ▄█    █▄     ▄████████    ▄████████    ▄████████  ▄█        ▄██████▄   ▄█     █▄  
    ███    ███ ▀█████████▄   ███    ███ ███    ███   ███ ▄███▀ ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ ███       ███    ███ ███     ███ 
    ███    █▀     ▀███▀▀██   ███    ███ ███    █▀    ███▐██▀   ███    ███ ███    ███   ███    █▀    ███    ███   ███    █▀  ███       ███    ███ ███     ███ 
    ███            ███   ▀   ███    ███ ███         ▄█████▀    ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄     ███       ███    ███ ███     ███ 
    ▀███████████     ███     ▀███████████ ███        ▀▀█████▄    ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███       ███    ███ ███     ███ 
            ███     ███       ███    ███ ███    █▄    ███▐██▄   ███    ███ ███    ███   ███    █▄  ▀███████████   ███        ███       ███    ███ ███     ███ 
    ▄█    ███     ███       ███    ███ ███    ███   ███ ▀███▄ ███    ███ ███    ███   ███    ███   ███    ███   ███        ███▌    ▄ ███    ███ ███ ▄█▄ ███ 
    ▄████████▀     ▄████▀     ███    █▀  ████████▀    ███   ▀█▀  ▀██████▀   ▀██████▀    ██████████   ███    ███   ███        █████▄▄██  ▀██████▀   ▀███▀███▀  
                                                    ▀                                              ███    ███              ▀                               

                                            author: @ice777_0\n"""
    return yaz

def url_aldir(aranacak):
    url = "https://stackoverflow.com/search?q="+aranacak
    return url


def baglan(link):
    r = requests.get(link)
    return r
def getHtml(r):
    soup = BeautifulSoup(r.content,"html.parser")
    return soup

def getQuestions(soup):
    a = soup.find_all("div",{"class":"container"})
    for i in a:
        c = i.find_all("div",{"class":"question-summary search-result"})
        for x in c:
            questionAl = x.find("a")["href"]
            questionList.append(questionAl)
    return questionList


def answers(liste):
    urls = "https://stackoverflow.com"+liste
    re = requests.get(urls)
    soups = BeautifulSoup(re.content,"html.parser")
    cont = soups.find("div",{"class":"container"})
    contnt = cont.find_all("div",{"id":"answers"})
    for i in contnt:
        a = i.find_all("div",{"class":"answer accepted-answer"})
        if not a:
            a = i.find_all("div",{"class":"answer"})
            if len(a)>=5:
                for j in range(0,5):
                    al = a[j].find("div",{"class":"s-prose js-post-body"}).text
                    suggestedAnswer[str(j+1)] = str(al)
            else:
                for j in range(0,len(a)):
                    al = a[j].find('div',{"class":"s-prose js-post-body"}).text
                    suggestedAnswer[str(j+1)] = str(al)
            return suggestedAnswer


        else:
            a = i.find_all("div",{"class":"answer accepted-answer"})
            gonder = a[0].find("div",{"class":"s-prose js-post-body"}).text
            for j in range(1,16):
                acceptedAnswer[str(j)] = str(gonder)
    return acceptedAnswer

def title(soup):
    a = soup.find_all("div",{"class":"container"})
    for i in a:
        c = i.find_all("div",{"class":"question-summary search-result"})
        for x in c:
            questionTit = x.find("a").text
            questionTitle_list.append(questionTit)
    return questionTitle_list



def pepe(list1):
    print(list1)
    print("\n\n")
    # print("\n\n\n")
    # for i in range(1,len(list1)+1):
        # print(list1[str(i)]+"\n")
def secim_yaptir(alin1):
    metin = ""
    text_q = list()
    for j in alin1:
        alin2 = j.replace("\r\n","")
        try:
            while alin2.startswith(" "):
                alin2 = alin2[1:]
            text_q.append(alin2)
        except Exception:
            text_q.append(alin2)

    for i in range(len(text_q)):
        metin += f"{i+1}) {text_q[i]}\n"
    return metin

def translate(cevirilecek):
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
        return cek["translated_text"]
    elif cek["result"] == "error":
        return "Üzgünüm çeviremedim"

    else:
        pass
