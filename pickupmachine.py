from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

def googlenumber(keyword):
    URL = "https://www.google.com/"
    driver.get(URL)
    time.sleep(3)
    key = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    key.send_keys(keyword)
    time.sleep(3)
    key.send_keys(Keys.RETURN)


    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', {'id':'result-stats'}).text
    temp = str(result)
    temp = temp[temp.index("약 ")+2:temp.index("개")]
    temp = temp.replace(",", "")
    print(keyword + '의 총 검색어수는' + temp + '입니다.')

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

def getMeaningOfNewlyCoinedWord(keyword):
    URL2 = "https://dict.naver.com/"
    driver.get(URL2)
    time.sleep(3)
    key2 = driver.find_element_by_xpath('//*[@id="ac_input"]')
    key2.send_keys(keyword)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/a').click()
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    try:
        result = soup.select('li > p')[1].text
        print('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + purePhrase(result) + '</Meaning>')
    except:
        print('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + 'None' + '</Meaning>')
    time.sleep(3)

   # URL3 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
   # driver.get(URL3)
   # time.sleep(3)

    #driver.find_element_by_css_selector('.er8xn').clear()
    #time.sleep(3)
    #driver.find_element_by_css_selector('.er8xn').send_keys(result)
    #time.sleep(10)
    #soup = BeautifulSoup(driver.page_source, "html.parser")
    #transresult = soup.find('div', class_='NqnNQd').text
    #print('<Original>' + keyword.replace("\n", "") + '</Original><Final translated>' + str(transresult) + '</Final translated>')



def originalTranslatedResult(keyword):
    URL3 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver.get(URL3)
    time.sleep(3)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').send_keys(keyword)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_='NqnNQd').text
    print('<Original>' + keyword.replace("\n", "") + '</Original><Translated>' + str(result) + '</Translated>')


#with open("input.txt", "r", encoding="UTF-8") as f:
#    list = f.readlines()
#    for i, data in enumerate(list):
#            try:
                #originalTranslatedResult(data)
#                getMeaningOfNewlyCoinedWord(data)
#            except: 0

#    for i, data in enumerate(list):
#        try:
#            print('')
            #googlenumber(data)
#        except: 0

with open("inputfinalplease.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                #originalTranslatedResult(data)
                getMeaningOfNewlyCoinedWord(data)
            except: 0

    for i, data in enumerate(list):
        try:
            googlenumber(data)
        except: 0


