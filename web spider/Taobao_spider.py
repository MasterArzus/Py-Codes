import re
import bs4
import requests
from bs4 import BeautifulSoup


# step 1 get context from web
def get_original_html(url, n):
    simulator = {"user-agent": "Mozilla/5.0"}
    simulator2 = {"user-agent": "Chrome/10"}
    # need try to catch error
    # 要注意异常处理
    try:
        if n == 1:
            r = requests.get(url, timeout=30)
            print(r.status_code)
            # access successfully while status code = 200, (404x)
            print(r.request.headers)
            # headers 查看发送给网页的头部信息
        if n == 2:
            r = requests.get(url, timeout=30, headers=simulator2)
            # get中headers可以添加虚拟浏览器进行访问
            print(r.status_code)
            # access successfully while status code = 200, (404x)
            print(r.request.headers)
            # headers 查看发送给网页的头部信息

        r.raise_for_status()  # if not 200 then HTTP error occurs
        # 上面这个方法用来判断网络链接状态
        r.encoding = r.apparent_encoding
        return r.text
    except requests.ConnectionError as ce:
        return "Http error: " + str(ce)


def parsePage(ilt, html):
    return 0


def printGoodslist(ilt):
    return 0


def main():
    # define the searching item
    good = "电脑"
    # define the searching depth
    depth = 2
    # define the info list
    Infolist = []
    start_url = "https://s.taobao.com/search?q=" + good

    for i in range(depth):
        # try turning to next page
        try:
            url = start_url + "&s=" + str(44*i)
            html = get_original_html(url, 2)
            parsePage(Infolist, html)
        except:
            print("Page {} error".format(i))
            continue

    printGoodslist(Infolist)


if __name__ == "__main__":
    main()
