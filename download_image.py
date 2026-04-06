import urllib.request
import ssl
import json

context = ssl._create_unverified_context()
api_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=File:Atyrau_bridge.JPG&prop=imageinfo&iiprop=url&format=json'

req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    image_url = pages[idx]['imageinfo'][0]['url']
    print(f'Found URL: {image_url}')
    
    img_req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
    with urllib.request.urlopen(img_req, context=context) as img_response:
        with open('c:\\Users\\Admin\\Desktop\\ECO-SYSTEM\\static\\img\\atyrau_bridge.png', 'wb') as f:
            f.write(img_response.read())
            print('Downloaded real image.')

