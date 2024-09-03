print('한국 소설 현진건의 운수 좋은 날에서 가장 많이 나온 단어 20개를 추출 후 이를 워드 클라우드로 만들어보기')
print('단, 의미없는 조사는 제외하는 전처리 작업도 수행해야 할 것')
file = open("C:\workSpace\운수좋은날.txt", 'r', encoding='UTF-8')
str = file.read()

replaceStr = str.replace('\n', '')
splitStrs = replaceStr.split(' ')

histogram = {}
for splitStr in splitStrs:
    histogram[splitStr] = histogram.get(splitStr, 0) + 1
    print(histogram)