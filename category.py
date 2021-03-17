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

list1 = list()
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
        categorize(similarity,keyword)
        print(similarity)

def categorize(s,keyword):
    if s > 0.9



with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
            try:
                checksimilarity(data)
            except: 0