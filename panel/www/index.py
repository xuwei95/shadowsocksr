#coding:utf-8 -*-
import web
import requests
def getip():
    res=requests.get('http://members.3322.org/dyndns/getip')
    res.encoding = 'utf8'
    return str(res.text.replace("\n", ""))
db = web.database(dbn='mysql', db = 'ss', user = 'root', pw = '123456',host="123.207.227.205",
port=3306)
urls=(
    '/','Index',
    '/test','Test',
    '/user','User',
    '/user/xinxi','xinxi',
    '/user/jiedian','jiedian',
    '/user/config','config',
    '/user/link','link',
    '/user/liuliang','liuliang',
    '/add','add',
    '/login','login',
    '/regester','regester',
    '/invite','invite',
    '/tos','tos',
    '/admin','admin',
    '/adminlogin','adminlogin'
)
render=web.template.render('templates')
class admin:
    def GET(self):
        result = db.select('user')
        return render.admin(result)
    def POST(self):
        result = db.select('user')
        return render.admin(result)
class Index:
    def GET(self):
        return render.index()
class Test:
    def GET(self,):
         result=db.select('user')
         return render.test(result)
class add:
    def POST(self):
        i = web.input()
        n = db.insert('user', server=i.server,port=i.port,user=i.user,
                      passwd=i.passwd,enable=i.enable,protocol=i.protocol,
                      method=i.method,obfs=i.obfs)
        raise web.seeother('/')
class invite:
    def GET(self,):
         return render.invite()
class tos:
    def GET(self,):
         return render.tos()
class login:
    def GET(self,):
         return render.login()
    def POST(self):
        i = web.input()
        myvar = dict(user=i.user,passwd=i.passwd)
        result = db.select('user', myvar, where="user = $user and passwd=$passwd")
        if result:
            return render.user(result)
            #raise web.seeother('/user')
        else:
            return '<script>alert("登录失败");history.back(-1)</script>'
class adminlogin:
    def GET(self,):
         return render.adminlogin()
    def POST(self):
        i = web.input()
        myvar = dict(user=i.user,passwd=i.passwd)
        res = db.select('admin', myvar, where="user = $user and passwd=$passwd")
        if res:
            result = db.select('user')
            return render.admin(result)
        else:
            return '<script>alert("登录失败");history.back(-1)</script>'
class regester:
    def GET(self,):
         return render.regester()
    def POST(self):
        i = web.input()
        myvar = dict(user=i.user)
        result = db.select('user', myvar, where="user = $user")
        if result:
            return '<script>alert("注册失败，用户名已存在");history.back(-1)</script>'
        else:
            res = db.select('user', where="port>10000")
            ports=[]
            for p in res:
                ports.append(p.port)
            for port in range(10000,65535):
                if port not in ports:
                    por=port
                    pass
            db.insert('user', user=i.user,passwd=i.passwd,port=por,used=0,u=1024*1024*100,enable=1024*1024*100,protocol='auth_aes128_sha1',canshu='%s:%s'%(por,i.passwd),method='aes-256-cfb',obfs='http_simple_compatible',type=0)
            result = db.select('user', myvar, where="user=$user")
            return render.user(result)
class xinxi:
    def GET(self):
        return render.xinxi()
    def POST(self):
        i=web.input()
        myvar = dict(id=i.id)
        result = db.select('user', myvar, where="id=$id")
        return render.xinxi(result)
class jiedian:
    def GET(self):
        return render.jiedian()
    def POST(self):
        result = db.select('server')
        return render.jiedian(result)
class config:
    def GET(self):
        i=web.input()
        var = dict(id=i.id)
        result = db.select('user', var, where="id=$id")
        return render.config(result)
    def POST(self):
        i=web.input()
        var = dict(id=i.id)
        db.update('user', where="id = $id",vars={'id': i.id},user=i.user,passwd=i.passwd,protocol=i.protocol,method=i.method,obfs=i.obfs)
        result = db.select('user', var, where="id=$id")
        return render.config(result)

class link:
    def GET(self):
        return render.link()
    def POST(self):
        i=web.input()
        myvar = dict(id=i.id)
        result = db.select('user', myvar, where="id=$id")
        return render.link(result)
class liuliang:
    def GET(self):
        return render.liuliang()
    def POST(self):
        i=web.input()
        myvar = dict(id=i.id)
        result = db.select('user', myvar, where="id=$id")
        return render.liuliang(result)
class User:
    def GET(self):
        return render.user()
if __name__=='__main__':
    web.application(urls,globals()).run()
