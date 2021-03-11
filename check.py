from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
def getMeaningOfNewlyCoinedWord(keyword):
    global count1
    global count2
    global count3
    global count4
    global count5
    global count6
    global count7
    global count8
    global count9
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
            count1 = count1+1
            resultf = resultout.split("\'")
            print('<Original>' + keyword + '<Meaning>' + resultf[1])

        elif "\"" in resultout:
            count2 = count2+1
            resultf = resultout.split("\"")
            print('<Original>' + keyword + '<Meaning>' + resultf[1])
        elif "‘" in resultout:
            count3 = count3 + 1
            resultf = resultout.split("‘")
            resultf2 = resultf[1].split("’")
            print('<Original>' + keyword + '<Meaning>' + resultf2[0])
        elif "또는" in resultout:
            count4 = count4 + 1
            resultf = resultout.split("또는")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "1." in resultout:
            count5 = count5 + 1
            resultf = resultout.split("1.")
            resultf2 = resultf[1].split("2.")
            print('<Original>' + keyword + '<Meaning>' + resultf2[0])
        elif "비유적" in resultout:
            count6 = count6 + 1
            if ("을") in resultout:
                resultf = resultout.split("을비유적")
                print('<Original>' + keyword + '<Meaning>' + resultf[0])
            else:
                resultf = resultout.split("를비유적")
                print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "뜻으로" in resultout:
            count7 = count7 + 1
            resultf = resultout.split("는뜻으로")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])
        elif "줄임말" in resultout:
            count8 = count8 + 1
            resultf = resultout.split("의줄임말")
            print('<Original>' + keyword + '<Meaning>' + resultf[0])

        else:
            count9 = count9 + 1
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


print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)



