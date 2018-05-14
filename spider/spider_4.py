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
class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()
        self.func = func

    def run(self) :
        self.func()


def parseurl(start):
    global out_queue
    global count
# Content-Length: 107
# Cache-Control: max-age=0
# # Origin: http://sou.chinanews.com.cn
# # Upgrade-Insecure-Requests: 1
# # Content-Type: application/x-www-form-urlencoded
# # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
# # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# # Referer: http://sou.chinanews.com.cn/search.do
# # Accept-Encoding: gzip, deflate
# # Accept-Language: zh-CN,zh;q=0.8
# # Cookie: JSESSIONID=aaa3k0gqLLoRNhBH3RL9v
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
        "q":"我",
        "ps":20,
        "start":start,
        "type":'',
        "sort":"pubtime",
        "time_scope":0,
        "channel":"auto"

    }
    response = requests.post("http://sou.chinanews.com.cn/search.do",headers=header,data=formdata)
    contenturl = response.text
    bsObj = BeautifulSoup(contenturl,"lxml") 
    list = bsObj.findAll("li",{"class":"news_title"})
    url = ''
    try:
        for item in list:
            url = item.find("a").attrs['href']
            count +=1 
            out_queue.put(url)
    except:
        pass
        #print(url)
    print(count)
        #print(i["url"])

def getContent(url):
    global mongo
    content = ''
    try:
        response = requests.get(url)
        html = response.text.encode('ISO-8859-1').decode(response.apparent_encoding,'ignore')
        bsObj = BeautifulSoup(html,"lxml") 
        list = bsObj.find("div",{"class":"left_zw"})
        try:
            for a in list.findAll("p"):
                content += a.get_text().strip()
        except:
            pass
            #print(url)
    except Exception as e:
        print(e)
        print('解码不了!!!!!!!!!!!'+url)
    label = 4
    labelname = "汽车"
    source = "中国新闻网"
    mongo.collectionInsert(content,label,labelname,source,url)

def worker() :
    global urls_queue
    while not urls_queue.empty():
        item = urls_queue.get() #获得任务
        #print(item)
        parseurl(item)
        
def worker2():
    global out_queue
    while not out_queue.empty():
        item = out_queue.get() #获得任务
        
        #print(item)
        if 'chinanews' in item:
            getContent(item)
          
def main() :
    global urls_queue
    global count
    threads = []

    url = "http://sou.chinanews.com.cn/search.do"
    for i in range(30000,50000,20) :  #向队列中放入任务
        urls_queue.put(i)
    print('put 1000 tasks done')
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
        print(thread)

    for thread in threads :
        print(thread)
        thread.join()

    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker2)
        thread.start()
        threads.append(thread)
        print('2',thread)

    for thread in threads :
        print(thread)
        thread.join()
    print(count)

    # for thread in threads :
    #     thread.join()

    

if __name__ == '__main__':
    main()
# parseurl('http://sou.chinanews.com.cn/search.do')

