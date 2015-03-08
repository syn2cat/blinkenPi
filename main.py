#!/usr/bin/env python3

import Image
import ImageDraw
import time

import requests
import json

r = requests.get('https://spaceapi.syn2cat.lu/status/json')

obj = json.loads(r.text)

presence = obj["sensors"]["people_now_present"][0]["value"]


if obj["state"]["open"]:
    print("And we are open!")
    print("There are {} Hackers present NOW!".format(presence))
