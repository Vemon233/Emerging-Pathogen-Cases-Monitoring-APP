from lxml import etree
from selenium import webdriver
import time
from datetime import datetime, timedelta

driver = webdriver.Chrome()

archnum = 8704200

while archnum > 8704199:
    url = 'https://promedmail.org/promed-post/?id=20220704.' + str(archnum)
    print(url)
    driver.get(url=url)
    time.sleep(5)
    pageSource = driver.page_source
    fp1 = open(str(archnum) + '.html', 'w', encoding='utf-8')
    fp1.write(pageSource)
    archnum = archnum - 1

