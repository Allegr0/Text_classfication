# 100万新闻样本集文本分类实验 
语料库包含总共1029815条文档，包含体育、娱乐、财经、房产、汽车、教育、法制、时政、能源、健康共10类，每类样本数量均在10万条以上。  
爬取的中国新闻网的数据，爬虫代码写的比较low，在spider/目录下。  
采用文档型数据库Mongodb存储语料库。每条记录包含8个字段:  
id、类别名称、文本内容、记录来源的url、类别编号、记录来源的门户名称、Jieba分词结果、Nlpir分词结果。  
采用jieba分词和Nlpir分词两种分词库，但是代码中只有jieba分词，Nlpir分词结果在队友的机器上跑的直接写进了mongodb数据库。  
基于sklean库采用DF、TF-IDF两种向量化放法、以及GBDT、SVM、LR、Navie Bayes四种算法对比试验  
由于样本集很大，采用DF、TF-IDF两种向量化方法在准确率上没体现出区别。  
由于样本集中有几类样本质量一般，最后得到的最高准确率是SVM算法跑出的88%。  
程序运行结果在fenci1结果和fenci2结果两个文件中。  
  
  mongodb数据库备份文件超过4个G，没法上传百度网盘。。。


