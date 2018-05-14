import requests
from bs4 import BeautifulSoup
header = {  
        "Host":"sou.chinanews.com.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.chinanews.com/china/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "JSESSIONID=aaa3k0gqLLoRNhBH3RL9v",
        "Referer": "http://sou.chinanews.com.cn/search.do",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://sou.chinanews.com.cn",
        "Upgrade-Insecure-Requests": "1"
    }

formdata = {
        "q":"和",
        "ps":20,
        "start":124000,
        "type":'',
        "sort":"pubtime",
        "time_scope":0,
        "channel":"edu"

}
response = requests.post("http://sou.chinanews.com.cn/search.do",headers=header,data=formdata)
contenturl = response.text
bsObj = BeautifulSoup(contenturl,"lxml") 
list = bsObj.findAll("li",{"class":"news_title"})
print(contenturl)
url = ''
try:
    for item in list:
        url = item.find("a").attrs['href']
        print(url)
except:
    pass
