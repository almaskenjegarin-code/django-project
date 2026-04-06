import urllib.request
import ssl
import json
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')
context = ssl._create_unverified_context()

title = "Файл:Atyrau City 2025.jpg"
api_url = f'https://ru.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json'

req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    if 'imageinfo' in pages[idx]:
        url = pages[idx]['imageinfo'][0]['url']
        print(f'Downloading {url}')
        
        req_img = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img, context=context) as response_img:
            with open('c:\\Users\\Admin\\Desktop\\ECO-SYSTEM\\static\\img\\atyrau_city.jpg', 'wb') as f:
                f.write(response_img.read())
        print("Success")

