from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open('name.txt', 'r').read()

python_mask = np.array(PIL.Image.open("image.png"))


wc = WordCloud(
    stopwords=STOPWORDS,
    mask=python_mask,
    scale=1,
    background_color="black",  
    colormap="rainbow",
    contour_width=0,
    prefer_horizontal=0.5,
    min_font_size=1,
    max_font_size=250,
    mode="RGBA",
    max_words=100000
).generate(text)


plt.figure(figsize=(10, 10)) 
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") 
plt.tight_layout(pad=0)  
plt.show()