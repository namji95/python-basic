import re
from collections import Counter
from konlpy.tag import Okt

print('한국 소설 현진건의 운수 좋은 날에서 가장 많이 나온 단어 20개 추출')
print('불용어 제거하는 전처리 작업도 수행')

class TextCounter:
    def __init__(self, file_path):
        self.okt = Okt()
        self.file_path = file_path
        self.sentences_tag = [] # 형태소 분석 결과

    # okt 기준 형태소 분리
    def morpheme_separation_space(self):
        text = open(self.file_path, 'r', encoding='UTF-8').read()
        text = re.sub(r'[^\w\s]', '', text)
        # okt 함수를 통해 읽어 들인 내용의 형태소를 분석
        # 단어만 저장할 수 있도록 설정
        # self.sentences_tag = [word for word in self.okt.morphs(text) if word.strip() != '']
        for word in self.okt.morphs(text):
            if word.strip() != '':
                self.sentences_tag.append(word)

        return self.sentences_tag

if __name__ == '__main__':
    text_class = TextCounter(r"C:\WorkSpace\Python\python-basic\blog\운수좋은날.txt")
    result = text_class.morpheme_separation_space()

    print(result)