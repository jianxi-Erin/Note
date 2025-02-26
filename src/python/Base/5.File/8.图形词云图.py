import wordcloud
import jieba
from imageio import imread

with open("newFile.txt", "r", encoding="utf-8") as f:
    result = " ".join(jieba.cut(f.read()))
    img = imread('shape.jpg')

    w = wordcloud.WordCloud(
        background_color="white",
        font_path="simhei.ttf",
        mask=img,
        width=1600, height=900
    )
    print()
    w.generate(result)
    w.to_file("newWord.png")
