# import json
# import string

import requests
import re

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    # url = 'https://book.douban.com/series/31179?page=' + str(page)

    html = request_dandan(url)
    items = parse_result(html)  # 解析过滤我们想要的信息
    for item in items:
        print(item)
    for item in items:
        write_item_to_file(item)


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
            }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    f = open(r'X:\bookpy.txt', 'r+')
    # assert isinstance(item, string)
    f.write(str(item) + '\n')
    f.close()


if __name__ == "__main__":#调用main函数
    for i in range(1, 26):
        main(i)

