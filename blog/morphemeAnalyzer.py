from konlpy.tag import Kkma, Komoran, Okt, Hannanum

kkma = Kkma()
komoran = Komoran()
okt = Okt()
hannanum = Hannanum()

text = ('어느 화창한 봄날, 푸른 하늘 아래서 사람들이 각자 목적지를 향해 빠르게 걸어가고 있을 때, '
        '나는 문득 멀리서 들려오는 새들의 노랫소리를 들으며 기분 좋은 미소를 지었다!')

# 각 품사를 태깅
kkma.pos(text)          # 텍스트의 형태소를 분석하여, 형태소와 품사 태그를 튜플로 반환
komoran.pos(text)       # 텍스트의 형태소를 분석하여, 형태소와 품사 태그를 튜플로 반환
okt.pos(text)           # 텍스트의 형태소를 분석하여, 형태소와 품사 태그를 튜플로 반환
hannanum.pos(text)      # 텍스트의 형태소를 분석하여, 형태소와 품사 태그를 튜플로 반환

# 명사 추출
kkma.nouns(text)        # 텍스트에서 명사만을 추출하여 리스트로 반환
komoran.nouns(text)     # 텍스트에서 명사만을 추출하여 리스트로 반환
okt.nouns(text)         # 텍스트에서 명사만을 추출하여 리스트로 반환
hannanum.nouns(text)    # 텍스트에서 명사만을 추출하여 리스트로 반환

# 텍스트만 형태소 분리
kkma.morphs(text)       # 텍스트를 형태소 단위로 분리하여 리스트로 반환
komoran.morphs(text)    # 텍스트를 형태소 단위로 분리하여 리스트로 반환
okt.morphs(text)        # 텍스트를 형태소 단위로 분리하여 리스트로 반환
hannanum.morphs(text)   # 텍스트를 형태소 단위로 분리하여 리스트로 반환

# text 그대로 출력
kkma.sentences(text)    # 텍스트를 문장 단위로 분리해 리스트로 반환
okt.normalize(text)     # 텍스트를 정규화하여 통일된 표현 형식으로 변환

# hannanum
hannanum.analyze(text)  # 텍스트를 분석하여 여러 해석 결과를 반환

# 어절 추출
okt.phrases(text)       # 텍스트에서 어절(구)을 추출하여 리스트로 반환