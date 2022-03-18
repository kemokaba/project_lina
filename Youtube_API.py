from urllib import request, response
from googleapiclient.discovery import build


api_key = 'AIzaSyBlFVhDLPeriijIn2pgCKJmRkC3jpS_inQ'

youtube = build('youtube', 'v3', developerKey=api_key)
# ...

request = youtube.search().list(
    part='snippet',
    q='baby justin',
)

response = request.execute()

print(response)