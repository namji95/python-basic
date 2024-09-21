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
        self.stop_word_list = []  # 불용어 리스트
        self.after_stop_word = []  # 불용어 제거된 결과

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

    # 따로 지정한 불용어 리스트 불러오기
    def stop_words_space(self):
        stop_words_list = open("C:/WorkSpace/Python/python-basic/blog/한국어_불용어.txt", 'r', encoding='UTF-8')
        # 텍스트 파일에 저장해둔 불용어 배열로 저장
        # 단어만 저장되도록 설정
        # self.stop_word_list = [word.strip() for word in stop_words_list]
        for word in stop_words_list:
            self.stop_word_list.append(word.strip())

    # 운수좋은날에서 불용어 제거
    def remove_stop_words(self):
        # 형태소 분리된 운수좋은날과 정리된 불용어를 사용하여
        # 운수좋은날에서 불용어 제거
        # self.after_stop_word = [word.strip() for word in self.sentences_tag if word not in self.stop_word_list]
        for word in self.sentences_tag:
            if word not in self.stop_word_list:
                self.after_stop_word.append(word.strip())

        return self.after_stop_word

if __name__ == '__main__':
    text_class = TextCounter(r"C:\WorkSpace\Python\python-basic\blog\운수좋은날.txt")
    text_class.morpheme_separation_space()
    text_class.stop_words_space()
    result = text_class.remove_stop_words()

    print(result)