from lxml import etree
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://promedmail.org/promed-post/?id=20220209.8701353')

time.sleep(5)
pageSource = driver.page_source
fp1 = open('pagetestsource.html', 'w', encoding='utf-8')
fp1.write(pageSource)

tree = etree.parse('pagetestsource.html', etree.HTMLParser())
r = tree.xpath('//div[@class="text1"]//text()')

fp = open('promedtesttext.txt', 'w', encoding='utf-8')

for each in r:
    fp.write(each + '\n')