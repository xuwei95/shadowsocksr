#coding:utf-8 -*-
import json
import pymysql
import getip
import time
# 连接数据库
connect = pymysql.Connect(
    host='123.207.227.205',
    port=3306,
    user='root',
    passwd='123456',
    db='ss',
    charset='utf8'
)
cursor = connect.cursor()
def update():
	f = file("/root/shadowsocksr/mudb.json")
	a= json.load(f)
	for x in a:
		user= x[u'user']
		passwd= x[u'passwd']
		port= x[u'port']
		obfs= x[u'obfs']
		used=x[u'd']
		enable=x[u'transfer_enable']
		u=enable-used
		protocol=x[u'protocol']
		canshu='%d:%s'%(port,passwd)
		method=x[u'method']
		if x[u'protocol_param']=='#':
			typ=1
		else:
			typ=0
		sql1="SELECT id FROM user WHERE user=%s AND type=0"
		cursor.execute(sql1,user)
		results = cursor.fetchall()
		if results:
			data=(used,u,enable,results[0][0])
			sql="UPDATE user SET used=%s,u=%s,enable=%s WHERE id=%s"
			cursor.execute(sql % data)
			connect.commit()
			print '更新:',data
		# else:
		# 	data=(server,user,port,passwd,used,u,enable,protocol,canshu,method,obfs,typ)
		# 	sql="INSERT INTO user (server,user,port,passwd,used,u,enable,protocol,canshu,method,obfs,type) VALUES ( '%s','%s', '%s','%s', '%s', '%s','%s','%s','%s', '%s', '%s','%s')"
		# 	cursor.execute(sql % data)
		# 	connect.commit()
		# 	print '插入：',data
def update1():
    sql="SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    j=[]
    for res in results:
        if res[11]==1:
            protocol_param="#"
        else:
        	protocol_param=""
        a={'d':res[4],
            'user':res[1],
           'port':res[2],
           'passwd':res[3],
           'u':0,
           'transfer_enable':res[6],
           'enable':1,
           'method':res[9],
           'protocol':res[7],
           'protocol_param':protocol_param,
           'obfs':res[10]}
        j.append(a)
    json.dump(j, open('/root/shadowsocksr/mudb.json', 'w'))
    print '更新成功'
while True:
    update()
    update1()
    time.sleep(10)
