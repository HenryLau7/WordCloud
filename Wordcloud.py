import wordcloud
import imageio
from wordcloud import ImageColorGenerator
text = open("hamlet.txt",encoding='utf-8')
txt = text.read()
mk = imageio.imread("caixukun.png")
w = wordcloud.WordCloud(mask=mk,background_color="white",scale=20)
w.generate(txt)
w.to_file('outputcai.png')
image_colors = ImageColorGenerator(mk)
w_color=w.recolor(color_func=image_colors)
w_color.to_file('caixukun_output.png')
