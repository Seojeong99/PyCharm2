from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:/driver/geckodriver.exe")
driver.wait = WebDriverWait(driver, 2)
