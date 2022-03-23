import time
import sys
sys.path.append('../../')
from pluginDefault import PluginDefault
from ast import keyword
from fileinput import filename
import json
from os import path
import os


class PluginCorrection(PluginDefault):
    def response(self, sentence=""):
        themeName= self.subject.split(".")[1]
        if themeName=="Correction":
            chemin = sentence.split(" ")[1]
            #print(chemin)
            newsentence=sentence.split(" ")[2]

            filename= 'plugins/'+chemin+'/intents.json'
            #print(filename)
            
            listObj = []

            if path.isfile(filename) is False:
                raise Exception("File not found")
            
            # Read JSON file
            with open(filename) as fp:
                listObj = json.load(fp)

            motcle = listObj[0]["sentences"]
            motcle += [newsentence]

            #print (motcle)

            listObj[0]["sentences"]=motcle

            # Verify updated list
            print(listObj)

            with open(filename, "w") as jsonfile:
                json.dump(listObj,jsonfile)
        os.system ("python3 models.py")
        return 'Correction terminée'