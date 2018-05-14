# import requests

# header = {  
#     "Host":"channel.chinanews.com",
#     "Connection": "keep-alive",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     "Accept": "*/*",
#     "Referer": "http://www.chinanews.com/china/",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Cookie": "cnsuuid=01dee237-feb0-da1c-cc03-ce50fdf82c4311952.01435780834_1509153665130; __jsluid=e5df349eaf8e2c419ef2b3f8b89cd62a; JSESSIONID=aaa5AS1vGFJvKeinZUG9v; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1509156946; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1509158568; cn_1263394109_dplus=%7B%22distinct_id%22%3A%20%2215f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201509160031%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201509160031%7D%7D; UM_distinctid=15f60917399469-08d01802aeb572-31657c00-13c680-15f6091739a197"
# }
# response = requests.get('http://channel.chinanews.com/cns/s/channel:life.shtml?pager=232&pagenum=100&_=1509201938117',headers=header)
# contenturl = response.text
# f = open('test.txt','w+')
# f.write(contenturl[contenturl.index("["):contenturl.rindex("]") + 1])
# f.close()
# urllist = eval(contenturl[contenturl.index("["):contenturl.rindex("]") + 1])

# url2txt = []
# for i in urllist:
#     url2txt.append(i["url"] + '\n')
# print(url2txt)
# # f = open('gn.txt','a+')
# # #去除最后的空格
# # f.writelines(url2txt)
# # f.close()
import chardet
import requests
from bs4 import BeautifulSoup
url = 'http://www.chinanews.com/house/2017/09-29/8343199.shtml'
response = requests.get(url)
html = response.text.encode('ISO-8859-1').decode(response.apparent_encoding,'ignore')
print(html)
print(response.apparent_encoding)
# soup = BeautifulSoup(response.text,"lxml")
# print(soup.original_encoding)
# html = response.text.encode('ISO-8859-1').decode(,'ignore')
# print(html)