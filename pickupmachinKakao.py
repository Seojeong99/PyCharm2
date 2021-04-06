from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

def kakaofirst():
    URL1 = "https://translate.kakao.com/"
    driver.get(URL1)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/a/span').click()
    time.sleep(3)


def kakao(korean, English):
    # <Kakao tanslate 영어> == <original 영어>
    URL1 = "https://translate.kakao.com/"
    driver.get(URL1)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(korean)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('p', class_='desc_translation').text
    print('<original 한글> ' + korean + ' <kakao tanslate 외국어> ' + str(result) + ' <kakao 외국어> ' + English)
    print('<kakao translate 외국어>==<original 외국어>?')
    if result == English:
        print("O")
    else:
        print("X")

    #<kakao tanslate 한글> == <original 한글>

    URL2 = "https://translate.kakao.com/"
    driver.get(URL2)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(str(result))
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('p', class_='desc_translation').text
    print('<kakao translate 외국어> ' + str(result) + ' <kakao tanslate 한글> ' + str(googlekorea) + ' <original 한글> '+ korean)
    print('<kakao tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    #<kakao tanslate 한글> == <original 한글>

    URL3 = "https://translate.kakao.com/"
    driver.get(URL3)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(English)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('p', class_='desc_translation').text
    print('<original 외국어> ' + English + ' <kakao tanslate 한글> ' + str(googlekorea2) +' <original 한글> '+ korean)
    print('<kakao tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')

data_pd = pd.read_excel("D:\A.xls", header=None, index_col=None)
data_np = pd.DataFrame.to_numpy(data_pd)
print(data_pd)
print("카카오번역기")

kakaofirst()
for i in range(0, 11):
    try:
         data1 = data_np[i][2]
         data2 = data_np[i][3]
         kakao(data1, data2)
    except: 0
