import re
import sentence
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from main import Jaccard_similarity

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

count1 = 0
def checksimilarity(keyword):
    global count1
    URL3 = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver.get(URL3)
    time.sleep(4)
    driver.find_element_by_css_selector('.er8xn').clear()
    time.sleep(4)
    keyword = keyword.replace("\n", "")
    str1 = keyword
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
    #similarity = Jaccard_similarity(str1, str(result2))
    original(str1, result1, result2)
    print(Jaccard_similarity(str1, str(result2)))

    count1 = count1 + Jaccard_similarity(str1, str(result2))


def original(string1, resultf1, resultf2):
    print('<original>' + string1 + '<original tr>' + str(resultf1) + '<final tr>' + str(resultf2))

with open("챠.txt", "r", encoding="UTF-8") as f:#오리지널 단어 번역출력, 유사도 출력
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                checksimilarity(data)
            except: 0

