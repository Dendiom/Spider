#-*-coding:utf-8-*-
#---------------------------
#ʱ�䣺2016.3.11
#���ߣ�13�Ź�����
#���ԣ�python2.7
#�汾��BUG��1.2
#���ܣ�ģ���¼������վ�������Ȩ�ɼ�
#ʹ�÷�����
#    1�����г�����d���»�����һ����֤��ͼƬ
#    2���ڿ���̨����ѧ��������֤���س������ɽ������ϵͳ��
#!!!ע�⣬�ļ��ɼ��γ̺����ΪNULL��������׼ȷ��
#---------------------------


import urllib
import urllib2
import cookielib
import re



#�����¼POST�ĵ�ַ
url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'

#��֤��ĵ�ַ       
url2 = 'http://jwxt.bupt.edu.cn/validateCodeAction.do?random='

#αװ�������ͷ
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer':'http://10.3.8.211/'}

#cookie��opener��ʼ��
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#��ȡ��֤��ͼƬ
filename = 'd://yzm.jpg'
pic = opener.open(url2).read()
f = open(filename,'wb')
f.write(pic)
f.close()

#POST���������¼
name = raw_input('������ѧ�ţ�')
pwd = raw_input('���������룺')
yzm = raw_input('��������֤��:')
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
    if title.group() == '<title>ѧ�����ۺϽ���</title>':
        print '��¼����ϵͳ�ɹ���'  
    else:
        print '��¼����ʧ�ܣ�'

#�����ȡѧ����ɼ�
print 'Calculating....'
credits = []    #ѧ��
scores = []    #�ɼ�
url3 = 'http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=723'
result1 = opener.open(url3)
result2 = opener.open(url3)


test_template = r'<td align="center">\s*(\d\.?\d*)\s*</td>'
ree = re.compile(test_template,re.S)
items = re.findall(ree,result1.read())

credit = [items[i] for i in range(len(items)) if (i+1)%3 ==0]
for i in range(len(credit)):
    credits.append(float(credit[i].encode('gbk')))
print 'һ���пγ�',len(credits),'��'
 

test_template2 = r'<p align="center">\s*(\d*.\d)&nbsp;\s*</P>'
ree2 = re.compile(test_template2,re.S|re.M)
items2 = re.findall(ree2,result2.read())
print '��ȡ���ĳɼ��У�',len(items2),'��'
for i in range(len(items2)):
    scores.append(float(items2[i].encode('gbk')))

sum1 = 0
for i in credits:
    sum1 = sum1 + i

sum2 = 0
for i in range(len(credits)):
    t = credits[i]*scores[i]
    sum2 = sum2 + t
    
print '��Ȩѧ�ּ���',sum2/sum1

    





