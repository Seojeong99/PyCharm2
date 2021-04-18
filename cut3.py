from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
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
        st1 = str('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + purePhrase(result) + '</Meaning>')
        newstr = cut(st1)
        getMeaningOfNewlyCoined(newstr)
    except:
        st2 = str('<Original>' + keyword.replace("\n", "") + '</Original><Meaning>' + 'None' + '</Meaning>')
        newstr2 = cut(st2)
        getMeaningOfNewlyCoined(newstr2)
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

def getMeaningOfNewlyCoined(keyword):
        keyword2 = cut(keyword)
        if '\'' in keyword2:
            resultf = keyword2.split("\'")
            # print('<Original>' + keyword + '<Meaning>' + resultf[1])
            print(resultf[1])

        elif "\"" in keyword2:
            resultf = keyword2.split("\"")
            # print('<Original>' + keyword + '<Meaning>' + resultf[1])
            print(resultf[1])
        elif "‘" in keyword2:
            resultf = keyword2.split("‘")
            resultf2 = resultf[1].split("’")
            # print('<Original>' + keyword + '<Meaning>' + resultf2[0])
            print(resultf2[0])
        elif "또는" in keyword2:
            resultf = keyword2.split("또는")
            # print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        elif "1." in keyword2:
            resultf = keyword2.split("1.")
            resultf2 = resultf[1].split("2.")
            # print('<Original>' + keyword + '<Meaning>' + resultf2[0])
            print(resultf2[0])
        elif "비유적" in keyword2:
            if ("을") in keyword2:
                resultf = keyword2.split("을비유적")
                # print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
            else:
                resultf = keyword2.split("를비유적")
                # print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
        elif "뜻으로" in keyword2:
            resultf = keyword2.split("는뜻으로")
            # print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        elif "줄임말" in keyword2:
            resultf = keyword2.split("의줄임말")
            # print('<Original>' + keyword + '<Meaning>' + resultf[0])
            print(resultf[0])
        else:
            if "⇒" in keyword2:
                resultf = keyword2.split("⇒")
                # print('<Original>' + keyword + '<Meaning>' + resultf[0])
                print(resultf[0])
            else:
                # print('<Original>' + keyword + '<Meaning>' + keyword)
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

def checksimilarity(keyword):
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
    similarity = Jaccard_similarity(str1, str(result2))
    original(str1, result1, result2)
    print(Jaccard_similarity(str1, str(result2)))

    count1 = count1 + Jaccard_similarity(str1, str(result2))

with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                getMeaningOfNewlyCoinedWord(data)
            except: 0