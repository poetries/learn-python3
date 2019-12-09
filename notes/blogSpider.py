''' 
原生爬虫
'''

from urllib import request
import re,json,os

baseUrl = 'http://blog.poetries.top'
class Spider():
  url = baseUrl + '/archives/'
  pattern = '<a class="post-title" href="(.*)">([\w]*?)</a>'

  def __init__(self,page=1):
    self.page = page 

  def __fetch_content(self):
    url = Spider.url
    if self.page != 1: 
      url = Spider.url + 'page/' + str(self.page)

    r = request.urlopen(url)
    #bytes
    htmls = str(r.read(), encoding='utf-8')
    return htmls

  def _analyse(self, htmls):
    res = re.findall(Spider.pattern, htmls)

    return res

  def start(self):
    htmls = self.__fetch_content()
    return self._analyse(htmls)



# 分页获取所有文章标题
result = [] # 保存多页数据 [[],[],[]]
for page in range(1,15):
  print('开始趴取，第(%d/%d)页文章.......'%(page,14))
  spider = Spider(page)
  res = spider.start()
  result.append(res)
  if page == 14:
    print('所有页面已趴取完...')

data = [] # 处理后的数据
if len(result) != 0:
  for i in result:
    res = list(map(lambda item: {
        'url': baseUrl + item[0],
        'title': item[1]
      },i))
    # 合并两个数组 [] + []
    data += res
  
  # 保存到当前文件夹
  with open(os.path.dirname(__file__) + '/blog.text','w') as f:
    f.write(json.dumps(data))

print(data)