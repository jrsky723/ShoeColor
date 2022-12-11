import numpy as np
import matplotlib.pyplot as plt
import math
import colorsys


def step (r,g,b, repetitions=1):
    lum = math.sqrt( .241 * r + .691 * g + .068 * b )
    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)
    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum
    return (h2, lum, v2)

def sort(colorlist): 
  colorlist.sort(key=lambda rgb: step(rgb[0],rgb[1],rgb[2], 5))

#reference : https://www.alanzucconi.com/2015/09/30/colour-sorting/


# get closest color from webcolors. But we didn't use this function.
# import webcolors

# def closest_color(requested_color):
#     min_colors = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_color[0]) ** 2
#         gd = (g_c - requested_color[1]) ** 2
#         bd = (b_c - requested_color[2]) ** 2
#         min_colors[(rd + gd + bd)] = name
#     return min_colors[min(min_colors.keys())]

if __name__ == "__main__" :
  # k = 400
  # colors = [np.random.rand(3) for n in range(k)]
  # sort(colors)
  # arr_2d = np.reshape(colors, (20,20,3))
  # plt.imshow(arr_2d)
  # plt.show()
  requested_color = [119, 172, 152]
  closest_name = closest_color(requested_color)
  print("closest color name:", closest_name)

