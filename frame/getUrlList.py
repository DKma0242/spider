#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def geturlList(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		urlList = bsObj.find_all('a')
	except AttributeError as e:
		return None
		
	return urlList

if __name__ == '__main__':
	urlList = geturlList("http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=3634961")
	if urlList == None:
		print("Title could not be found")
	else:
		for url in urlList:
			print(url)