from io import BytesIO
import re
from turtle import color
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = 'https://kream.co.kr/search?category_id=34&sort=popular&per_page=40'

driver = webdriver.Chrome('./data_crawl/chromedriver')
driver.maximize_window()
driver.get(url)

max_scroll_num = 100
for _ in range(max_scroll_num):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2)

time.sleep(1)
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
lis = bsObj.find("div",{"class" : "search_result_list"})
items = lis.findAll("div", {"class":"search_result_item"})

# 스크롤 이후에 모든 아이템의 데이터를 추출
def getLink(a):
  return 'https://kream.co.kr' + a.get('href') + " "

def getImage(a):
  picture = a.find("picture", {"class" : "picture product_img"})
  source = picture.find("source", {"type" : "image/webp"})
  imgSrc = source.get('srcset') + " "
  return imgSrc

from colorthief import ColorThief
import Colors as MyCol

def getColors(a):
  imgSrc = getImage(a)
  fd = urlopen(imgSrc)
  f = BytesIO(fd.read())
  color_thief = ColorThief(f)
  palette = color_thief.get_palette(color_count=10, quality=1)
  colors = []
  for col in palette:
    if col[3] < 8: continue
    cName = MyCol.closestColor(col[0:3])
    colors.append([cName, col[3]])
  return colors


def getNames(a):
  EngName = a.find("p", {"class","name"}).getText()
  return EngName

def getBrand(a):
  return a.find("p", ["class", "brand"]).getText()
  
def getPrice(a):
  priceStr = a.find("div", ["class", "amount"]).getText()
  numbers = re.sub(r'[^0-9]', '', priceStr)
  price = 0
  if len(numbers): price = int(numbers)
  return price

import csv

csvFile = open("./data/shoes.csv", 'w',encoding='utf-8', newline='')
writer = csv.writer(csvFile)
writer.writerow(('Name', 'Brand', 'Price', 'Image', 'Colors', 'Link'))
for item in items:
  a = item.find("a", {"class" : "item_inner"})
  price = getPrice(a)
  if price == 0 : continue
  link = getLink(a)
  Colors = getColors(a)
  name = getNames(a)
  brand = getBrand(a)
  image = getImage(a)
  writer.writerow((name, brand, price, image, Colors, link))
csvFile.close()