#!/usr/bin/env python3

import json
import urllib.request as ur
import urllib.parse as par
import datetime
import time

url = "https://level2.lu/spaceapi/"

xml = ur.urlopen(url).read()

data = json.loads(xml.decode('utf-8'))

stateOpen = data['state']['open']
stateLast = data['state']['lastchange']
now = int(time.time())

print("Last triggered: " + str((now - stateLast)))

print(stateLast)

if stateOpen == True:
  print("Space is open!")
else:
  print("We are closed :(")

countPeople = data['sensors']['people_now_present']
type(countPeople)

print("We are " + str(countPeople[0]['value']))