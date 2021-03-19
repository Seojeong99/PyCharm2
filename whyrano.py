from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import sentence
from main import Jaccard_similarity
from similarity import original

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)


def ifsimilarity(s):
    if s > 0.5:
        print("1")
    else:
        print("0")


def che(keyword):
    print("야왜출력안되냐 죽고싶냐")
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
    sim = Jaccard_similarity(str1, str(result2))
    print(sim+"0")
    ifsimilarity(sim)
    original(str1, result1, result2)
    #print(Jaccard_similarity(str1, str(result2)))
    #count1 = count1 + Jaccard_similarity(str1, str(result2))

che("곰손")

#with open("input.txt", "r", encoding="UTF-8") as f:
#    list = f.readlines()
##    for i, data in enumerate(list):
 #       try:
 #           che(data)
 #       except:
 #           0
