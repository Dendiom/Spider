#-*-coding:utf-8-*-
#---------------------------------
#beautiful 扒取百度贴吧只看楼主的文字
#---------------------------
from bs4 import BeautifulSoup
import urllib2

#[x.extract() for x in soup_packtpage.find_all('script')]  可以去掉javascript

file = open("d://tiebatxt.txt",'wb')
url = "undefind"
req = urllib2.urlopen(url).read()
  

soup = BeautifulSoup(req,"html.parser")

print "正在爬取文件"

for each in soup.find_all("div",class_="d_post_content j_d_post_content "):
    file.write(each.get_text().encode("utf8"))
    file.write('\r\n')

file.close()
print" Complete!"

