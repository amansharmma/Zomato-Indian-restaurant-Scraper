from pprint import pprint
import xlsxwriter
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://www.zomato.com/bangalore/top-restaurants'

def request(url):
	driver = webdriver.Chrome()
	driver.get(url)
	response = driver.execute_script("return document.documentElement.outerHTML")
	driver.quit()
	soup = BeautifulSoup(response,'html.parser')
	return (soup)
soup = (request(url))
x = []
new = soup.find('div',class_='row col-res-list collection_listings_container')
g = new.find_all("div",class_="col-s-8 col-l-1by3")
dic = {}
for i in g :
	b = (i.find("a").text.strip())
	a = (i.find("div",class_="res_title zblack bold nowrap"))
	c = (i.find("div",class_="nowrap grey-text fontsize5 ttupper"))
	dic["name"] = (a.text.strip())
	dic["ratings"] = (b[:3])
	dic["Adress"] = (c.text.strip())
	x.append(dic.copy())
m = []
n = []
workbook = xlsxwriter.Workbook('xl1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hotel Names') 
worksheet.write('B1', 'Ratings') 
worksheet.write('C1', 'Address') 

working = xlsxwriter.Workbook('xl2.xlsx')
work = working.add_worksheet()

work.write('A1', 'Hotel Names') 
work.write('B1', 'Ratings') 
work.write('C1', 'Address')

row = 0
col = 0
ecol = 1
row1 = 0
col1 = 0
ecol1 = 1
for k in x :
	if k["ratings"] == 'NEW':
		pass
	elif float(k['ratings']) < 4.0 :
		row += 1
		m.append(k)
		worksheet.write(row,col, k["name"]) 
		worksheet.write(row,col+1, k["ratings"]) 
		worksheet.write(row,ecol+1, k["Adress"])
	elif float(k["ratings"]) >= 4.0 :
		row1 += 1
		n.append(k)
		work.write(row1,col1, k["name"]) 
		work.write(row1,col1+1, k["ratings"]) 
		work.write(row1,ecol1+1, k["Adress"])
workbook.close()
working.close()
# print (m)
# print (n)n