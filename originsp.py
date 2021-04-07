from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import pandas as pd
import pickupmachinesp as sp

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)


data_pd = pd.read_excel("D:\Sp.xls", header=None, index_col=None, sheet_name='Sheet2')
data_np = pd.DataFrame.to_numpy(data_pd)
print("~~~~~~~~~일반용어~~~~~~~~~")
print("구글 번역기")
for i in range(1, 100):
    try:
        data1 = data_np[i][2]
        data2 = data_np[i][3]
        print(data1,data2)
        sp.google(data1, data2)
    except:
        0

print("papago 번역기")
for j in range(1, 100):
    try:
        data1 = data_np[j][2]
        data2 = data_np[j][3]
        sp.naver(data1, data2)
    except:
        0

print("kakao 번역기")
sp.kakaofirst()
for k in range(1, 100):
    try:
        data1 = data_np[k][2]
        data2 = data_np[k][3]
        sp.kakao(data1, data2)
    except:
        0