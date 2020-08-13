
import ssl
from urllib import request, parse
context = ssl._create_unverified_context( )
url = 'https://passport.bilibili.com/login'
headers = {
    #假装自己是浏览器
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  '
                  'Chrome/77.0.3865.90 Safari/537.36',
}

dict1212 = {
    'return_url': 'https://www.bilibili.com/',
    'user_name': '19856442405',
    'password': '7@4216#L',
    '_post_type': 'ajax',
 }
data = bytes(parse.urlencode(dict1212), 'utf-8')
req = request.Request(url, data=data, headers=headers, method='GET')
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))