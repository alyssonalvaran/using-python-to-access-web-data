import json, ssl
import certifi
import urllib.request, urllib.parse, urllib.error


api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# address = 'South Federal University'
address = 'Universidade Tecnica de Lisboa'

# Always add the key first.
url = serviceurl + urllib.parse.urlencode({
        'key': api_key,
        'address': address
    })

print('Retrieving', url)
data = urllib.request.urlopen(
        url,
        context=ssl.create_default_context(cafile=certifi.where())
    ).read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('===== Failure to retrieve data =====')
    print(data)
else:
    # print(json.dumps(js, indent=4))

    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)

    print(js['results'][0]['place_id'])