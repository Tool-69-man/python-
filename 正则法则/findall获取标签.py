import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import urllib.request
import re
sock = urllib.request.urlopen(r"http://h5.hunlipic.com/web.php?id=q6YyYKL")
htmlStr=sock.read()#???read()不能用
sock.close()
print('open tags')
# print(re.findall(r"<[^/>][^>]+[^/>]>", htmlStr))
print('close tags')
print(re.findall(r"</[^>]+>",htmlStr))
print('self-closing  tags')
# print(re.findall(r"<[^>]+/", htmlStr))