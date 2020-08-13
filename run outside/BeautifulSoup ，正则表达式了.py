

import requests
from bs4 import BeautifulSoup

url = 'http://h5.hunlipic.com/web.php?id=q6YyYKL'#浪漫分享网分享个人所思所想

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

# print(soup.get_text())
# print(soup.audio)

# while True:
    # print(soup.a.next)

# print(soup.a)#只有第一个a标签

#print(soup.a.string)

# print(soup.find_all('a'))#所有的a标签中
# print(soup.find_all('div'))#所有的div

# print(soup.find_all('script'))
# print(soup.script)
# print(soup.script.string)
# print(soup.select('script'))#所有的script

# print(soup.title.parent.name)#head
# print(soup.title)#<title>灰色简约主页</title>
# print(soup.title.string)#灰色简约主页
# print(soup.find_all('meta'))
# print(soup.find_all('link'))
# print(soup.find_all('class="content"'))
# print(soup.find_all('id="large-header" '))
# print(soup.select('div > #large-header'))
print(soup.select('div > .content'))























