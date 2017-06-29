#-*-coding:utf-8-*-
#---------------------------
#时间：2016.3.11
#作者：13信工方超
#语言：python2.7
#版本：BUG版1.2
#功能：模拟登录教务处网站，计算加权成绩
#使用方法：
#    1：运行程序，在d盘下会生成一个验证码图片
#    2：在控制台输入学号密码验证码后回车，即可进入教务系统！
#!!!注意，四级成绩课程号如果为NULL，则结果不准确！
#---------------------------


import urllib
import urllib2
import cookielib
import re



#教务登录POST的地址
url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'

#验证码的地址       
url2 = 'http://jwxt.bupt.edu.cn/validateCodeAction.do?random='

#伪装的浏览器头
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer':'http://10.3.8.211/'}

#cookie与opener初始化
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#获取验证码图片
filename = 'd://yzm.jpg'
pic = opener.open(url2).read()
f = open(filename,'wb')
f.write(pic)
f.close()

#POST数据虚拟登录
name = raw_input('请输入学号：')
pwd = raw_input('请输入密码：')
yzm = raw_input('请输入验证码:')
values = {'type':'sso',
          'zjh':name,           
          'mm':pwd,            
          'v_yzm':yzm }
data = urllib.urlencode(values)
req = urllib2.Request(url,data,header)
response = opener.open(req).read()
temp1 = r'<title>(.*?)</title>'
word1 = re.compile(temp1,re.S)
title = re.search(word1,response)
if title:
    #print title.group()
    if title.group() == '<title>学分制综合教务</title>':
        print '登录教务系统成功！'  
    else:
        print '登录教务失败！'

#爬虫拔取学分与成绩
print 'Calculating....'
credits = []    #学分
scores = []    #成绩
url3 = 'http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=723'
result1 = opener.open(url3)
result2 = opener.open(url3)


test_template = r'<td align="center">\s*(\d\.?\d*)\s*</td>'
ree = re.compile(test_template,re.S)
items = re.findall(ree,result1.read())

credit = [items[i] for i in range(len(items)) if (i+1)%3 ==0]
for i in range(len(credit)):
    credits.append(float(credit[i].encode('gbk')))
print '一共有课程',len(credits),'门'
 

test_template2 = r'<p align="center">\s*(\d*.\d)&nbsp;\s*</P>'
ree2 = re.compile(test_template2,re.S|re.M)
items2 = re.findall(ree2,result2.read())
print '获取到的成绩有：',len(items2),'个'
for i in range(len(items2)):
    scores.append(float(items2[i].encode('gbk')))

sum1 = 0
for i in credits:
    sum1 = sum1 + i

sum2 = 0
for i in range(len(credits)):
    t = credits[i]*scores[i]
    sum2 = sum2 + t
    
print '加权学分绩：',sum2/sum1

    





