import jieba
from mongoAPI import mongoAPI
import time
import jieba.posseg
class preprocessing:
    def __init__(self):
        self.collection_news = mongoAPI('news')
        self.ObjectId = ''
        self.stopWords = []
        self.leftWords = [] 
        self.NounWord = ['n','ns','nt','nz','Ng']
    def loadStopWords(self):
        self.stopWords = [line.strip()  for line in open('stopWord.txt').readlines() ]

    def cutWords(self,msg):
        seg_list = jieba.posseg.cut(msg)
        self.leftWords = []
        for i in seg_list:
            if (i.flag in self.NounWord) and (i.word not in self.stopWords) and (len(i.word) > 1):
                self.leftWords.append(i.word)
        # seg_list = jieba.cut(msg,cut_all=False)
        # #key_list = jieba.analyse.extract_tags(msg,20) #get keywords 
        # self.leftWords = []
        # for i in seg_list:
        #     if (i not in self.stopWords):
        #         self.leftWords.append(i)        

    def writeListWords(self):
        wordList = list(self.leftWords)
        fenci = ' '.join(wordList)
        self.collection_news.collectionUpdate(self.ObjectId,fenci)
        
    def trainKeyWords(self):
        result = self.collection_news.collectionFind({})
        i = 0
        for re in result:
            self.ObjectId = re['_id']
            content = re['content'].strip()
            ustring = content.replace(' ','')
            self.cutWords(ustring)
            self.writeListWords()
            i += 1
            if (i%100 == 0):
                print(i)

if __name__ == '__main__':
    te = preprocessing()
    te.loadStopWords()
    te.trainKeyWords()