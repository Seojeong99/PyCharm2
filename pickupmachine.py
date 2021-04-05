from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

def google(korean, English):
    # <google tanslate 영어> == <original 영어>
    URL1 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver.get(URL1)
    time.sleep(3)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').send_keys(korean)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_='NqnNQd').text
    print('<original 한글> ' + korean + ' <google tanslate 영어> ' + str(result) + ' <original 영어> ' + English)
    print('<google translate 영어>==<original 영어>?')
    if result == English:
        print("O")
    else:
        print("X")

    #<google tanslate 한글> == <original 한글>

    URL2 = "https://translate.google.com/?sl=en&tl=ko&op=translate"
    driver.get(URL2)
    time.sleep(3)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').send_keys(str(result))
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('div', class_='NqnNQd').text
    print('<google translate 영어> ' + str(result) + ' <google tanslate 한글> ' + str(googlekorea) + ' <original 한글> '+ korean)
    print('<google tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    #<google tanslate 한글> == <original 한글>

    URL3 = "https://translate.google.com/?sl=en&tl=ko&op=translate"
    driver.get(URL3)
    time.sleep(3)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(3)
    driver.find_element_by_css_selector('.er8xn').send_keys(English)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('div', class_='NqnNQd').text
    print('<original 영어> ' + English + ' <google tanslate 한글> ' + str(googlekorea2) +' <original 한글> '+ korean)
    print('<google tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')

data_pd = pd.read_excel("D:\A.xls", header=None, index_col=None)
data_np = pd.DataFrame.to_numpy(data_pd)
print(data_pd)
print("구글 번역기")

for i in range(0, 11):
    try:
         data1 = data_np[i][2]
         data2 = data_np[i][3]
         google(data1, data2)
    except: 0
