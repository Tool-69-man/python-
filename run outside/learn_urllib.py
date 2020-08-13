import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))

