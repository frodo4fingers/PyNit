from PIL import Image
import numpy as np
import sys

path = "/home/frodo/Pictures/"

image = Image.open(path + "sunbath.jpg")
image = image.resize((int(1920/8), int(1080/8)), Image.ANTIALIAS)
matrix = np.asarray(image.convert('RGB'))


def rgb2hex(rgb):
    return "%02x%02x%02x" % rgb


shape = matrix.shape
# print(shape)
rgb = []
for i in range(shape[0]):  # rows
    for k in range(shape[1]):  # columns
        rgb.append(rgb2hex((matrix[i, k][0], matrix[i, k][1], matrix[i, k][2])))

count = len(rgb)
# print(len(rgb))

colors = []
counts = []

# i = 0
for ccode in rgb:
    # sys.stdout.write("\rpixels: %i/%i" % (i+1, count))
    # sys.stdout.flush()
    if ccode not in colors:
        num = rgb.count(ccode)
        colors.append(ccode)
        counts.append(num)

    # i += 1


print("max", max(counts))
idx = counts.index(max(counts))
print("index", idx)
print(colors[idx], counts[idx])
