import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from main import Jaccard_similarity

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)
def checksimilarity(keyword):
    URL3 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver.get(URL3)
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    #keyword = keyword.replace("\n", "")
    str1 = str("이건 " + keyword + "이다.")
    print(str1)
    #이건 이다.
    driver.find_element_by_css_selector('.er8xn').send_keys(str1)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result1 = soup.find('div', class_='NqnNQd').text

    URL4 = "https://translate.google.com/?sl=en&tl=ko&op=translate"
    driver.get(URL4)
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').send_keys(result1)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result2 = soup.find('div', class_='NqnNQd').text
    #print('<original>' + str1 + '<original tr>' + str(result1) + '<final tr>' + str(result2))
    #similarity = Jaccard_similarity(str1, str(result2))
    print(Jaccard_similarity(str1, str(result2)))
    #if similarity < 0.8 :

     #count1 = count1 + Jaccard_similarity(str1, str(result2))


def original:
with open("input5.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:

                checksimilarity(data)
            except:
                0

with open("input5.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                checksimilarity(data)
            except: 0

#print(round(count1 / 400, 4))
#count1 = 0

#with open("inputfinal.txt", "r", encoding="UTF-8") as f:
#    list = f.readlines()
#    for i, data in enumerate(list):
#            try:
#                checksimilarity(data)
#            except: 0

#print(round(count1 / 400, 4))