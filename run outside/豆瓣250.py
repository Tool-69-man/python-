# import re
# from bs4 import BeautifulSoup
# import requests
#
#
# def return_requests(url):
#     # try:
#     #     response = requests.get(url)
#     #     if response.status_code == 200:
#     #         return response.text
#     # except requests.RequestException:
#     #     return None
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#     except requests.RequestException:
#         return None
#
#
# def main(page):
#     url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
#     html = return_requests(url)
#     print(html)
#     # soup = BeautifulSoup(html, 'lxml')
#     # save_excel(soup)
#
#
# if __name__ in '__main__':
#     for i in range(1, 26):
#         main(i)
import requests
from bs4 import BeautifulSoup





def request_douban(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None





def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    print(html)


if __name__ == '__main__':

    for i in range(0, 10):
        main(i)


