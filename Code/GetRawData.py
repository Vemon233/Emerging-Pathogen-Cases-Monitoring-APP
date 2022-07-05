from lxml import etree
from selenium import webdriver
import time

driver = webdriver.Chrome()
archive = 20220704.8704233
url = 'https://promedmail.org/promed-post/?id=' + str(archive)
driver.get(url=url)

time.sleep(5)
pageSource = driver.page_source
fp1 = open('pagetestsource.html', 'w', encoding='utf-8')
fp1.write(pageSource)

tree = etree.parse('pagetestsource.html', etree.HTMLParser())
r = tree.xpath('//div[@class="text1"]//text()')

fp2 = open('promedtesttext.txt', 'w', encoding='utf-8')

for each in r:
    fp2.write(each + '\n')
