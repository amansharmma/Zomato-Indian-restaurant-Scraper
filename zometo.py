from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get('https://www.zomato.com/indore')
response = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(response,'html.parser')
driver.quit()
colections = soup.find("div",class_="collections-grid row")
a = colections.find("div",class_="col-l-16 col-s-16").a["href"]
driver = webdriver.Chrome()
driver.get(a)
response = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(response,'html.parser')
driver.quit()
t = soup.find("div",class_="col-l-16 collections-tab-content mbot")
pprint (t)