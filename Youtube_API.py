from textwrap import indent
from urllib import request, response
import webbrowser
from googleapiclient.discovery import build
import json

api_key = 'AIzaSyBlFVhDLPeriijIn2pgCKJmRkC3jpS_inQ'

youtube = build('youtube', 'v3', developerKey=api_key)
# ...

sentenses = '#youtube#iseefire'
titre = sentenses.split('#')[2]

request = youtube.search().list(
    part='snippet',
    q=titre,
)
response = request.execute()

    
#fichier = open("result.txt", "w")
#json.dump(response, fichier, indent = 6)
#fichier.close()

print(response['items'][0]['snippet']['title'])
webbrowser.open('https://www.youtube.com/watch?v='+response['items'][0]['id']['videoId'])

