from datetime import datetime

def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y

c = f1(10)
print(c)

def f2(x):
    a = 3
    b = 5
    y = a * x + b
    print(y)

d = f2(10)
print(d)

if 1 + 1 == 2:
    print('yes')
else:
    print('no')

def quiz():
    ans = input('1 + 2 = ')
    return 1 + 2 == int(ans)

print(quiz())

print('\n연습 문제 1')
print('매개변수로 받은 정수를 한국어로 표기한 문자열을 반환하는 함수 korean_number()를 정의하세요. 단, 매개변수는 1 이상 10 이하의 정수라고 가정합니다.')

def korean_number(num):
    if num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'
    elif num == 10:
        return '십'

print(korean_number(int(input())))

print('\n연습 문제 2')
print('triple() 함수를 완성하세요.')
def triple(x):
    return x * 3
print('오늘의 날짜 객체를 구하는 코드는 다음과 같습니다. (코드를 이해하지 못해도 이 문제를 풀 수 있습니다.)')
def korean_age(birth_year):
    today = datetime.today()
    return today.year - birth_year + 1

if __name__ == '__main__':
    print("triple(2):", triple(2))
    print("triple('x')", triple('x'))
    print("korean_age(2000):", korean_age(2000))