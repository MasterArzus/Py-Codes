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


# step 2 get proper data structure from step 1
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 遍历查找表格中信息

    for tr in soup.find('tbody').children:
        text = tr.text.replace(" ", "")
        # print(text)
        uni_info = text.split("\n")
        # 过滤掉除表格信息外的信息
        for info in uni_info:
            if info == "":
                uni_info.remove(info)

        # print(uni_info)

        ulist.append([uni_info[0], uni_info[1], uni_info[6]])


# step 2 print proper data structure
def printUnivList(ulist, num):
    # use format to print table
    print("{:^10}\t{:^14}\t{:^10}".format("Rank", "Name", "Score"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []  # to save the information of the website
    n = 30  # num to print
    url1 = "https://www.shanghairanking.cn/rankings/bcur/2023"
    html = get_original_html(url1, 2)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, n)


if __name__ == "__main__":
    main()
