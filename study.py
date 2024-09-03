# from konlpy.tag import Okt # 네 번째 풀이에서 사용
# from wordcloud import WordCloud, STOPWORDS # 네 번째 풀이에서 사용
# import matplotlib.pyplot as plt # 네 번째 풀이에서 사용

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

print('한국 소설 현진건의 운수 좋은 날에서 가장 많이 나온 단어 20개를 추출 후 이를 워드 클라우드로 만들어보기')
print('단, 의미없는 조사는 제외하는 전처리 작업도 수행해야 할 것')
okt = Okt()

# print('\n첫 번째 풀이')
# file = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8')
# str = file.read()
#
# replaceStr = str.replace('\n', '')
# splitStrs = replaceStr.split(' ')
#
# histogram = {}
# for splitStr in splitStrs:
#     histogram[splitStr] = histogram.get(splitStr, 0) + 1
#     print(histogram)

# print('\n두 번째 풀이')
# file = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8')
# lyrics = ''
#
# for line in file:
#     if line == '':
#         continue
#     line = line.replace('(', '').replace(')', '')
#     lyrics = lyrics + line
#
# lyrics = lyrics.split()
#
# counts =dict()
# for word in lyrics:
#     counts[word] = counts.get(word, 0) + 1
#
# counts_val_reverse = sorted(counts.items(),
#                             reverse=True,
#                             key=lambda item: item[1])
#
# num = 1
# for key, value in counts_val_reverse:
#     if num <= 20:
#         print(key, " : ", value)
#     else:
#         break
#     num += 1

# print('\n세 번째 풀이')
# file = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8')
# str = file.read()
#
# text_file = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "", str)
#
# text_file = okt.morphs(text_file, stem=False)
#
# stop_words= {'은', '는', '이', '가', '하', '아', '것', '들', '의', '있', '되', '수', '보', '주', '등', '한'}
# text_file = [token for token in text_file if not token in stop_words]
#
# text = ''
# for line in text_file:
#     text += line + ' '
#
# text = text.split()
#
# counts = dict()
# for word in text:
#     counts[word] = counts.get(word, 0) + 1
#
# counts_val_reverse = sorted(counts.items(),
#                             reverse=True,
#                             key=lambda item: item[1])
#
# num = 1
# for key, value in counts_val_reverse:
#     if num <= 20:
#         print(key, " : ", value)
#     else:
#         break
#     num += 1

# print('\n네 번째 풀이')
# file = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8')
# file_text = file.read()
#
# okt_file_text = okt.morphs(file_text, norm=True)
#
# oktTag = []
# for token in okt_file_text:
#     oktTag += okt.pos(token)
#
# file = open("C:\workSpace\불용어.txt", 'r', encoding='UTF-8')
# stopWords = file.read()
# stopWord = stopWords.split()
# stopPos = ['Suffix','Punctuation','Josa','Foreign','Alpha','Number']
#
# word = []
# for tag in oktTag:
#     if tag[1] not in stopPos:
#         if tag[0] not in stopWord:
#             word.append(tag[0])
#
# counts = dict()
# for text in word:
#     counts[text] = counts.get(text, 0) + 1
#
# counts_val_reverse = sorted(counts.items(),
#                             reverse=True,
#                             key=lambda item: item[1])
#
# num = 1
# text = ''
# for key, value in counts_val_reverse:
#     if num <= 20:
#         print(key, " : ", value)
#         word += key
#     else:
#         break
#     num += 1
#
# for text_word in word:
#     text += text_word + ' '
#
# # 워드 클라우드를 생성하며, 생성된 워드 클라우드를 myWC 이름의 변수에 저장하
# STOPWORDS.add(stopWords)
# myWC = WordCloud(font_path="C:/workSpace/NanumFontSetup_OTF_GOTHIC/NanumGothic.otf", max_words=20, background_color="white", stopwords=STOPWORDS).generate(text)
# # 워드 클라이드의 크기 정의
# plt.figure(figsize=(5, 5))
# plt.imshow(myWC)
# plt.axis('off')
# plt.show()

# print('\n다섯 번째 풀이')
# open으로 txt 파일을 열고 read()를 이용하여 읽습니다.
text = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8').read()

# okt 함수를 통해 읽어 들인 내용의 형태소를 분석합니다.
sentences_tag = []
sentences_tag = okt.pos(text)

noun_adj_list = []

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어줍니다.
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

# 가장 많이 나온 단어부터 40개를 저장합니다.
counts = Counter(noun_adj_list)
tags = counts.most_common(20)

for key, value in tags:
    print(key, ' : ', value)

# wordCloud를 생성합니다.
# 한글을 분석하기 위해 font를 한글로 지정해줘야 합니다.
wc = WordCloud(font_path="C:/workSpace/NanumFontSetup_OTF_GOTHIC/NanumGothicBold.otf", background_color="white")
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10, 10))
plt.axis('off')
plt.imshow(cloud)
plt.show()