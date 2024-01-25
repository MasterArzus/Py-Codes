# 股票数据定向爬虫
import re
import requests
from bs4 import BeautifulSoup
import traceback


# 函数功能：原始数据爬取
def getHtmlText(url, n):
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
        # print(r.text)
        return r.text
    except:
        traceback.print_exc()


# 函数功能：获取股票列表
def getStockList(lst, stockListURL):
    ra = [11, 12, 13, 14, 15, 16, 17]
    # ra = [11]
    count = 1
    for i in ra:
        stock_list_html = getHtmlText(stockListURL + str(i), 2)
        soup = BeautifulSoup(stock_list_html, "html.parser")
        a = soup.find_all('a')

        for i in a:
            try:
                if i.text.find('(') > 1:
                    keyValue = i.text.replace(')', '')
                    keyValue = keyValue.split('(')
                    lst.append(keyValue)
                    # print(keyValue)
            except:
                traceback.print_exc()


# 函数功能：进入每个股票的链接，爬取对应股票的相关信息
def getStockInfo(lis, stockInfoURL, fpath):
    count = len(lis)
    ready_count = 0
    f = open(fpath, 'a', encoding='utf-8')
    for j in lis[:10]:
        stock_info_html = getHtmlText(stockInfoURL + str(j[1]), 2)
        print(stock_info_html)


def main():
    lst = []
    stock_list_url = "http://quote.cfi.cn/stockList.aspx?t="  # 股票列表，翻页接口
    stock_info_url = "https://quote.cfi.cn/quote.aspx?actstockid=&actcontenttype=outline&client=pc&searchcode="
    # 每个股票的链接都是"https://quote.cfi.cn/quote.aspx?actstockid=&actcontenttype=outline&client=pc&searchcode="000000的形式
    output_path = "D:\Codes\Python\web crawler(spider)\StockInfo.txt"
    getStockList(lst, stock_list_url)
    print(len(lst))
    getStockInfo(lst, stock_info_url, output_path)


if __name__ == "__main__":
    main()
