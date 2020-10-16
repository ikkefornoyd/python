from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import platform
import sys
import random
import time
import urllib
import urllib.request as req

a = str(random.randint(70,100))
b = str(random.randint(40,70))
c = str(random.randint(0,40))
adsoyad = "Selim"+"Yilmaz{0}{1}{2}".format(a,b,c)
kullanici = adsoyad+a
mail = input("Mail Adresi veya Telefon Numarası: ")
parola = "ICE777v01"
print("""Password(Sifre) otomatik olarak tanimlanmistir.
Password(Sifre): ICE777v01
""")
time.sleep(2)

renk = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
platform = platform.system()
if platform == "Windows":
    chromedriver = "/chromedriver.exe"
    try:
        os.system("pip install selenium")
        os.system("pip install beautifulsoup4")
    except:
        print(renk +"Selenium ve beautifulsoup4 kurulamadi\nEger beklersen kurabilirim")
chromedriver1 = os.getcwd()+chromedriver
class Date():
    def __init__(self,ay,gun,yil,indirme):
            self.ay = ay
            self.gun = gun
            self.yil = yil
            self.indirme

class Instagram(Date):
    def __init__(self,kullanici,parola,mail,adsoyad):
        self.adsoyad = adsoyad
        self.kullanici = kullanici
        self.mail = mail
        self.parola = parola
        self.browser = webdriver.Chrome()


    def signUp(self):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(2)
        action = webdriver.ActionChains(self.browser)
        usernameinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input") 
        parolainput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")
        mailinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        adsoyadinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input")

        mailinput.send_keys(self.mail)
        time.sleep(1)
        adsoyadinput.send_keys(self.adsoyad)
        time.sleep(1)
        usernameinput.send_keys(self.username)
        time.sleep(1)
        parolainput.send_keys(self.parola)
        time.sleep(1)
        parolainput.send_keys(Keys.ENTER)
        time.sleep(2.75)

    def button(self):
        self.ay = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select")
        time.sleep(1)
        self.ay.click()
        time.sleep(1)
        self.ay.send_keys(Keys.ENTER)
        self.gun = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select")
        self.gun.click()
        self.gun.send_keys(Keys.ENTER)
        time.sleep(2)
        self.yil = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")
        self.yil.click()
        time.sleep(2)
        action = webdriver.ActionChains(self.browser)
        a = 0
        while a<14:
            action.key_down(Keys.ARROW_DOWN).perform()
            a +=1
        self.yil.send_keys(Keys.ENTER)
        buton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[5]/div[2]/button")
        buton.click()
        time.sleep(10)


    def down(self,indirme,api="https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"):
        if not api:
            print("\t\tGörünüşe göre api kısmını boş bırakmışsın . Orjinal api ile devam ediliyor!")
            api="https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
        if not indirme:
            print("\t\tApi kaynağından güncel liste indiriliyor")
            try:
                req.urlretrieve(api,"proxy.txt")
            except:
                print("\n\t\tProxy listesi indirilirken hata ile karşılaşıldı . Tekrar deneniyor")
                time.sleep(3)
                try:
                    req.urlretrieve(api,"proxy.txt")
                except:print("\n\t\tProxy listesi indirilirken hata ile karşılaşıldı !")
    def proxy(self):
        while True:
            try:
                with open("proxy.txt") as liste:
                    liste = liste.read().split("\n")
                    liste = random.choice(liste)
                    if not liste:
                        print("\t\tProxy boş geldi . Yeniden deneniyor !")
                    else:
                        break
            except:
                try:
                    time.sleep(3)
                    with open("proxy.txt") as liste:
                        liste = liste.read().split("\n")
                        liste = random.choice(liste)
                        if not liste:
                            print("\t\tProxy boş geldi . Yeniden deneniyor !")
                        else:
                            break
                except:print("\n\t\tProxy.txt bulunamadı . Api kaynağından indiriliyor !");basla.down(self,self.indirme,self.api) 
        agents = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
        agent = random.choice(agents)
        print("""\t\t\033[36m-\033[0mProxy : {} User-Agent : {}\033[36m-\033[0m""".format(liste,agent[13:35]))

        basla.down()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument('--proxy-server={}'.format(liste))
        chrome_options.add_argument("--user-agent={}".format(agent))
        chrome_options.add_argument("--headless")
        if platform == "Windows":
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)


basla = Instagram(kullanici,parola,mail,adsoyad)
basla.proxy()
basla.signUp()
basla.button()
with open("account.txt","a",encoding="utf-8") as file:
    file.write(kullanici+":"+parola+"\n")

if os.path.exists("account.txt"):
    pass
else:
    with open("account.txt","a",encoding="utf-8") as file:
        file.write(kullanici+":"+parola+"\n")
