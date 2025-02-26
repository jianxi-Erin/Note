# jieba是优秀的中文分词词库
import jieba

with open("newFile.txt", "r", encoding="utf-8") as file:
    read = file.read()
# 分词,不使用精确切分,
#  jieba.cut(read, cut_all=False)默认精确模式,将句子最精确地切开,适合文本分析
# jieba.cut(read, cut_all=True)全模式:把句子中所有的可以成词的词语都扫描出来, 速度快,但是不能解决歧义问题
# lcut_for_search(seg_str)搜索引擎模式:在精确模式的基础上,对长词再次切分,提高召回率,适合用于搜索引擎分词
re = jieba.cut(read, cut_all=False)
letters = " ".join(re)
# ?设置切分使用的分隔符
print(letters)

from jieba import analyse

# 统计词频
mix = jieba.analyse.extract_tags(read, topK=5)
print(mix)
