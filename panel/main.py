#coding:utf-8 -*-
import queryalluser,queryuser,add,delect,os
print '输入选项：\n1，开启服务\n2,关闭服务\n3,添加用户\n4,删除用户\n5,查询所有用户信息\n6,查询单个用户信息\n'
a=input()
if a==1:
	os.system('bash /root/shadowsocksr/run.sh')
	print 'shadowsocksr服务已启动'
elif a==2:
	os.system('bash /root/shadowsocksr/stop.sh')
	print 'shadowsocksr服务已关闭'
elif a==3:
	add.add()
	os.system('bash /root/shadowsocksr/run.sh')
elif a==4:
	delect.delect()
	os.system('bash /root/shadowsocksr/run.sh')
elif a==5:
	queryalluser.query()
elif a==6:
	queryuser.query() 
