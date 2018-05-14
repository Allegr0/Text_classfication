from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
import numpy as np

from sklearn import metrics
vectorizer = TfidfVectorizer()
corpus = [
     'This is the first document.',
     'This is the second second document.',
     'And the third one.',
     'Is this the first document?',
 ]

# analyze = vectorizer.build_analyzer()
X = vectorizer.fit_transform(corpus)
X_test = vectorizer.transform(['this is the 123'])
print(vectorizer.get_feature_names() )
print(X_test.toarray())
    # tv=TfidfVectorizer()#该类会统计每个词语的tf-idf权值    
    # fea_train = tv.fit_transform(trainData)    #return feature vector 'fea_train' [n_samples,n_features]  
    # fea_test = tv.transform(testData)  
# joblib.dump(vectorizer, 'vectorizer.vc') 
vectorizer1 = joblib.load('vectorizer.vc') 
test = vectorizer.transform(['ths s t4he 123'])
print(test)
# test1 = vectorizer1.transform(['ths s t4he 123'])
# print(test.toarray())
# print(test1.toarray())
# print(vectorizer.get_feature_names())
# print(X.nnz)
# print(X.toarray())
# print(vectorizer)



# X = np.random.randint(5, size=(6, 100))
# y = np.array([1, 2, 3, 4, 5, 6])
# print(X)
# from sklearn.naive_bayes import MultinomialNB
# clf = MultinomialNB()
# clf.fit(X, y)
# MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
# print(clf.predict(X[2:4]))
# label = [0,1,2,3,3,1,2,0]
# pred = [1,3,2,3,2,0,0,0]
# conf_mat = metrics.confusion_matrix(label, pred)
# conf_mat.sum(axis = 0)

# print(conf_mat)
# print(sum(sum(conf_mat)))
# print(conf_mat.sum(axis = 0))
# print(conf_mat.sum(axis = 1))


