import user
import random
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import pyautogui

browser = webdriver.Chrome()

#browserı açmak
browser.get("https://twitter.com/login?lang=tr")

#kullanıcı adı ve şifre girilmesi
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'))).send_keys(user.user_name)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(user.password)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div'))).click()
time.sleep(120)
sayac = 1

haber_listesi = []

while True:
    try:
        r = requests.get("https://www.mynet.com/son-dakika-haberleri")
        r1 = requests.get("https://www.haberler.com/son-dakika/")
        
        soup = BeautifulSoup(r.content, "html.parser")
        soup1 = BeautifulSoup(r1.content, "html.parser")

        #mynet
        mynet = soup.find("div", {"class" : "row col-3 head-line"}).find("p").text.lstrip()
        
        
        #son dakika haberleri
        sdhaberleri = soup1.find("div", {"class":"hblnBox"}).find("div",{"class":"hblnContent"}).find("p").text
       
       
        for i in [mynet , sdhaberleri]:
            if len(i) <60 or len(i)>280:
                continue
            else:
                #time.sleep(120)
                if i not in haber_listesi:
                #twitt atmak
                    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'))).send_keys(i.strip() + "\n#SonDakika ".lstrip())
                    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span').click()
                    print(f"{sayac} haber paylaşıldı ", datetime.datetime.now())
                    sayac += 1
                    browser.refresh()
                    haber_listesi.append(i)
                else:
                    time.sleep(3)
                    continue
                
    except:
        print("Some error has been received. ")
        browser.refresh()
        continue