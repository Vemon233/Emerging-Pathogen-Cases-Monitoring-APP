from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://promedmail.org/promed-post/?id=20220209.8701353')

time.sleep(5)

mytext = driver.page_source
print(mytext)