#!/usr/bin/env python

import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 3)

# 24-bit RGB scrolling example.
# The adafruit.png image has a couple columns of black pixels at
# the right edge, so erasing after the scrolled image isn't necessary.
matrix.Clear()
image = Image.open("../images/100px-LightOn.svg.png")
image.load()
for n in range(32, -image.size[0], -1):
	matrix.SetImage(image.im.id, n, 1)
	time.sleep(0.025)

matrix.Clear()
image = Image.open("../images/100px-LightOff.svg.png")
image.load()
for n in range(32, -image.size[0], -1):
	matrix.SetImage(image.im.id, n, 1)
	time.sleep(0.025)

matrix.Clear()