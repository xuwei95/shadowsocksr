#coding:utf-8 -*-
import queryalluser,queryuser,add,delect,os
print '输入选项：\n1，增加用户\n2,删除用户\n3，查询所有用户信息\n4，查询单个用户信息\n'
a=input()
if a==1:
	add.add()
elif a==2:
	delect.delect()
elif a==3:
	queryalluser.query()
elif a==4:
	queryuser.query() 
os.system('bash /root/shadowsocksr/run.sh')
print 'shadowsocksr服务已启动'
