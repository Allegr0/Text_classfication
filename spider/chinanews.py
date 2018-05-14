import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("..")
from mongoAPI import mongoAPI
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    ,"Accept-Encoding":"gzip, deflate"
    ,"Accept-Language":"zh-CN,zh;q=0.8"
    ,"Cache-Control":"max-age=0"
    ,"Connection":"keep-alive"
    ,"Cookie":"cnsuuid=01dee237-feb0-da1c-cc03-ce50fdf82c4311952.01435780834_1509153665130; JSESSIONID=aaaZGLsdnemEybu-HKG9v; __jsluid=e5df349eaf8e2c419ef2b3f8b89cd62a; cn_1263394109_dplus=%7B%22distinct_id%22%3A%20%2215f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201509154898%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201509154898%7D%7D; UM_distinctid=15f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197"
    ,"Host":"channel.chinanews.com"
    ,"Upgrade-Insecure-Requests":"1"
    ,"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.3"
    }



def getContent(url):
    response = requests.get(url)
    html = response.text.encode('ISO-8859-1').decode('gbk','ignore')
    bsObj = BeautifulSoup(html,"lxml") 
    list = bsObj.find("div",{"class":"left_zw"})
    content = ''
    for a in list.findAll("p"):
        content += a.get_text().strip()
    return content

if __name__ == '__main__':
    print(getContent('http://www.chinanews.com/gn/2017/10-23/8358915.shtml'))
    # label = 8
    # labelname = "时政"
    # source = "中国新闻网"
    # mongo = mongoAPI('news')
    # f = open('gn1.txt','r')
    # filecontent = eval(f.readline())
    # for i in filecontent:
    #     url = i["url"]
    #     content = getContent(url)
    #     #print(content)
    #     mongo.collectionInsert(content,label,labelname,source,url)


# print(html)