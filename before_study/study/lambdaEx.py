'''
람다 형식은 인공지능 분야나 Auto CAD라는 설계 프로그램에서 쓰이는 Lisp 언어에서 물려받았다고 합니다.
함수를 한 줄만으로 만들게 해주는 역할을 합니다.
작성 방법은
lambda 매개변수 : 표현식
'''

# 일반 함수
print('\n람다 기본 표현식')
def hap(x, y):
    return x + y

print('함수 : ', hap(10 , 20))

# 람다
answer = (lambda x, y : x + y)(10, 20)
print('람다 : ', answer)

# map 함수
'''
map 함수는 함수와 리스트를인자로 받습니다.
리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음,
그 결과를 새로운 리스트에 담아줍니다.
작성 방법은
map(함수, 리스트)
'''
print('\nmap을 이용한 람다 표현식')
listMap1 = map(lambda x: x ** 2, range(5))
for i in listMap1:
    print(i, end=' ')

print()

listMap2 = list(map(lambda x: x ** 2, range(5)))
for i in listMap2:
    print(i, end=' ')

# reduce 함수
'''
reduce 함수는 각 원소들을 하나씩 꺼내 함수 로직에 맞게 적용시킵니다.
작성 방법은
reduce(함수, 시퀀스)
'''
print('\n\nreduce를 이용한 람다 표현식')
from functools import reduce
reduceLambda1 = reduce(lambda x, y : x + y, [0, 1, 2, 3, 4])
print(reduceLambda1)

print('역순 정렬')
reduceLambda2 = reduce(lambda x, y : x + y, ['abcde'])
splitLambda = list(reversed(reduceLambda2))
answer = reduce(lambda x, y : x + y, splitLambda)
print(answer)

# filter 함수
'''
리스트에 들어있는 원소들을 함수에 적용시켜서 
결과가 참인 값들로 새로운 리스트를 만들어줍니다.
작성 방법은
filter(함수, 리스트)
'''
print('\nfilter를 이용한 람다 표현식')
filterLambda1 = filter(lambda x : x < 5, range(11))
for i in filterLambda1:
    print(i, end=' ')

print()

filterLambda2 = list(filter(lambda x : x > 5, range(11)))
for i in filterLambda2:
    print(i, end=' ')

print()

filterLambda3 = filter(lambda x : x % 2, range(11))
for i in filterLambda3:
    print(i, end=' ')

print()

filterLambda4 = list(filter(lambda x : x % 2, range(11)))
for i in filterLambda4:
    print(i, end=' ')