from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np
# from scipy.misc
'''
读入文件
'''
f = open("明朝那些事.txt","r",encoding="gbk").read()
# image = Image.open(r"index.jpg")
# mk = np.array(image)

'''
jieba分词
'''
cut_text = jieba.cut(f)
result = " ".join(cut_text)

'''
生成词云
'''
wc = WordCloud(
    font_path=r'.\simhei.ttf',#设置字体
    background_color="green",
    width=500,
    height=366,
    margin=2,
    # mask = mk   #设置背景
).generate(result)

wc.to_file("03.jpg")