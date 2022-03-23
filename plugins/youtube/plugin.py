from importlib import import_module
import sys
from time import sleep
from unittest import result
sys.path.append('../../')
from pluginDefault import PluginDefault
from urllib import request, response
from googleapiclient.discovery import build
import webbrowser

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

            if "#open" in sentence:
                choix = sentence.split(".")[1]
                if choix == "1":
                    webbrowser.open('https://www.youtube.com/watch?v='+result['items'][0]['id']['videoId'])
                    return result['items'][0]['snippet']['title']
                elif choix == "2":
                    webbrowser.open('https://www.youtube.com/watch?v='+result['items'][1]['id']['videoId'])
                    return result['items'][1]['snippet']['title']
                elif choix == "3":
                    webbrowser.open('https://www.youtube.com/watch?v='+result['items'][2]['id']['videoId'])
                    return result['items'][2]['snippet']['title']

            #Si valuesentence = sentence.split(" ")[1] est null:
            #return 'Champ vide'
            
            return result['items'][0]['snippet']['title'] + ('  https://www.youtube.com/watch?v='+result['items'][0]['id']['videoId']) + '\n' + \
                    result['items'][1]['snippet']['title'] + ('  https://www.youtube.com/watch?v='+result['items'][1]['id']['videoId']) + '\n' + \
                    result['items'][2]['snippet']['title'] + ('  https://www.youtube.com/watch?v='+result['items'][2]['id']['videoId'])