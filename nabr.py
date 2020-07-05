import giris
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

browser = webdriver.Chrome("/Users/AveC/Desktop/python/chromedriver")

#browserı açmak
browser.get("https://twitter.com/login?lang=tr")

#kullanıcı adı ve şifre girilmesi
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'))).send_keys(giris.user_name)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(giris.password)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span'))).click()

sayac = 1


while True:
    try:
        r = requests.get("https://www.mynet.com/son-dakika-haberleri")

        soup = BeautifulSoup(r.content, "html.parser")

        mynet = soup.find("div", {"class" : "row col-3 head-line"}).find("p").text.lstrip()
        
        #twitt atmak
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'))).send_keys(mynet + " #SONDAKİKA ".lstrip())
        browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span').click()
        print(f"{sayac} haber paylaşıldı ", datetime.datetime.now())
        sayac += 1
        
        time.sleep(random.randint(240,300))
        browser.refresh()
    except:
        print("Some error has been received. ")
        browser.refresh()
        continue