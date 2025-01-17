from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

print('한국 소설 현진건의 운수 좋은 날에서 가장 많이 나온 단어 20개를 추출 후 이를 워드 클라우드로 만들어보기')
print('단, 의미없는 조사는 제외하는 전처리 작업도 수행해야 할 것')
okt = Okt()

class TextCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sentences_tag = []
        self.noun_adj_list = []
        self.tags = []

    # okt 기준 형태소 분리 함수
    def morpheme_separation_space(self):
        text = open(self.file_path, 'r', encoding='UTF-8').read()

        # okt 함수를 통해 읽어 들인 내용의 형태소를 분석합니다.
        self.sentences_tag.extend(okt.pos(text))

    # 명사와 형용사인 단어만 추출할 함수
    def morpheme_separation(self):
        # tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어줍니다.
        for word, tag in self.sentences_tag:
            if tag in ['Noun', 'Adjective']:
                self.noun_adj_list.append(word)
    
    # 가장 많이 나온 단어 20개 추출 함수
    def top_count(self):
        # 가장 많이 나온 단어부터 20개를 저장합니다.
        counts = Counter(self.noun_adj_list)
        self.tags.extend(counts.most_common(20))

        # for key, value in self.tags:
        #     print(key, ' : ', value)

        return self.tags
    
    # 워드 클라우드 호출 함수
    def word_cloud(self):
        # wordCloud를 생성합니다.
        # 한글을 분석하기 위해 font를 한글로 지정해줘야 합니다.
        wc = WordCloud(font_path="C:/workSpace/NanumFontSetup_OTF_GOTHIC/NanumGothicBold.otf", background_color="white")
        cloud = wc.generate_from_frequencies(dict(self.tags))

        plt.figure(figsize=(10, 10))
        plt.axis('off')
        plt.imshow(cloud)
        plt.show()
    
if __name__ == "__main__":
    text_class = TextCounter(r"C:\workSpace\운수좋은날.txt")
    text_class.morpheme_separation_space()
    text_class.morpheme_separation()
    tags = text_class.top_count()
    print(tags)
    text_class.word_cloud()