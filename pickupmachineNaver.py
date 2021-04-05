from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

def naver(korean, English):
    # <papago tanslate 영어> == <original 영어>
    URL1 = "https://papago.naver.com/"
    driver.get(URL1)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(korean)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<original 한글> ' + korean + ' <papago tanslate 영어> ' + str(result) + ' <original 영어> ' + English)
    print('<papago translate 영어>==<original 영어>?')
    if result == English:
        print("O")
    else:
        print("X")

        # <google tanslate 한글> == <original 한글>

    URL2 = "https://papago.naver.com/"
    driver.get(URL2)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(str(result))
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<papago translate 영어> ' + str(result) + ' <papago tanslate 한글> ' + str(
        googlekorea) + ' <original 한글> ' + korean)
    print('<papago tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    # <papago tanslate 한글> == <original 한글>

    URL3 = "https://papago.naver.com/"
    driver.get(URL3)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(English)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<original 영어> ' + English + ' <papago tanslate 한글> ' + str(googlekorea2) + ' <original 한글> ' + korean)
    print('<papago tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')

data_pd = pd.read_excel("D:\A.xls", header=None, index_col=None)
data_np = pd.DataFrame.to_numpy(data_pd)
print(data_pd)
print("파파고")

for i in range(0, 11):
    try:
         data1 = data_np[i][2]
         data2 = data_np[i][3]
         naver(data1, data2)
    except: 0
