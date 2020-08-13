

import learn_urllib.request
response = learn_urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))
