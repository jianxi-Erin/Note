# 导入词云图
import wordcloud
import jieba

with open("newFile.txt", "r", encoding="utf-8") as f:
    read = f.read()
    result = ",".join(jieba.cut(read))

# 设置画布基本设置
w = wordcloud.WordCloud(
    background_color="white",
    font_path="simhei.ttf",
    width=1600, height=900
)
print(result)
# 设置输入文本,以空格分开,会自动统计相同字符个数
w.generate(result)
# 设置输出路径
w.to_file("whiteWord.png")
