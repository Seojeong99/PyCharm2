from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)

def getMeaningOfNewlyCoinedWord(keyword):
    URL = "https://www.naver.com/"
    driver.get(URL)
    time.sleep(5)
    for i in range(0, len(keyword)):
        try:
            driver.find_element_by_css_selector('#query').clear()
            time.sleep(3)
            driver.find_element_by_css_selector('#query').send_keys(keyword[i])
        except:
            driver.find_element_by_css_selector('#nx_query').clear()
            time.sleep(3)
            driver.find_element_by_css_selector('#nx_query').send_keys(keyword[i])

        time.sleep(3)

        try:
            driver.find_element_by_css_selector('.ico_search_submit').click()
        except:
            driver.find_element_by_css_selector('.bt_search > i:nth-child(1)').click()

        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            result = soup.find('p', class_='mean api_txt_lines').text
            print('<Original>' + keyword[i] + '</Original><Meaning>' + result + '</Meaning>')
        except:
            print('<Original>' + keyword[i] + '</Original><Meaning>' + 'None' + '</Meaning>')

def getTranslatedResult(keyword):
    URL = "https://translate.google.com/?sl=ko&tl=en&op=translate"
    driver.get(URL)
    time.sleep(3)
    for i in range(0, len(keyword)):
        driver.find_element_by_css_selector('.er8xn').clear()
        time.sleep(3)
        driver.find_element_by_css_selector('.er8xn').send_keys(keyword[i])
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        result = soup.find('div', class_='NqnNQd').text
        print('<Original>' + keyword[i] + '</Original><Translated>' + str(result) + '</Translated>')

def getRecommendedSearchKeyword(keyword):
    URL = "https://www.google.com"
    driver.get(URL)
    time.sleep(5)
    for i in range(0, len(keyword)):
        driver.find_element_by_css_selector('.gLFyf').clear()
        time.sleep(3)
        driver.find_element_by_css_selector('.gLFyf').send_keys(keyword[i])
        time.sleep(2)
        driver.find_element_by_css_selector('.gLFyf').send_keys(Keys.RETURN)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        try:
            result = soup.find('a', class_='gL9Hy').text
            print('<Original>' + keyword[i] + '</Original><Recommended>' + str(result) + '</Recommended>')
        except:
            print('<Original>' + keyword[i] + '</Original><Recommended>' + 'None' + '</Recommended>')

def getKakaoTranslatedResult():
    driver.get('https://translate.kakao.com/')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/a/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys('안녕')
    time.sleep(3)
    temp = driver.page_source

    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('p', class_='desc_translation').text


    print(result)

    #temp = temp[temp.index('desc_translation'):]
    #temp = temp[len('desc_translation'):]
    #temp = temp[2:]
    #temp = temp[:temp.index("</p>")]
    #print(temp)

def navernews():
    driver.get('https://news.naver.com/')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    result = soup.find_all('a', class_="list_tit nclicks('rig.renws2')")
    for i in range(0, len(result)):
        temp = str(result[i])
        temp = temp[temp.index(">") + 1:]
        temp = temp[:temp.index("</a>")]
        print(temp)

def Jaccard_similarity(doc1, doc2):
    doc1 = set(doc1)
    doc2 = set(doc2)
    return len(doc1 & doc2) / len(doc1 | doc2)

if __name__ == "__main__":
    word = ['낄끼빠빠', '아아', '맛있냥', '멀라염', '뻐카충']
    word2 = ['난 잘 몰라 요', '나 는몰 라요', '배 가너무 고파요', '아 아를 먹을래?', '아이스아 메리카노']
    #getMeaningOfNewlyCoinedWord(word)
    #getTranslatedResult(word)
    #getRecommendedSearchKeyword(word2)
    #getKakaoTranslatedResult()
    #navernews()

    str1 = "I go to school"
    str2 = "he didn't go to school"
    print(Jaccard_similarity(str1, str2))

