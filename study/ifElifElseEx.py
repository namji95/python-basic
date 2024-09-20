print('if-else문 예시')
a = 1234 * 4
b = 13456 / 2
if a > b:
    print('a')
else:
    print('b')

print('\nif-elif-else 예시')
c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else:
    print('I don\'t know')

print('\n나머지 계산을 이용하는 if 문')
a = 48
b = 4
if a % b == 0:
    print(f'{a}는 {b}로 나누어 떨어집니다.')
elif a % b != 0:
    print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')

print('\n조건에 따라 반복문 중단하기')
max = 10

while True:
    num1 = int(input())
    if num1 > max:
        print(num1, 'is too big')
        break

print('\nif문 연습 문제 1')
while True:
    num2 = int(input())
    if num2 == 1:
        print('일')
        break
    elif num2 == 2:
        print('이')
        break
    elif num2 == 3:
        print('삼')
        break

print('\nif문 연습 문제 2')
while True:
    print('What year were you born? ')
    num3 = int(input())
    if num3 <= 1924:
        print('가장 위대한 세대(The Greatest Generation)')
        break
    elif num3 <= 1945:
        print('침묵 세대(The Silent Generation)')
        break
    elif num3 <= 1964:
        print('베이비붐 세대(baby boomer)')
        break
    elif num3 <= 1980:
        print('X 세대(Generation X')
        break
    elif num3 <= 1996:
        print('밀레니얼(millennial)')
        break
    else:
        print('Z 세대(Generation Z)')
        break

print('\nif문 연습 문제 3')
print('길이, 부피, 무게나 금액을 표기할 때 1000을 k로 표기하곤 합니다.'
      '예를 들어 3000m는 3km로 표기하는 것이 일반적입니다.'
      '다음은 입력받은 숫자가 1000보다 크면'
      '1자리부터 100자리까지의 숫자를 생략하고 k를 붙여주는 코드입니다.')
num = int(input())
result = ''

if num >= 1000:
    result = str(num // 1000) + 'K'
elif num >= 0:
    pass
print(result)

print('문제는 백만 이상의 숫자를 입력 받았을 때'
      '1 ~ 10만자리 숫자를 생력하고'
      'M을 붙여 출력하는 코드를 만들기 입니다.')
num4 = int(input())
result1 = ''
if num4 >= 1000000000:
    result1 = str(num4 // 1000000000) + 'G'
elif num4 >= 1000000:
    result1 = str(num4 // 1000000) + 'M'

print(result1)

print('\nif문 연습 문제 4')
print('input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가,'
      '음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 스크립트 작성')
result2 = 0
while True:
    num5 = int(input())
    if num5 >= 0:
        result2 += num5
    else:
        break

print(result2)

print('\nif문 연습 문제 5')
print('윤년은 역볍을 실제 태양년에 맞추기 위해 어분의 하루 또는 월을 끼우는 해입니다.'
      '현재 사용하는 그레고리력의 윤년 규칙은 다음과 같습니다.')
print('서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다.'
      '서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다.'
      '서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다.')

is_leap_year = None

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

print('\nif문 and / or 사용')
s = 'banana'
if 'a' in s:
    if 'b' in 'banana':
        print('banana에는 a도 있고 b도 있어요!')

if 'a' in s and 'b' in s:
    print('banana에는 a도 있고 b도 있어요!')

