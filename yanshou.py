from mongoAPI import mongoAPI
from preprocessing import preprocessing
from sklearn.cross_validation import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB  
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import numpy as np
from sklearn.metrics import confusion_matrix  
from sklearn.ensemble import GradientBoostingClassifier
import time
#训练、测试

class Train_Test:

    def GBDT(self,trainLabel,testLabel):

        clf = GradientBoostingClassifier(random_state=10)   
        clf.fit(fea_train,np.array(trainLabel))
        pred = clf.predict(fea_test)
        totalScore(testLabel,pred)  

    def nbClassifier(self):
        
        clf = MultinomialNB(alpha = 0.01)   
        clf.fit(self.fea_train,np.array(self.trainLabel))
        return clf
        
    def logisticReg(self):

        clf = LogisticRegression()
        clf.fit(self.fea_train,np.array(self.trainLabel)) 
        return clf

    def SVM(self):
        
        clf = LinearSVC(random_state=0)
        clf.fit(self.fea_train,np.array(self.trainLabel)) 
        return clf
    
    def test(self,clf):
        pred = clf.predict(self.fea_test)
        self.totalScore(self.testLabel,pred)

    #模型评价
    def totalScore(self,testLabel,pred):
        A = 0
        labels = ['体育','娱乐','财经','房产','汽车','教育','法制','时政','能源','健康']
        labels.append('总数')
        print(classification_report(testLabel, pred))
        labelname = '\t'
        conf_mat = metrics.confusion_matrix(testLabel, pred)
        print('confusion matrix:')
        for i in labels:
            labelname = labelname + i + '\t'
        print(labelname)
        rowsum = conf_mat.sum(axis = 1)
        for i in range(len(conf_mat)):
            row = str(i) + '\t'
            for j in range(len(conf_mat[i])):
                row = row + str(conf_mat[i][j]) + '\t'
            row += str(rowsum[i])
            print(row)
        row = '*' + '\t'
        rowsum = conf_mat.sum(axis = 0)
        for j in range(len(conf_mat)):
            row = row + str(rowsum[j]) + '\t'
        row += str(sum(sum(conf_mat)))
        print(row)
        
    def preprocess(self):
        #数据预处理、分词
        # pre = preprocessing()
        # pre.loadStopWords()
        # pre.trainKeyWords()
        
        #从mongodb中读取分词后的样本
        trainCorpus = []
        classLabel = []
        result = mongoAPI('news').collectionFind({'label':{'$ne':6}})
        for re in result:
            if 'fenci' in re:
                trainCorpus.append(re['fenci'].strip())
                classLabel.append(re['label'])
        self.trainData, self.testData, self.trainLabel, self.testLabel = train_test_split(trainCorpus, classLabel, test_size = 0.5)

        print('*'*80 + '\n生成tfidf向量\n' + '*'*80 )
        start = time.time()
        tv=TfidfVectorizer(max_features=50000)#该类会统计每个词语的tf-idf权值    
        self.fea_train = tv.fit_transform(self.trainData)    #return feature vector 'fea_train' [n_samples,n_features]  
        self.fea_test = tv.transform(self.testData)   
        f = open('feature_names_tfidf.txt','w+')
        f.writelines([i + '\n' for i in tv.get_feature_names()])
        f.close()
        print('Size of fea_train:' + str(self.fea_train.shape))
        print('Size of fea_test:' + str(self.fea_test.shape))
        print(self.fea_train.nnz)
        print(self.fea_test.nnz)
        end = time.time()
        print('-'*80 + '\n生成tfidf向量耗时' + ('%.2fs'%(end-start)) + '\n' + '-'*80)

        # print('*'*80 + '\nlogisticReg\n' + '*'*80)
        # start = time.time()
        # logisticReg(trainLabel,testLabel)
        # end = time.time()
        # print('-'*80 + '\n逻辑回归分类耗时' + ('%.2fs'%(end-start)) + '\n' + '-'*80)

        # print('*'*80 + '\nSVM\n' + '*'*80 )
        # start = time.time()
        # SVM(trainLabel,testLabel)
        # end = time.time()
        # print('-'*80 + '\nSVM分类耗时' + ('%.2fs'%(end-start)) + '\n' + '-'*80)

        # print('*'*80 + '\nNaive Bayes\n' + '*'*80 )
        # start = time.time()
        # nbClassifier(trainLabel,testLabel)
        # end = time.time()
        # print('-'*80 + '\n朴素贝叶斯分类耗时' + ('%.2fs'%(end-start)) + '\n' + '-'*80)

        # print('*'*80 + '\nGBDT\n' + '*'*80 )
        # start = time.time()
        # GBDT(trainLabel,testLabel)
        # end = time.time()
        # print('-'*80 + '\nGBDT分类耗时' + ('%.2fs'%(end-start)) + '\n' + '-'*80)    
