import jieba

import jieba.posseg
msg = '我爱北京王菲天安门贝克汉姆是打发第三方的算法都被称作是是防守打法地方'
seg_list = jieba.posseg.cut(msg)

for i in seg_list:
    print(i.word,i.flag)

import jieba.analyse
result=jieba.analyse.extract_tags(msg,4) 
print(result)