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
    URL1 = "https://translate.google.com/?sl=ko&tl=es&op=translate"
    driver.get(URL1)
    time.sleep(4)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(4)
    driver.find_element_by_css_selector('.er8xn').send_keys(korean)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_='NqnNQd').text
    print('<original 한글> ' + korean + ' <google tanslate 외국어> ' + str(result) + ' <original 외국어> ' + English)
    print('<google translate 외국어>==<original 외국어>?')
    if result == English:
        print("O")
    else:
        print("X")

    # <google tanslate 한글> == <original 한글>

    URL2 = "https://translate.google.com/?sl=es&tl=ko&op=translate"
    driver.get(URL2)
    time.sleep(4)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(4)
    driver.find_element_by_css_selector('.er8xn').send_keys(str(result))
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('div', class_='NqnNQd').text
    print('<google translate 외국어> ' + str(result) + ' <google tanslate 한글> ' + str(
        googlekorea) + ' <original 한글> ' + korean)
    print('<google tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    # <google tanslate 한글> == <original 한글>

    URL3 = "https://translate.google.com/?sl=es&tl=ko&op=translate"
    driver.get(URL3)
    time.sleep(4)

    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(4)
    driver.find_element_by_css_selector('.er8xn').send_keys(English)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('div', class_='NqnNQd').text
    print('<original 외국어> ' + English + ' <google tanslate 한글> ' + str(googlekorea2) + ' <original 한글> ' + korean)
    print('<google tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')


def naver(korean, English):
    # <papago tanslate 영어> == <original 영어>
    URL1 = "https://papago.naver.com/?sk=ko&tk=es"
    driver.get(URL1)
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(korean)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<original 한글> ' + korean + ' <papago tanslate 외국어> ' + str(result) + ' <original 외국어> ' + English)
    print('<papago translate 외국어>==<original 외국어>?')
    if result == English:
        print("O")
    else:
        print("X")

        # <google tanslate 한글> == <original 한글>
    time.sleep(3)
    URL2 = "https://papago.naver.com/?sk=es&tk=ko"
    driver.get(URL2)
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(str(result))
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<papago translate 외국어> ' + str(result) + ' <papago tanslate 한글> ' + str(
        googlekorea) + ' <original 한글> ' + korean)
    print('<papago tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    # <papago tanslate 한글> == <original 한글>

    URL3 = "https://papago.naver.com/?sk=es&tk=ko"
    driver.get(URL3)
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="txtSource"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(English)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('div', class_='edit_box___1KtZ3 active___3VPGL').text
    print('<original 외국어> ' + English + ' <papago tanslate 한글> ' + str(googlekorea2) + ' <original 한글> ' + korean)
    print('<papago tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')


def kakao(korean, English):
    # <Kakao tanslate 영어> == <original 영어>
    URL1 = "https://translate.kakao.com/"
    driver.get(URL1)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(korean)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/a').click()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[11]/a').click()
    time.sleep(6)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('p', class_='desc_translation').text
    print('<original 한글> ' + korean + ' <kakao tanslate 외국어> ' + str(result) + ' <original 외국어> ' + English)
    print('<kakao translate 외국어>==<original 외국어>?')
    if result == English:
        print("O")
    else:
        print("X")

    # <kakao tanslate 한글> == <original 한글>

    URL2 = "https://translate.kakao.com/"
    driver.get(URL2)
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/a").click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/ul/li[12]/a").click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(str(result))
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/a').click()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/ul/li[1]/a').click()
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea = soup.find('p', class_='desc_translation').text
    print('<kakao translate 외국어> ' + str(result) + ' <kakao tanslate 한글> ' + str(
        googlekorea) + ' <original 한글> ' + korean)
    print('<kakao tanslate 한글>==<original 한글>?')
    if korean == str(googlekorea):
        print("O")
    else:
        print("X")

    # <kakao tanslate 한글> == <original 한글>

    URL3 = "https://translate.kakao.com/"
    driver.get(URL3)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(English)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    googlekorea2 = soup.find('p', class_='desc_translation').text
    print('<original 외국어> ' + English + ' <kakao tanslate 한글> ' + str(googlekorea2) + ' <original 한글> ' + korean)
    print('<kakao tanslate 한글>==<original 한글>?')
    if str(googlekorea2) == korean:
        print("O")
    else:
        print("X")

    print('--------------------------------')

def kakaofirst():
    URL1 = "https://translate.kakao.com/"
    driver.get(URL1)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/a/span').click()
    time.sleep(4)

data_pd = pd.read_excel("D:\Sp.xls", header=None, index_col=None, sheet_name='Sheet1')
data_np = pd.DataFrame.to_numpy(data_pd)
#print("~~~~~~~~~지명~~~~~~~~~")
#print("구글 번역기")
#for i in range(303, 710):
#    try:
#        data1 = data_np[i][2]
#        data2 = data_np[i][3]
#        google(data1, data2)
#    except:
#        0

#print("papago 번역기")
#for j in range(636, 710):
#    try:
#        data1 = data_np[j][2]
#        data2 = data_np[j][3]
#        naver(data1, data2)
#    except:
#        0

print("kakao 번역기")
kakaofirst()
for k in range(69, 710):
    try:
        data1 = data_np[k][2]
        data2 = data_np[k][3]
        kakao(data1, data2)
    except:
        0
data_pd = pd.read_excel("D:\Sp.xls", header=None, index_col=None, sheet_name='Sheet2')
data_np = pd.DataFrame.to_numpy(data_pd)
print("~~~~~~~~~일반용어~~~~~~~~~")
print("구글 번역기")
for i in range(1, 100):
    try:
        data1 = data_np[i][2]
        data2 = data_np[i][3]
        google(data1, data2)
    except:
        0

#print("papago 번역기")
#for j in range(1, 100):
#    try:
#        data1 = data_np[j][2]
#        data2 = data_np[j][3]
#        naver(data1, data2)
#    except:
#        0

#print("kakao 번역기")
#kakaofirst()
#for k in range(1, 100):
#    try:
#        data1 = data_np[k][2]
#        data2 = data_np[k][3]
#        kakao(data1, data2)
#    except:
#        0