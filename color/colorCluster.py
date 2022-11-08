# reference : https://engineer-mole.tistory.com/250
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
def load_shoe_data(filename):
  class ShoeData:
    data = []
    target = []
    feature_names = ['Name','Brand','Colors','Link','wish','review']
  shoes = ShoeData()
  with open(filename,'r', encoding ='utf-8') as f:
    for items in csv.reader(f):
      if items[0].startswith('#'): continue
      shoes.target.append(eval(items[2]))
      shoes.data.append(items)
    shoes.data = np.array(shoes.data)
    return shoes

shoes = load_shoe_data('data/shoes.csv')
fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Main Colors of Shoes (view_init(30, 330))", size = 20)
# ax.set_xlabel("R", size = 14)
# ax.set_ylabel("G", size = 14)
# ax.set_zlabel("B", size = 14)
# for colors in shoes.target:
#   RGBP = colors[0]
#   RGB = np.array(RGBP[:-1])/255.0
#   ax.scatter(RGB[0], RGB[1], RGB[2], color = RGB)
# ax.view_init(30, 330)
# plt.show()

