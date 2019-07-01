import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
from PIL import Image
import numpy as np

'''
文件路径配置，绘图字体配置
'''
stop_path = '百度停用词列表.txt'
noval_path = '明朝那些事.txt'
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

'''
读入停用词，生成停用词列表
'''
stop_list = []
def read_stopword():

    stop_list1 = open(stop_path,encoding='gbk').readlines()
    for line in stop_list1:
        stop_list.append(line.strip('\n').strip())
    # return stop_list


'''
读入要分析的文件
'''
def read_file():
    noval = open(noval_path,encoding='gbk').read()
    return noval


'''
对数据进行jieba分词，返回分词后的列表。
'''
def txt_cut(noval):
    return [w for w in jieba.cut(noval) if w not in stop_list and len(w) > 1]

'''
生成柱状图
'''
def Statistics(txtcut):
    word_count = pd.Series(txtcut).value_counts().sort_values(ascending=False)[0:20]
    print(word_count)
    plt.figure(figsize=(15, 8))
    x = word_count.index.tolist()  # 获取的是index列，转换成list
    y = word_count.values.tolist()  # 获取的是values列，转换成list
    print(list(zip(x, y)))
    sns.barplot(x, y, palette="BuPu_r")
    plt.title('词频Top20')
    plt.ylabel('count')
    sns.despine(bottom=True)
    plt.savefig('./词频统计.png', dpi=400)
    plt.show()

'''
生成词云
'''
def wordcloud(txt_cut):
    result = " ".join(txt_cut)
    image = Image.open(r'index.png')
    graph = np.array(image)
    wc = WordCloud(
        font_path=r'.\simhei.ttf',  # 字体地址
        background_color='white',  # 背景色
        max_font_size=100,  # 显示字体最大值
        max_words=100,  # 最大词数
        mask=graph
    )
    wc.generate(result)
    # image_color = wordcloud.ImageColorGenerator(graph)
    # wc.recolor(color_func=image_color)
    wc.to_file(r"cloud.png")
    plt.title("史上第一混乱词云图")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()


'''
主函数调用
'''
def main():
    # 读取停用词
    read_stopword()
    #读取要分析的文档
    str = read_file()
    #进行分词处理
    s = txt_cut(str)
    # print(s[:15])
    #生成柱状图
    # Statistics(s)
    #生成词云
    wordcloud(s)

if __name__ == '__main__':
    main()


