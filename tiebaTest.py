#-*-coding:utf-8-*-
#---------------------
#名称:百度贴吧爬虫测试
#时间2016.3.5
#语言:python 2.7
#功能：下载输入页面内容
#----------------------

#函数主体
import urllib2
from ensurepip import __main__

def tiebaSpider(url,startpage,endpage):
    for i in range(startpage,endpage+1):
        filename = 'd:\\tiebe%d.html' % i
        print '正在下载第%d页内容' % i
        f = open(filename,'w')
        req = urllib2.urlopen(url+str((i-1)*50)).read()
        f.write(req)
    print '下载完毕'
    f.close()
    
#曼联吧url
url = 'http://tieba.baidu.com/f?kw=%E6%9B%BC%E8%81%94&ie=utf-8&pn='
sp = int(raw_input('请输入起始页码'))
ep = int(raw_input('请输入结束页码'))


tiebaSpider(url, sp, ep)

        
        
    

