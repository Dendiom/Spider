# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:34:59 2017

@author: Pu Yuan / 袁普
@descripion: 此爬虫使用Xpath扒取百度贴吧帖子中楼主的楼层，
             每楼扒取正文以及楼主的发帖时间。
"""
import requests
import time
from lxml import etree
import sys

#加了下面两句话，Spyder会无法print
reload(sys)

sys.setdefaultencoding('utf-8')


def get_content(url):
    """获取贴吧只看楼主的数据.

    Args:
        url: 百度贴吧帖子URL.

    Returns:
        无返回值，爬取的数据存入文档中
    """
    
    start_url = url + '?see_lz=1'
    file_path = 'data.txt'
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
            }
    response = requests.get(start_url, headers=headers)
    tree = etree.HTML(response.text)
    
    #获取一共有几页
    page_count = int(tree.xpath("//li[@class='l_reply_num'][1]/span[@class='red'][2]")[0].text)
    urls = []  #超过一页的，将剩余url存入
    if page_count > 1:
        for page in range(page_count - 1):
            urls.append(url + '?see_lz=1&pn=' + str(page + 2))
    
    print 'exec url: ', start_url
    
    with open(file_path, 'w+') as f:
        get_details(tree, file_path, f)
    
        #获取剩余页面的结果
        for url in urls:
            print 'exec url: ', url
            res = requests.get(url, headers=headers)
            get_details(etree.HTML(res.text), file_path, f)
        
    print 'data crawling complete'
    
    
def get_details(tree, file_path, f):
    """将此页面的数据写入文件中.

    Args:
        txt: lxml解析结果.
        file_path: 写入的文件位置.
        f：open()函数

    Returns:
        无返回值，爬取的数据存入文档中
    """
    content = tree.xpath("//div[@class='l_post l_post_bright j_l_post clearfix  ']")
    for floor in content:
        time = floor.xpath(".//span[@class='tail-info'][last()]")[0]    #每层楼的时间
        text = floor.xpath(".//cc/div")[0].xpath('string(.)').strip()
        f.write(('更新时间: ' + time.text).encode('utf-8') + '\n\n')
        f.write(text.encode('utf-8') + '\n\n\n')
        

if __name__ == '__main__':
    #get_content('https://tieba.baidu.com/p/5260400878')
   # get_content('https://tieba.baidu.com/p/5373486660')
    get_content('https://tieba.baidu.com/p/4365220080')
    

