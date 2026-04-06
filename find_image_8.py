import urllib.request
import ssl
import json
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')
context = ssl._create_unverified_context()

search_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Atyrau&prop=images&format=json'

req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    images = pages[idx].get('images', [])
    for img in images:
        title = img['title']
        if '.jpg' in title.lower() or '.jpeg' in title.lower():
            print(title)

