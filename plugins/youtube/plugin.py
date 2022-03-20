from importlib import import_module
import sys
from time import sleep
from unittest import result
sys.path.append('../../')
from pluginDefault import PluginDefault
from urllib import request, response
from googleapiclient.discovery import build
import webbrowser
import os
import asyncio
import time

api_key = 'AIzaSyBlFVhDLPeriijIn2pgCKJmRkC3jpS_inQ'

youtube = build('youtube', 'v3', developerKey=api_key)

class PluginYoutube(PluginDefault):
    #def responsevideo():
                       
     #       cmd = 'python3 Youtube_API.py'
    #        return os.system(cmd)


    def response(self, sentence=""):

        themeName= self.subject.split(".")[1]
        valuesentence = sentence.split(" ")[1]
        titre = valuesentence

        if themeName == "Youtube":
            request = youtube.search().list(
            part='snippet',
            q=titre,
            )
            result = request.execute()

            webbrowser.open('https://www.youtube.com/watch?v='+result['items'][0]['id']['videoId'])

            return result['items'][0]['snippet']['title'] + ('  https://www.youtube.com/watch?v='+result['items'][0]['id']['videoId'])





   
           

        