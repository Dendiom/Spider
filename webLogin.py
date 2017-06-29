#-*-coding:utf-8-*-
#µ«¬ºŒ“” –£‘∞Õ¯ŒﬁCOOKIES

import urllib    
import urllib2    
 
#filename = 'd:\\t.html' 
url = 'http://10.3.8.211'    
    
values = {'DDDDD' : '2013210681',    
          'upass' : '061',
          'savePWD' :'0',
          '0MKKey':''}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer':'http://10.3.8.211/'}
                                
  
data = urllib.urlencode(values) 
req = urllib2.Request(url,data,headers)  
response = urllib2.urlopen(req)  
#f = open(filename,'w')
#f.write(response.read())
#f.close()
print  'Internet has connected successfully!'
