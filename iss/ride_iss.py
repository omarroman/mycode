import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

## display out pythonic data
print("\n\nConverted python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson['number'])
people = helmetson['people']
#print(people)

for peeplist in people:
    #print(peeplist)
    print( "{} is on the {}".format(peeplist['name'], peeplist['craft']))
