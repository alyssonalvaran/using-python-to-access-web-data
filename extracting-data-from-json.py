import json
import urllib.request, urllib.parse, urllib.error

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1055462.json'
data = json.loads(urllib.request.urlopen(url).read().decode())

# print(json.dumps(data, indent=4))
# counts = [comment['count'] for comment in data['comments']]
# print(sum(counts))

print(sum([comment['count'] for comment in data['comments']]))
