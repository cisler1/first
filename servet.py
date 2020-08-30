import requests
from bs4 import BeautifulSoup
import time

sonuc = 0

while True:

    r = requests.get("http://www.altinkaynak.com/Altin/Kur/Guncel")

    soup = BeautifulSoup(r.content, "html.parser")

    gram_altin = soup.find("td",{"id":"tdGABuy"}).text[0:8]

    ata_altin = soup.find("td",{"id":"tdABuy"}).text[0:8]

    tam_altin = soup.find("td",{"id":"tdTBuy"}).text[0:8]

    yarim_altin = soup.find("td",{"id":"tdYBuy"}).text[0:8]

    ceyrek_altin = soup.find("td",{"id":"tdCBuy"}).text[0:8]

    yirmiiki_ayar = soup.find("td",{"id":"tdBBuy"}).text[0:8]

    liste = [gram_altin, ceyrek_altin, yarim_altin, tam_altin, ata_altin, yirmiiki_ayar,yirmiiki_ayar, yirmiiki_ayar]

    liste2 = ["Gram Altın", "Çeyrek Altın", "Yarım Altın", "Tam Altın", "Ata Altın", "22 Ayar Bilezik","İnce Bilezik","Kalın Bilezik"]

    liste3 = [3,21,6,1,2,75, 40, 5]

    for i in range(8):
        print(liste2[i],":",liste[i])
        toplam = float(liste[i])*float(liste3[i])
        sonuc = sonuc + toplam
        
    print("TOPLAM: ", sonuc)
    print("-----------------------")
    time.sleep(5)
    sonuc = 0
