#一段简单的 Python 爬虫程序

#读出一个URL下的a标签里href地址为.html的所有地址

#!/usr/bin/python
# Filename: test.py

import urllib

content = urllib.urlopen('http://codecloud.net').read()
s1 = 0
while s1 >= 0:
    begin = content.find(r'<a',s1)
    m1 = content.find(r'href=',begin)
    m2 = content.find(r'>',m1)
    if(content[m1:m2].find(r'.html')!=-1):
        m2 = content.find(r'.html',m1)
        url = content[m1+6:m2+5]
        print url
    s1 = m2     
