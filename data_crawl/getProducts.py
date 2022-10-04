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

max_scroll_num = 20
for _ in range(max_scroll_num):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)

time.sleep(1)
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
lis = bsObj.find("div",{"class" : "search_result_list"})
items = lis.findAll("div", {"class":"search_result_item"})

# 스크롤 이후에 모든 아이템의 데이터를 추출
def getLink(a):
  return 'https://kream.co.kr' + a.get('href')

def getImage(a):
  picture = a.find("picture", {"class" : "picture product_img"})
  source = picture.find("source", {"type" : "image/webp"})
  imgSrc = source.get('srcset')
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
  KorName = a.find("p", {"class","translated_name"}).getText()
  return [EngName, KorName]

def getBrand(a):
  return a.find("p", ["class", "brand"]).getText()
  
def getPrice(a):
  priceStr = a.find("div", ["class", "amount"]).getText()
  numbers = re.sub(r'[^0-9]', '', priceStr)
  price = 0
  if len(numbers): price = int(numbers)
  return price

import csv

csvFile = open("./data/shoes.csv", 'w',encoding='euc-kr', newline='')
writer = csv.writer(csvFile)
writer.writerow(('Name', 'Brand', 'Price', 'Image', 'Colors', 'Link'))
for item in items:
  a = item.find("a", {"class" : "item_inner"})
  price = getPrice(a)
  if price == 0 : continue
  link = getLink(a)
  Colors = getColors(a)
  names = getNames(a)
  brand = getBrand(a)
  image = getImage(a)
  writer.writerow((names, brand, price, image, Colors, link))
csvFile.close()

# todo 비슷한 색깔로 색깔 단순화 작업, sql로 데이터베이스 저장,
#신발의 구매를 할 수 있게끔 링크도 따로 저장하는게 나을듯