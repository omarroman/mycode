#!/usr/bin/env python3

import urllib.request
import json
import yaml

## Trace the Space
quizspace = 'http://api.open-notify.org/astros.json'

## Call the webservice
quizctrl = urllib.request.urlopen(quizspace)

## put fileobject into helmet
quiz = quizctrl.read()

## decode json to python data structure
quizson = json.loads(quiz.decode('utf-8'))

## display out pythonic data
#print("\n\nConverted python data")
#print(quizson)

peeps = []
for person in quizson['people']:
    dict1 = {}
    dict1["first_name"] = person['name'].split()[0]
    dict1["last_name"] = person['name'].split()[1]
    dict1["craft"] = person['craft']
    peeps.append(dict1)

print(peeps)

qfile = open("quizguide.yaml", "w")
yaml.dump(peeps, qfile)
qfile.close()
