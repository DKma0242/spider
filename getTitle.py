#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		title = bsObj.title.text
	except AttributeError as e:
		return None
		
	return title

if __name__ == '__main__':
	title = getTitle("http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=3634961")
	if title == None:
		print("Title could not be found")
	else:
		print(title)

