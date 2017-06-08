#coding:utf-8 -*-
import json
def queryuser(x,a):
	i=0
	for m in a:
		if x==m[u'user']:
			return i
		else:
			i+=1
	return False
def delect():
	f = file("/root/shadowsocksr/mudb.json");
	a= json.load(f);
	print '输入要删除的用户：'
	user= raw_input()
	x=queryuser(user,a)
	if x:
		del(a[x])
		print '成功删除用户%s'%user
		json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
	else :
		print '用户名不存在，请重新输入'
	f.close();
