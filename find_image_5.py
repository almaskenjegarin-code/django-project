import urllib.request
import ssl
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

context = ssl._create_unverified_context()

# Find the URL for a well known photo of Imangali Mosque
api_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Imangali_Mosque&prop=images&format=json'

req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
with urllib.request.urlopen(req, context=context) as response:
    data = json.loads(response.read())

pages = data['query']['pages']
for idx in pages:
    images = pages[idx].get('images', [])
    for img in images:
        title = img['title']
        if '.jpg' in title.lower() or '.png' in title.lower():
            
            # Now get the URL for this file
            img_info_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
            img_req = urllib.request.Request(img_info_url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
            try:
                with urllib.request.urlopen(img_req, context=context) as img_resp:
                    img_data = json.loads(img_resp.read())
                    img_pages = img_data['query']['pages']
                    for p_idx in img_pages:
                        if 'imageinfo' in img_pages[p_idx]:
                            url = img_pages[p_idx]['imageinfo'][0]['url']
                            print(f'Downloading {url}')
                            dl_req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
                            with urllib.request.urlopen(dl_req, context=context) as dl_resp:
                                with open('c:\\Users\\Admin\\Desktop\\ECO-SYSTEM\\static\\img\\atyrau_mosque.jpg', 'wb') as f:
                                    f.write(dl_resp.read())
                            print('Success')
                            sys.exit(0)
            except Exception as e:
                print(e)
