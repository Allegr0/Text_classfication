from bs4 import BeautifulSoup
import requests
from mongoAPI import mongoAPI
def findAllContent(url, collection_news):
    html = requests.get(url[3]).text
    bsObj = BeautifulSoup(html,"lxml") 
    list = bsObj.find("div",{"class":"post_text"})
    if not list:
        list = bsObj.find("div",{"class":"g-articleSpec-left"})
    text = ''
    if list:
        for a in list.findAll("p"):
            text += a.get_text()
        text = text.replace("\n","")
        text = text.replace("\t","")
        collection_news.collectionInsert(text,url[0],url[1],url[2],url[3])

def findAllNews(url,collection_news):
    html = requests.get(url[3]).text
    bsObj = BeautifulSoup(html,"lxml") 
    list = bsObj.find("div",{"class":"area areabg1"})
    print(len(list.findAll("a")))
    for a in list.findAll("a"):
        url[3] = a.attrs['href']
        findAllContent(url,collection_news)
collection_news = mongoAPI('news') 
url = []
# url.append([0,'体育','网易','http://news.163.com/special/0001386F/rank_sports.html'])
# url.append([1,'娱乐','网易','http://news.163.com/special/0001386F/rank_ent.html'])
# url.append([2,'财经','网易','http://money.163.com/special/002526BH/rank.html'])
# url.append([3,'科技','网易','http://news.163.com/special/0001386F/rank_tech.html'])
# url.append([4,'汽车','网易','http://news.163.com/special/0001386F/rank_auto.html'])
url.append([5,'游戏','网易','http://news.163.com/special/0001386F/game_rank.html'])
# url.append([6,'旅游','网易','http://news.163.com/special/0001386F/rank_travel.html'])
# url.append([7,'教育','网易','http://news.163.com/special/0001386F/rank_edu.html'])


for u in url:
    print(u)
    findAllNews(u,collection_news)
# findAllNews(url2)
