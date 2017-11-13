#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import getTitle

def geturlList(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try:
		bsObj = BeautifulSoup(html.read(),"html.parser")
		urlList = bsObj.find_all("a",{"target":"_blank"})
	except AttributeError as e:
		return None
		
	return urlList

if __name__ == '__main__':
	urlMain = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461"
	urlList = geturlList(urlMain)
	print(getTitle.getTitle(urlMain))
	for url in urlList:
			title = getTitle.getTitle(url.attrs['href'])
			print(title)
			
'''	if urlList == None:
		print("Title could not be found")
	else:
		for url in urlList:
			title = getTitle.getTitle(url.attrs['href'])
		    print(title)
'''			
