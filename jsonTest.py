#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import json
import urllib.request as ur
import urllib.parse as par
from datetime import timedelta, datetime
import time

url = "https://level2.lu/spaceapi/"

xml = ur.urlopen(url).read()

data = json.loads(xml.decode('utf-8'))

stateOpen = data['state']['open']
stateLast = data['state']['lastchange']
now = time.time()

def getTime(seconds):
    sec = timedelta(seconds=int(seconds))
    d = datetime(1,1,1) + sec

    if d.day-1 > 0:
        return("{} day(s), {} hour(s), {} minute(s) and {} seconds".format(d.day-1, d.hour, d.minute, d.second))
    elif d.hour > 0:
        return("{} hour(s), {} minute(s) and {} seconds".format(d.hour, d.minute, d.second))
    elif d.minute > 0:
        return("{} minute(s) and {} seconds".format(d.minute, d.second))
    else:
        return("{} seconds".format(d.second))

st = getTime(now- stateLast)

print("Last triggered: " + st)

if stateOpen == True:
  print("Space is open!")
  countPeople = data['sensors']['people_now_present']
  print("We are " + str(countPeople[0]['value']))
  type(countPeople)
else:
  print("We are closed :(")

