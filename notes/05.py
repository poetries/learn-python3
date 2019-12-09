import requests
import json
import re

url = 'http://fs.bravestonezou.top:8888/files?filepath=//jty-person-app&_=1575772630473'

res = requests.get(url)

files = json.loads(res.text)['files']
 
names = []
for item in files:
  names.append(item['name'].split('.apk')[0])

# print(names)

# 列表推导式
print(list([item['name'].split('.apk')[0]] for item in files))