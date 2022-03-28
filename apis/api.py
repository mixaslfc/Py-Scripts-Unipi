# get api
import urllib.request
import json

with urllib.request.urlopen('https://api.opap.gr/draws/v3.0/1100/last-result-and-active') as response:
    html = response.read()
data=json.loads(html)

nums=data['last']['winningNumbers']['list']

last_draw=data['drawId'] #last draw

with urllib.request.urlopen('https://api.opap.gr/draws/v3.0/1100/'+str(last_draw-1)) as response:
    html = response.read()
