import threading
import time
import queue
import requests
import sys
import time
sys.path.append("../")
from mongoAPI import mongoAPI
from bs4 import BeautifulSoup

urls_queue = queue.Queue()  #构造一个不限制大小的的队列
out_queue = queue.Queue()
count = 0
_WORKER_THREAD_NUM = 8   #设置线程个数
mongo = mongoAPI('news')


def getContent(url):
    global mongo
    content = ''
    try:
        response = requests.get(url)
        html = response.text.encode('ISO-8859-1').decode(response.apparent_encoding,'ignore')
        bsObj = BeautifulSoup(html,"lxml") 
        list = bsObj.find("div",{"class":"left_zw"})
        if list == None:
            list = bsObj.find("font",{"id":"Zoom"})
        if list == None:
            list = bsObj.find("div",{"id":"newstext"})        
        try:
            if list.find('p') == None:
                for a in list.findAll("span"):
                    content += a.get_text().strip()
            else:
                for a in list.findAll("p"):
                    content += a.get_text().strip()
        except:
            pass
            #print(url)
    except Exception as e:
        print(e)
        print('解码不了!!!!!!!!!!!'+url)
    label = 10
    labelname = "健康"
    source = "中国新闻网"
    #print(url,content)
    return content
    # mongo.collectionInsert(content,label,labelname,source,url)


    

if __name__ == '__main__':
    print(getContent('http://www.chinanews.com/jk/2014/12-11/6867833.shtml'))
    result = mongo.collectionFind({'label':10,'content':''})
    for re in result:
        ObjectId = re['_id']
        url = re['url']
        if '/m/' in url:
            url = url.replace('/m/','/')
        if '/shipin/' in url:
            continue
        content = getContent(url)
        if content == '':
            continue
        mongo.collectionUpdateContent(ObjectId,content)