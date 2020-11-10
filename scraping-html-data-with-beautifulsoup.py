import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# import ssl

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
    # print(line.decode().strip())

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = 'http://www.dr-chuck.com/page1.htm'
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1055459.html'
# html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
numbers = [
    int(tag.contents[0])
    for tag in tags
    if tag.get('class')[0] == 'comments'
]

print(sum(numbers))