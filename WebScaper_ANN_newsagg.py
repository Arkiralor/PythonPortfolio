from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime


# path to chromedriver.exe
path = "D:\Libraries\Arkiralor's Software Setups\Chromedriver\chromedriver.exe"
# create instance of webdriver
driver = webdriver.Chrome(path)
# site url
url = 'https://bleedingcool.com/comics/manga/'
# Code to open a specific url
driver.get(url)

def scrape():
   pageInfo = []
   try:
      # wait for search results to be fetched
      WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.a, 'latest-headline'))
      )
   except Exception as e:
      print(e)
      driver.quit()
    # contains the search results


   searchResults = driver.find_elements_by_class_name('latest-headline')
   for result in searchResults:
        element = result.find_element_by_css_selector('a')
        link = element.get_attribute('href')
        header = result.find_element_by_css_selector('h3').text
        text = result.find_element_by_class_name('latest-article-excerpt').text
        ##image = result.find_element_by_class_name('thumbnail')
        pageInfo.append({'header' : header, 'link' : link, 'text': text})
   return pageInfo

pageInfo = scrape()

print(pageInfo)

df = pd.DataFrame(pageInfo)
x = str(datetime.date.today())
fileName = 'otakunews' + '_' + x + '.csv'
df.to_csv(fileName)
