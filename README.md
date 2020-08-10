# Python词云入门——十行代码即可领取爱豆！

词云图大家应该不会陌生，即是由词汇组成类似云的彩色图形。

今天Henry带领大家一起学习用Python自带的词云库——wordcloud在十行代码内绘制出精美的词云图！

想要给自己的照片做词云吗？！！

那赶快进来学习吧！

#### 一、准备工作

首先是工具的准备

- 安装Python。安装地址：https://www.python.org/
- 安装Python的一些库：wordcloud, imageio

```python
pip install wordcloud
pip install imageio
```

然后是材料（照片）的准备

- 尽量选择像素高的照片。
- 对比度尽量高，不宜全身为同一种颜色。
- 尽量有一定的pose，肢体较为舒展。

最后是文案的准备

- 最好为英文，并且有足够多的单词。
- 词云默认出现次数越多，显示得就越大。
- Henry用的是哈姆雷特(Hamlet)剧本。



#### 二、开始制作

现在进行到我们的制作环节啦！进入到IDE（Henry用的是Pycharm）。

- 导入相关库

```python
import wordcloud   //词云库，提供了最主要的功能
import imageio     //进行图像的输入和输出
from wordcloud import ImageColorGenerator    //用来取色
```

- 打开我们要进行处理的图片文件和文案文件。//我这里以Kunkun的为例。

```python
text = open("hamlet.txt",encoding='utf-8')    //打开Hamlet文案
txt = text.read()         //读取文案，保存到变量txt中
mk = imageio.imread("caixukun.png")  //打开我们Kunkun的图片，保存到变量mk中
```

- 最关键的部分！生成词云！

```python
//第一行是建立一个词云变量，形状就是变量mk，背景选取白色，scale越高最后得到的越清晰，20就足够啦
w = wordcloud.WordCloud(mask=mk,background_color="white",scale=20)
//第二行便是用txt保存的文字来生成(generate)词云啦。
w.generate(txt)
```

- 将词云导出图片文件。

```python
w.to_file("caixukun_output.png") //导出png格式的词云图
```

于是我们可以在文件夹找到生成的图片文件

大概有了Kunkun的轮廓！但是！我们Kunkun明明是穿的粉丝的衣服，咋整成了这个sai儿？安排！

- 对词云进行重新填色

```python
image_colors = ImageColorGenerator(mk)       //取出原图中的颜色
w_color=w.recolor(color_func=image_colors)    //用原图中的颜色对词云进行重新填色
```

接着再生成文件，就有了我们文章顶部出现的样子啦！！

这就是本期的全部内容！用十行代码做出了精美的词云！你学会了吗？

没学会也没关系，所有的内容我都上传到了我的Github网站：https://github.com/HenryLau7/WordCloud/

欢迎大家随时学习！


注意注意！如果你不想学习呢？请关注本公众号「今天我秃了吗」，后台点击「词云」，按照提示即可获得精美的词云图！

还不快来尝试！

