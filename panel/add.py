#coding:utf-8 -*-
import json,getip
def liuliang(x):
	return x*1024**3
def queryuser(x,a):
	for m in a:
		if x==m[u'user']:
			return True
	return False
def queryport(x,a):
        for m in a:
                if x==m[u'port']:
                        return True
        return False
def add():
	f = file("/root/shadowsocksr/mudb.json");
	a= json.load(f);##server,user,port,passwd,used,enable,protoco,canshu,method,obfs,type
	server=getip.getip()		
	print '输入选项：\n1，增加单端口多用户端口\n2，添加普通用户'
	b=input()
	if b==1:
		user= raw_input('输入用户：')
		if queryuser(user,a):
			print '用户名已存在，请重新输入'
		else:
			port= input('输入端口(0-65535)：')
			if queryport(port,a):
				print '端口已被占用，请重新输入'
			else:
				passwd= raw_input('输入密码：')
				obfs='http_simple_compatible'
				used=0
				u=0
				enable=input('输入可用流量(GB)：')
				protocol='auth_aes128_sha1'
				method='aes-128-cfb'
				m={'enable':1,'user':user,'passwd':passwd,'port':port,'obfs':obfs,'d':used,'transfer_enable':liuliang(enable),'u':0,'protocol':protocol,'protocol_param':'#','method':method}
				a.append(m)
				json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
				print '成功添加多用户端口:%d'%port
				print '连接信息为：\n服务器：%s\n端口：%d\n密码：%s\n加密方法：%s\n协议：%s\n混淆方式：%s\n'%(server,port,passwd,method,protocol,obfs)
	elif b==2:
		user= raw_input('输入用户：')
		if queryuser(user,a):
			print '用户名已存在，请重新输入'
		else:
			port= input('输入端口(0-65535,大于65535仅可使用单端口多用户端口)：')
			if queryport(port,a):
				print '端口已被占用，请重新输入'
			else:
				passwd= raw_input('输入密码：')
				obfs='http_simple_compatible'
				used=0
				u=0
				enable=input('输入可用流量(GB)：')
				protocol='auth_aes128_sha1'
				canshu='%d:%s'%(port,passwd)
				method='aes-128-cfb'
				m={'enable':1,'user':user,'passwd':passwd,'port':port,'obfs':obfs,'d':used,'transfer_enable':liuliang(enable),'u':0,'protocol':protocol,'protocol_param':'','method':method}
				a.append(m)
				json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
				print '成功添加用户:%s'%user
				print '连接信息为：\n服务器：%s\n端口：%d\n密码：%s\n加密方法：%s\n协议：%s\n混淆方式：%s\n'%(server,port,passwd,method,protocol,obfs)
				print '单端口多用户协议参数为：%s'%canshu
	f.close();

