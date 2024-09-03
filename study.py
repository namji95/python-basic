import re

from konlpy.tag import Okt

okt = Okt()

print('한국 소설 현진건의 운수 좋은 날에서 가장 많이 나온 단어 20개를 추출 후 이를 워드 클라우드로 만들어보기')
print('단, 의미없는 조사는 제외하는 전처리 작업도 수행해야 할 것')
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