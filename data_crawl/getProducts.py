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

max_scroll_num = 100
curScroll = 1;
for _ in range(max_scroll_num):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  if curScroll % 10 == 0 :
    print(f'Current Scroll :{curScroll}')
  curScroll += 1
  time.sleep(2)

time.sleep(1)
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
lis = bsObj.find("div",{"class" : "search_result_list"})
items = lis.findAll("div", {"class":"search_result_item"})

# 스크롤 이후에 모든 아이템의 데이터를 추출
from colorthief import ColorThief
import number as MyNum
def getLink(a):
  return 'https://kream.co.kr' + a.get('href') + " "

def getImage(a):
  try:
    picture = a.find("picture", {"class" : "picture product_img"})
    source = picture.find("source", {"type" : "image/webp"})
    imgSrc = source.get('srcset') + " "
  except:
    imgSrc = 'NULL'
  return imgSrc

def getColors(a):
  try:
    imgSrc = getImage(a)
    fd = urlopen(imgSrc)
    f = BytesIO(fd.read())
    color_thief = ColorThief(f)
    palette = color_thief.get_palette(color_count=10, quality=1)
    colors = []
    for col in palette:
      if col[3] < 8: continue
      colors.append(col)
    colors = sorted(colors, key = lambda x : -x[3])
  except:
    print(f'getColor Exception\n{imgSrc}')
    colors = [(-1,-1,-1,-1)]
  return colors

def getName(a):
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
def getWish(I):
  figure = I.find("span", ["class", "wish_figure"])
  text = figure.find("span", ["class", "text"]).getText()
  return MyNum.getNumber(text)

def getReview(I): 
  figure = I.find("span",["class","review_figure"])
  text = figure.find("span", ["class", "text"]).getText()
  return MyNum.getNumber(text)

import csv

csvFile = open("./data/shoes.csv", 'w',encoding='utf-8', newline='')
writer = csv.writer(csvFile)
writer.writerow(('Name', 'Brand', 'Colors', 'Link'))
itemCnt = 0
for item in items:
  if itemCnt == 1000 : break
  a = item.find("a", {"class" : "item_inner"})
  I = item.find("div", {"class" : "interest_figure"})
  price = getPrice(a)
  if price == 0 : continue
  itemCnt += 1
  if itemCnt % 100 == 0 : print(f'itemCnt: {itemCnt}')
  wish = getWish(I)
  review = getReview(I)
  link = getLink(a)
  Colors = getColors(a)
  name = getName(a)
  brand = getBrand(a)
  writer.writerow((name, brand, Colors, link))
csvFile.close()