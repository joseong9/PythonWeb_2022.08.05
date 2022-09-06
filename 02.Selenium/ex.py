import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome('chromedriver', options=options)

url = 'https://www.google.co.kr/'
driver.get(url)


#구글 검색 상단에 숭례문 검색
search_box = driver.find_element(by=By.NAME, value='q')
search_box.send_keys('숭례문')
search_box.send_keys(Keys.ENTER)
time.sleep(2)