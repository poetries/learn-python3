import os
import re
import urllib.request 

#获取股票代码
def stock_id_list():
	with open('stock_num.txt') as f:
		stock = []
		for line in f.readlines():
			line = line.replace('\n','')
			stock.append(line)
		return stock

#模拟浏览器第一次点击
def first_view(stock_id):
	url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+stock_id+'/page_type/ndbg.phtml'
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
	try:
		f = urllib.request.urlopen(req)
		html = f.read().decode('gb2312')
		target = r'&id=[0-9]{6,10}'
		target_list = re.findall(target,html)
		return target_list
	except:
		print('还是编码问题！')

#模拟浏览器第二次点击，并进入下载页
def second_view(stock_id,target_list):
	for target_id in target_list:
		target_url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+stock_id+'&id='+target_id
		treq = urllib.request.Request(target_url)
		treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
		try:
			f = urllib.request.urlopen(treq) 
			thtml = f.read().decode('gbk')
			#print(thtml)
			try:
				file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
				local = './'+stock_id+'/'+file_url.group(0).split("/")[-1]+'.PDF'
#+'.pdf'
				print (file_url.group(0))
				urllib.request.urlretrieve(file_url.group(0),local,None)
               
			except:
				print('这里没有可供下载PDF的链接')

		except:
			print('文件编码有问题！')

#测试
if __name__ == '__main__':
	stock_list = stock_id_list()
	for stock_id in stock_list:
		os.mkdir('./'+stock_id)
		try:
			target_list = first_view(stock_id)
			second_view(stock_id,target_list)
		except:
			print("这支股票停牌了")





	
