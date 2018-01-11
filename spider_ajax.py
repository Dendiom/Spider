# -*- coding: utf-8 -*-
"""
Created on Thu Nov 7 21:34:59 2017

@author: Pu Yuan
@descripion: 此爬虫爬取京东的图书排行榜上的图书相关ajax数据。

"""
import requests
import time
import json
from lxml import etree
import sys

#==============================================================================
# #加了下面两句话，Spyder会无法print
# reload(sys)
# 
# sys.setdefaultencoding('utf-8')
#==============================================================================

#========================== global variables ===============================

headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
}
file_path = 'data_books.txt'
url = 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1'
base_url = 'http://p.3.cn/prices/mgets?type=1^&skuIds='

def main(url):
    res = requests.get(url, headers=headers)
    res.encoding ='GBK'
    tree = etree.HTML(res.text)
    ids = tree.xpath('//dd/del/@data-price-id')
    titles = tree.xpath("//a[@class='p-name']/text()")
    authors = tree.xpath('//div[3]/dl[1]/dd/a[1]/text()')
    price_url = generate_url(base_url, ids)
    price_res = requests.get(price_url, headers=headers)
    #print price_res.text[14:-3]
    price_json = json.loads(price_res.text[14:-3])
        
    with open(file_path, 'a+') as f:
        for i in range(len(titles)):
            f.write('书名：%s      作者：%s     现价：%s     原价：%s\n' % (titles[i].encode('utf-8'),
                authors[i].encode('utf-8'), price_json[i].get('op').encode('utf-8'), price_json[i].get('m').encode('utf-8')))
    
    next_page = tree.xpath("//a[@class='pn-next']/@href")
    if next_page:
        time.sleep(3)
        next_url = 'http:' + next_page[0]
        print next_url
        main(next_url)
    else:
        print 'Mission Complete!'

def generate_url(base_url, ids):
    """组建商品价格查询时间戳.
    Args:
        base_url: 查询基本URL.
        ids：商品Id数组.
    Returns:
        组好的Url
    """
    timestamp = int(round(time.time() * 1000))
    query = ','.join(map(lambda id: 'J_' + id + ',' + 'J_' + id + ',' + 'J_' + id, ids))
    url = base_url + query + '&callback=jQuery7847582&_=' + str(timestamp)    
    #print url
    return url

def test():
    generate_url(base_url, ['dsds','dsdd','ssss'])

if __name__ == '__main__':
    main(url)
    #test()