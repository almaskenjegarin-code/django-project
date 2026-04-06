import urllib.request
import ssl
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

context = ssl._create_unverified_context()
search_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Atyrau&prop=images&format=json'

req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    images = pages[idx].get('images', [])
    for img in images:
        print(img['title'])

