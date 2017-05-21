#coding:utf-8 -*-
import requests
def getip():
	res=requests.get('http://members.3322.org/dyndns/getip')
	res.encoding = 'utf8'
	return str(res.text.replace("\n", ""))
