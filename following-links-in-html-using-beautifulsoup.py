import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = input('Enter URL: ')
# count = int(input('Enter count: '))
# position = int(input('Enter position: '))

url = 'http://py4e-data.dr-chuck.net/known_by_Ramsey.html'
count = 7
position = 18

name = ''

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tag = soup('a')[position - 1]
    name = tag.contents[0]
    url = tag.get('href')

print(name)