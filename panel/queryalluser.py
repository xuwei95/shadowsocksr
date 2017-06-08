#coding:utf-8 -*-
import json,getip
def fun(val):
        ret=""
        if val / 1024 < 4:
                ret += "%s" % val
        elif val / 1024 ** 2 < 4:
                val /= float(1024)
                ret += "%s KB" % val
        elif val / 1024 ** 3 < 4:
                val /= float(1024 ** 2)
                ret += "%s MB" % val
        else:
                val /= float(1024 ** 3)
                ret += "%s GB" % val
        return ret
def query():
        f = file("/root/shadowsocksr/mudb.json")
        a= json.load(f);##server,user,port,passwd,used,enable,protoco,canshu,method,obfs,type
        server=getip.getip()
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
                print u"服务器：%s\n用户名：%s\n密码：%s\n端口：%d\n已用流量：%s\n剩余流量：%s\n总流量：%s\n加密方法：%s\n混淆方式：%s\n协议：%s\n单端口多用户协议参数：%s\n"%(server,user,passwd,port,fun(used),fun(u),fun(enable),method,obfs,protocol,canshu)
        f.close()
