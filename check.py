from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

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
        result = re.sub(r"\s+|\s+$", "", result)
        resultout = outspace(result)

        if '\'' in resultout:
            resultf = resultout.split("\'")
            print('<Original>' + keyword + '<Meaning>' + resultf[1])

        elif "\"" in resultout:
            resultf = resultout.split("\"")
            print('<Original>' + keyword + '<Meaning>' + resultf[1])
        elif "‘" in resultout:
            resultf = resultout.split("‘")
            resultf2 = resultf[1].split("’")
            print('<Original>' + keyword + '<Meaning>' + resultf2[0])
        elif "또는" in resultout:
            resultf = resultout.split("또는")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "1." in resultout:
            resultf = resultout.split("1.")
            resultf2 = resultf[1].split("2.")
            print('<Original>' + keyword + '<Meaning>' + resultf2[0])
        elif "비유적" in resultout:
            if ("을") in resultout:
                resultf = resultout.split("을비유적")
                print('<Original>' + keyword + '<Meaning>' + resultf[0])
            else:
                resultf = resultout.split("를비유적")
                print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "뜻으로" in resultout:
            resultf = resultout.split("는뜻으로")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "줄임말" in resultout:
            resultf = resultout.split("의줄임말")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])
        else:
            if "⇒" in resultout:
                resultf = resultout.split("⇒")
                print('<Original>' + keyword + '<Meaning>' + resultf[0])
            else:
                print('<Original>' + keyword + '<Meaning>' + resultout)

    except:
        print('<Original>' + keyword + '</Original><Meaning>' + 'None' + '</Meaning>')



def outspace(resultinput):
    if "[" in resultinput:
        key1 = resultinput.split("[")
        key2 = key1[1].split("]")
        return key2[1]
    else:
        return resultinput

with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                getMeaningOfNewlyCoinedWord(data)
            except: 0



