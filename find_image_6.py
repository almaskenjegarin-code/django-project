import urllib.request
import ssl

context = ssl._create_unverified_context()
url = 'https://upload.wikimedia.org/wikipedia/commons/0/0f/Atyrau_railway_station.jpg'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 ECO-SYSTEM-Bot/1.0'})
with urllib.request.urlopen(req, context=context) as response:
    with open('c:\\Users\\Admin\\Desktop\\ECO-SYSTEM\\static\\img\\atyrau_station.jpg', 'wb') as f:
        f.write(response.read())
print('Downloaded successfully')

