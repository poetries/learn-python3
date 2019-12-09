import requests

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

print(r.content)
