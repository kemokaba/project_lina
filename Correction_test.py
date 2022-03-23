from ast import keyword
from fileinput import filename
import json
from os import path

filename= './plugins/correction/intents.json'
listObj = []

if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)

motcle = listObj[0]["sentences"]

var="test"

motcle += [var]

print (motcle)

listObj[0]["sentences"]=motcle

# Verify updated list
print(listObj)

with open(filename, "w") as jsonfile:
    json.dump(listObj,jsonfile)
