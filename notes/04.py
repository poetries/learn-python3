from urllib import request

url = 'http://blog.poetries.top'

res = request.urlopen(url, timeout=1)
data = res.read().decode('utf-8')

print(data)