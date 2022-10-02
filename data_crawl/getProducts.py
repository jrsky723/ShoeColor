from io import BytesIO
import re
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = 'https://kream.co.kr/search?category_id=34&sort=popular&per_page=40'

driver = webdriver.Chrome('./data_crawl/chromedriver')
driver.maximize_window()
driver.get(url)

max_scroll_num = 50
for _ in range(max_scroll_num):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)

time.sleep(1)
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
lis = bsObj.find("div",{"class" : "search_result_list"})
items = lis.findAll("div", {"class":"search_result_item"})

# 스크롤 이후에 모든 아이템의 데이터를 추출
from colorthief import ColorThief

def getImage(a):
  picture = a.find("picture", {"class" : "picture product_img"})
  source = picture.find("source", {"type" : "image/webp"})
  imgSrc = source.get('srcset')
  return imgSrc
def getColors(a):
  imgSrc = getImage(a)
  fd = urlopen(imgSrc)
  f = BytesIO(fd.read())
  color_thief = ColorThief(f)
  palette = color_thief.get_palette(color_count=10, quality=1)
  colors = []
  for pal in palette:
    if pal[3] < 9: continue
    colors.append([pal[0], pal[1], pal[2]])
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

csvFile = open("./data/shoes.csv", 'wt')


writer = csv.writer(csvFile)
writer.writerow(('Name', 'brand', 'price', 'image', 'colors'))
for item in items:
  a = item.find("a", {"class" : "item_inner"})
  price = getPrice(a)
  if price == 0 : continue
  colors = getColors(a)
  names = getNames(a)
  brand = getBrand(a)
  image = getImage(a)
  writer.writerow((names, brand, price, image, colors))
csvFile.close()

