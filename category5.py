import re
import sentence
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from main import Jaccard_similarity

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)


def checksimilarity(akeyword):
        global count1
        URL3 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
        driver.get(URL3)
        time.sleep(4)
        driver.find_element_by_css_selector('.er8xn').clear()
        time.sleep(4)
        keyword = keyword.replace("\n", "")
        str1 = sentence.letcut(keyword)
        driver.find_element_by_css_selector('.er8xn').send_keys(str1)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        result1 = soup.find('div', class_='NqnNQd').text

        URL4 = "https://translate.google.com/?sl=en&tl=ko&op=translate"
        driver.get(URL4)
        time.sleep(4)
        driver.find_element_by_css_selector('.er8xn').clear()
        time.sleep(4)
        driver.find_element_by_css_selector('.er8xn').send_keys(result1)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        result2 = soup.find('div', class_='NqnNQd').text
        x = Jaccard_similarity(str1, str(result2))
        ififsimilarityis(x,keyword)
        print(x)

def getMeaningOfNewlyCoinedWord(keyword):
    print("1")
    time.sleep(3)
    URL2 = "https://dict.naver.com/"
    driver.get(URL2)
    time.sleep(4)
    key2 = driver.find_element_by_xpath('//*[@id="ac_input"]')
    key2.send_keys(keyword)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/a').click()
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    try:
        result = soup.select('li > p')[1].text
        print('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + purePhrase(result) + '</Meaning>')
        #st1 = str('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + purePhrase(result) + '</Meaning>')
        #return st1
    except:
        print('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + 'None' + '</Meaning>')
        #str2 = str('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + 'None' + '</Meaning>')
        #return str2
    time.sleep(3)

def purePhrase(data):
    retValue = ""
    start = 0
    origin = 0
    if "]" in str(data):
        origin = str(data).index("]") + 1
    for i in range(origin, len(str(data)) - 1):
        if str(data[i:i+1]).isspace() == False:
            start = i
            break
    retValue = str(data[start:])
    if "." in retValue:
        retValue = retValue[:retValue.index(".")]

    return retValue


def ififsimilarityis(s,keyword):
        if s > 0.5:
                getMeaningOfNewlyCoinedWord(keyword)

        else:
                print(0)



with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                checksimilarity(data)
            except: 0