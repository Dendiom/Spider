#-*-coding:utf-8-*-
#---------------------------
#��Դ������
#���ԣ�python2.7
#���ܣ��������°ٿ�ҳ���ϵ�������Ϣ
#---------------------------

import urllib2
import re

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer':'http://10.3.8.211/'}
url = 'http://www.qiushibaike.com/textnew/'   #���°ٿ�����ҳ��

res = urllib2.Request(url,headers = header)
response = urllib2.urlopen(res)
data = response.read().decode('utf-8')
test_template = r'<div class="content">\s*(.*?)\s*<!--\d*-->'
ree = re.compile(test_template,re.S)
items = re.findall(ree, data)

test_template2 = r'<span class="page-numbers">\s*(\d*)\s*</span>'
ree2 = re.compile(test_template2,re.S)
items2 = re.findall(ree2,data)

print 'һ��������ҳ��:',items2[len(items2)-1],'ҳ'
print


if items:
    num = 1
    for i in items:
        print '%d: ' % (num) ,i
        print
        num += 1
else:
    print 'ƥ��ʧ��'




