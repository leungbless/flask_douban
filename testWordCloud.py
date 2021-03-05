import jieba  #导入中文的词云的组件（分词）
from matplotlib import pyplot as plt  #绘图工具，数据可视化
from wordcloud import WordCloud #导入词云
from PIL import Image #图像处理
import numpy as np  #矩阵运算
import sqlite3   #sqlite数据库



conn = sqlite3.connect("movies.db")
cur = conn.cursor()
sql = "select instroduction from movies250"

data = cur.execute(sql)
text = ""

for item in data:
    text = text + item[0]

cur.close()
conn.close()

#开始分词
cut = jieba.cut(text)
string = ' '.join(cut) #用空格把词拆出来，把对象变成字符串
#print(string)

img = Image.open(r'static/images/www1.jpg') #打开遮罩图片
img_arr = np.array(img)  #将图片转换为数组
wc = WordCloud(
    background_color = 'white',  #输出图片的背景色
    mask = img_arr,              #遮罩的文件
    font_path = "simfang.ttf"  #选择字体(C:\Windows\Fonts)
)
wc.generate_from_text(string) #从哪个文本(切好的词)生成WordCloud

#绘制图片
fig = plt.figure(1) #从第一个位置开始绘制
plt.imshow(wc)      #按照词云的规则显示图片
plt.axis('off')     #不显示坐标轴

#plt.show()  #显示生成图片(在程序里面显示，没有保存成一个文件)
plt.savefig(r'./word.jpg',dpi=450)   #将生成的图片保存起来(前面是保存的路径，dpi是清晰度)


