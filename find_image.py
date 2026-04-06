import urllib.request
import ssl
import json

context = ssl._create_unverified_context()
search_url = 'https://en.wikipedia.org/w/api.php?action=query&generator=images&titles=Atyrau&gimlimit=10&prop=imageinfo&iiprop=url&format=json'

req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    if 'imageinfo' in pages[idx]:
        image_url = pages[idx]['imageinfo'][0]['url']
        title = pages[idx]['title']
        if '.jpg' in image_url.lower() or '.png' in image_url.lower():
            print(f'Found: {title} -> {image_url}')

