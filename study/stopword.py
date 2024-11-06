from konlpy.tag import Okt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''
pip install nltk
pip install konlpy
위 두 명령어로 각 라이브러리 다운받아야 합니다.

nltk.download('punkt')      # 토큰화
nltk.download('punkt_tab')
nltk.download('stopwords')  # 불용어 목록
nltk.download('wordnet')    # WordNet 사전

'''

stop_words_list = stopwords.words('english')
print('영어 불용어 개수 : ', len(stop_words_list))
words = dict()
for word in stop_words_list:
    words[word] = words.get(word, 0) + 1

print('영어 불용어 종류 : ', words)

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example)

result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)

print('불용어 제거 전 : ', word_tokens)
print('불용어 제거 후 : ', result)

okt = Okt()
example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

stop_words = set(stop_words.split(' '))
word_tokens = okt.morphs(example)

result = [word for word in word_tokens if not word in stop_words]

print('불용어 제거 전 : ', word_tokens)
print('불용어 제거 후 : ', result)