from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)


def getMeaningOfNewlyCoinedWord(keyword):
        keyword2 = cut(keyword)
        if '\'' in keyword2:
            resultf = keyword2.split("\'")
            #print('<Original>' + keyword + '<Meaning>' + resultf[1])
            print(resultf[1])

        elif "\"" in keyword2:
            resultf = keyword2.split("\"")
            #print('<Original>' + keyword + '<Meaning>' + resultf[1])
            print(resultf[1])
        elif "‘" in keyword2:
            resultf = keyword2.split("‘")
            resultf2 = resultf[1].split("’")
            #print('<Original>' + keyword + '<Meaning>' + resultf2[0])
            print(resultf2[0])
        elif "또는" in keyword2:
            resultf = keyword2.split("또는")
            #print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        elif "1." in keyword2:
            resultf = keyword2.split("1.")
            resultf2 = resultf[1].split("2.")
            #print('<Original>' + keyword + '<Meaning>' + resultf2[0])
            print(resultf2[0])
        elif "비유적" in keyword2:
            if ("을") in keyword2:
                resultf = keyword2.split("을비유적")
                #print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
            else:
                resultf = keyword2.split("를비유적")
                #print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
        elif "뜻으로" in keyword2:
            resultf = keyword2.split("는뜻으로")
            #print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        elif "줄임말" in keyword2:
            resultf = keyword2.split("의줄임말")
            #print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        else:
            if "⇒" in keyword2:
                resultf = keyword2.split("⇒")
                #print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
            else:
                #print('<Original>' + keyword + '<Meaning>' + keyword)
                print(keyword2)



def outspace(resultinput):
    if "[" in resultinput:
        key1 = resultinput.split("[")
        key2 = key1[1].split("]")
        return key2[1]
    else:
        return resultinput

def cut(resultinput):
    if "<" in resultinput:
        key1 = resultinput.split("<Meaning>")
        key2 = key1[1].split("</Meaning>")
        return key2[0]
    else:
        return resultinput

with open("inputfinalplease.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                getMeaningOfNewlyCoinedWord(data)
            except: 0




