#!/usr/bin/env python3

try:
    import Image
    import ImageDraw
    HAVE_PIL = True
except:
    try:
        from PIL import Image
        from PIL import ImageDraw
        HAVE_PIL = True
    except:
        HAVE_PIL = False

import time

from rgbmatrix import Adafruit_RGBmatrix

import requests
import json

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 3)

r = requests.get('https://spaceapi.syn2cat.lu/status/json')

obj = json.loads(r.text)

def main():

    presence = obj["sensors"]["people_now_present"][0]["value"]


    if obj["state"]["open"]:
        print("And we are open!")
        print("There are {} Hackers present NOW!".format(presence))
        openSpace()

    if obj["state"]["closed"]:
        print("And we are closed!")
        print("There were {} Hackers present! Good night, good fight!".format(presence))
        closedSpace()


def openSpace():
    matrix.Clear()
    image = Image.open("images/32px-LightOn.svg.png")
    image.load()
    for n in range(32, -image.size[0], -1):
        matrix.SetImage(image.im.id, n, 1)
        time.sleep(0.025)

def closedSpace():
    matrix.Clear()
    image = Image.open("images/32px-LightOf.svg.png")
    image.load()
    for n in range(32, -image.size[0], -1):
        matrix.SetImage(image.im.id, n, 1)
        time.sleep(0.025)


if __name__ == "__main__": main()
