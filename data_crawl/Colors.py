
color = {
    "Hot Pink": (236, 111, 189),
    "Pink": (249, 177, 225),
    "Red": (216, 0, 22),
    "Salmon": (255, 154, 132),
    "Orange": (243, 102, 0),
    "Harvest": (255, 200, 0),
    "Yellow": (238, 237, 116),
    "Navy Blue": (7, 23, 93),
    "Royal Blue": (52, 138, 225),
    "Baby Blue": (138, 193, 235),
    "Turquoise": (0, 200, 224),
    "Green": (0, 185, 104),
    "Acovado": (93, 136, 56),
    "Light Green": (157, 228, 144),
    "Purple" : (91,0,121),
    "Black" : (15,24,32),
    "Gray" : (173,174,176),
    "White" : (250,252,251),
    "Ecru" : (232,230,223),
    "Tan" : (210,166,133),
    "Brown" : (107,52,15)
}

def closestColor(rgb):
  differences = {}
  for colorName, colorRgb in color.items():
    r,g,b = colorRgb
    differences[sum([(r - rgb[0])**2, (g - rgb[1])**2, (b - rgb[2])**2])] = colorName
  return differences[min(differences.keys())]

print(closestColor((0,0,3)))