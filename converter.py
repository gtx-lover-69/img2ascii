import sys, random, argparse
from tkinter import Image

import numpy as np
import math

from PIL import image

gscale = '@%#*+=-:. '

def getAvg(image):
    img = np.array(image)
    w,h = img.shape
    return np.average(img.reshape(w*h))

def convertToASCII(image):
    global gscale
    image = Image.open(filename).convert('L')
    W, H = image.size[0], image.size[1]
    print(W, H)

    w = W/cols

    h = w/scale

    rows = int(H/h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    if cols > W or rows > H:
        print