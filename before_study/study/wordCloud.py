import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

from before_study.study.study import TextCounter


class WordCloudExample:
    def __init__(self):
        self.text_top_count = []

    def text_count(self):
        text_counter = TextCounter(r"C:\WorkSpace\Python\python-basic\blog\운수좋은날.txt")
        self.text_top_count = text_counter.get_final_result()

    def word_cloud(self):
        imgArray = np.array(Image.open('C:/WorkSpace/Python/python-basic/image/heart.png'))
        wc = WordCloud(
            font_path="C:/WorkSpace/Python/LaundryGothic_OTF/런드리고딕OTF Bold.otf",
            background_color="white",
            mask=imgArray
        ).generate_from_frequencies(dict(self.text_top_count))

        plt.figure(figsize = (10,10))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.show()

if __name__ == '__main__':
    wordcloud = WordCloudExample()
    wordcloud.text_count()
    wordcloud.word_cloud()