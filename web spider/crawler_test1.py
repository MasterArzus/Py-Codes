import requests
# requests library
import scrapy
import re
from bs4 import BeautifulSoup
# 这样引入beautifulSoup

# requests.request('GET', url, **kargs)
# 1 arg: params: '字典或键值对，字节序列，添加到url中找到对应的资源'
# 2 arg: data: 向服务器提交资源时使用, '后面可提交字符串，字典等，存在网页服务器不同位置，text获取来确认'
# 3 arg: json: 向服务器提交JSON格式文件
# 4 arg: headers: 字典，http定制头，模拟各种浏览器访问网页，如: headers = {'user-agent': 'Chrome/10'}
# 5 arg: cookies:
# 6 arg: auth:
# 7 arg: files: transport files to the server files = {'file': open('data.xls', 'rb')}
# 8 arg: proxies: 字典类型，增加代理访问服务器
# 9 arg: allow_redirects: True/False 是否允许重定向
# 10 arg: stream: True/False 是否允许立即下载
# 11 arg: verify: True/False 认证ssl路径
# 12 arg: cert: True/False 本地ssl路径


# define standard crawler function
def getHTMLtext(url, n):
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


if __name__ == "__main__":
    url1 = "http://www.baidu.com"
    url2 = "http://www.bing.com"
    url3 = "http://python123.io/ws/demo.html"

    demo = getHTMLtext(url3, 1)
    soup = BeautifulSoup(demo, "html.parser")
    # 对demo进行html的词法解析，soup为解析后的文本
    tag = soup.a
    # tag 的属性是bs4.element.Tag

    print(tag.attrs)
    # attrs 返回的是一个字典(dict)，可以通过['key']的方式来查找value
    print(tag)
    print(tag.string)

    # find links in the 'a' module and find with dict key 'href'
    # 'a' can be replace by ['a', 'b'] to find all info of tag 'a', 'b'
    for link in soup.find_all('a'):
        print(link.get('href'))

    # return navigable string
    print(soup.prettify())
