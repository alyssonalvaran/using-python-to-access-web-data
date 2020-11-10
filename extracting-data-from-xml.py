# import xml.etree.ElementTree as ET
# data= '''
#     <person>
#         <name>Chuck</name>
#         <phone type="intl">
#             +1 734 303 4456
#         </phone>
#         <email hide="yes"/>
#     </person>
# '''

# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

# input = '''<users>
#     <user x="2">
#         <id>001</id>
#         <name>Chuck</name>
#     </user>
#     <user x="7">
#         <id>009</id>
#         <name>Brent</name>
#     </user>
# </users>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('user')
# print('User count:', len(lst))
# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = input('Enter URL: ')

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1055461.xml'
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
counts = [int(count.text) for count in tree.findall('.//count')]

print(sum(counts))