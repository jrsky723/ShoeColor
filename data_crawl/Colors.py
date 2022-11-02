color = {
    "Hot Pink": (236, 111, 189),
    "Pink": (249, 177, 225),
    "Red": (216, 0, 22),
    "Salmon": (255, 154, 132),
    "Orange": (243, 102, 0),
    "Harvest": (242, 205, 85),
    "Yellow": (238, 237, 116),
    "Navy Blue": (7, 23, 93),
    "Royal Blue": (3, 100, 159),
    "Baby Blue": (138, 193, 235),
    "Turquoise": (0, 200, 224),
    "Green": (38, 95, 69),
    "Light Green": (157, 228, 144),
    "Olive": (130, 125, 72),
    "Purple": (91, 0, 121),
    "Black": (24, 24, 24),
    "Gray": (173, 174, 176),
    "White": (232, 230, 223),
    "Brown": (146, 111, 75),
    "Mocha": (99, 80, 66)
}

# reference by tewlipdesigigns https://www.tewlipdesigns.com/thread-colors

def closestColor(rgb):
  differences = {}
  for colorName, colorRgb in color.items():
    r, g, b = colorRgb
    differences[sum([(r - rgb[0])**2, (g - rgb[1]) **
                    2, (b - rgb[2])**2])] = colorName
  return differences[min(differences.keys())]

import matplotlib.pyplot as plt

fig = plt.figure()
i = 1 
for key, val in color.items():
  ax = fig.add_subplot(5, 5, i)
  ax.imshow([[val]])
  ax.axis("off")
  ax.set_title(key)
  i += 1
plt.subplots_adjust(hspace=1)
plt.show()
