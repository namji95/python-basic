print('\ntype 함수')
print('type(3) : ', type(3))
print('type(7.7) : ', type(7.7))
print("type('a') : ", type('a'))
print('type("A") : ', type("A"))

print('\n정수 int')
print('100000 : ', 100000)
print('100_000_000 : ', 100_000_000)

print('\n부동 소수점 float')
print('5 / 3 : ', 5 / 3)

print('\n복소수 complex')
'''
제곱하면 -1이 되는 수 i를 허수(imaginary number)라고 합니다.
i**2 == -1
파이썬에서 허수 i를 j로 나타냅니다.
복소수의 거듭제곱 (1 + i)**10을 손으로 계산하는 과정은
(1 + i)**2 = 1 + 2i + i**2
(1 + i)**10 = {(1 + i)**2}**5 = (2i)**5 = 2**5*i**5 = 32(i**2)**2i = 32i
'''
print('type(3 + 4j) : ', type(3 + 4j))
print((1 + 1j)**10)

print('\n문자열 str, 리스트 list, 튜플 tuple')
print('type("abcdefg") : ', type("abcdefg"))
print("type(['a', 'b', 'c']) : ", type(['a', 'b', 'c']))
print("type(('a', 'b', 'c')) : ", type(('a', 'b', 'c')))

print('\n매핑')
print("type({'one': 1, 'two': 2, 'three': 3}) : ", type({'one': 1, 'two': 2, 'three': 3}))

print('\n불')
print("type(True == 'True') : ", type(True == 'True'))
print("type(3 >= 1) : ", type(3 >= 1))
print("type(False) : ", type(False))

print('\n세트')
fruits = {'apple', 'banana', 'orange'}
print("type(fruits) : ", type(fruits))