import threading
import time
import queue
import requests
import sys
import time
sys.path.append("../../")
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


def parseurl(url):
    global out_queue
    global count
    header = {  
        "Host":"channel.chinanews.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept": "*/*",
        "Referer": "http://www.chinanews.com/china/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "cnsuuid=01dee237-feb0-da1c-cc03-ce50fdf82c4311952.01435780834_1509153665130; __jsluid=e5df349eaf8e2c419ef2b3f8b89cd62a; JSESSIONID=aaa5AS1vGFJvKeinZUG9v; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1509156946; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1509158568; cn_1263394109_dplus=%7B%22distinct_id%22%3A%20%2215f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201509160031%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201509160031%7D%7D; UM_distinctid=15f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197"
    }
    response = requests.get(url,headers=header)
    contenturl = response.text
    urllist = []
    try:
        urllist = eval(contenturl[contenturl.index("["):contenturl.rindex("]") + 1])
    except:
        try:
            urllist = eval(contenturl[contenturl.index("["):contenturl.rindex("}") + 1]+']')
        except:
            print('parseurlerror!!!!!!!!' + url)
            print(count)
    url2txt = []
    for i in urllist:
        count +=1 
        out_queue.put(i["url"])
    print(count)
        #print(i["url"])

def getContent(url):
    global mongo
    content = ''
    try:
        response = requests.get(url)
        html = response.text.encode('ISO-8859-1').decode('gbk','ignore')
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
    label = 2
    labelname = "财经"
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
    url = "http://channel.chinanews.com/cns/s/channel:cj.shtml?pager=0&pagenum=100&_=1509207283512"
    for i in range(0,1000) :  #向队列中放入任务
        url = 'http://channel.chinanews.com/cns/s/channel:cj.shtml?pager=' + str(i) + '&pagenum=100&_=1509207283512'
        urls_queue.put(url)
    print('put 1000 tasks done')
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads :
        print(thread)
        thread.join()
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker2)
        thread.start()
        threads.append(thread)

    for thread in threads :
        print(thread)
        thread.join()
    print(count)

    # for thread in threads :
    #     thread.join()

    

if __name__ == '__main__':
    main()
    #parseurl('http://channel.chinanews.com/cns/s/channel:cul.shtml?pager=523&pagenum=100&_=1509173309399')

