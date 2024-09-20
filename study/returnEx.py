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
'''
매개변수로 받은 정수를 한국어로 표기한 문자열을 반환하는 함수 korean_number()를 정의하세요. 
단, 매개변수는 1 이상 10 이하의 정수라고 가정합니다.
'''

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
'''
triple() 함수를 완성하세요.
'''
def triple(x):
    return x * 3
'''
오늘의 날짜 객체를 구하는 코드는 다음과 같습니다. 
(코드를 이해하지 못해도 이 문제를 풀 수 있습니다.)
'''
def korean_age(birth_year):
    today = datetime.today()
    return today.year - birth_year + 1

if __name__ == '__main__':
    print("triple(2):", triple(2))
    print("triple('x')", triple('x'))
    print("korean_age(2000):", korean_age(2000))

print('\n연습 문제 3')
'''
직장인 A씨는 1년 동안 열심히 일해서 연말에 성과급으로 천만 원을 받았습니다. 
연이율 3.875%(단리)인 고정금리 상품에 예금하려고 합니다. 5년 동안 넣어두면 이자가 얼마 붙는지 계산해 보겠습니다.

첫 해에 원금 10,000,000원에 대한 이자 10,000,000 * 0.03875 = 387500원이 붙습니다.
둘째 해에 원금 10,000,000원에 대한 이자 387500원이 붙습니다.
마찬가지로 셋째, 넷째, 다섯째 해에도 해마다 같은 금액의 이자가 붙습니다.

만기가 되어 받을 수 있는 이자는 다음과 같습니다.

>>> 10000000 * 0.03875 * 5
1937500.0
원금과 이자를 합한 총액, 즉 원리금은 다음과 같습니다.

>>> 10000000 + 10000000 * 0.03875 * 5
11937500.0

소수점 이하는 필요 없지만 지금은 그대로 둘게요.
원금(Principal), 이율(rate), 기간(time)이 주어졌을 때, 
이자(Interest)를 구하는 공식은 다음과 같습니다.
I = Prt
그리고 원리금(Amount)을 구하는 공식은 다음과 같습니다.
A = P(1 + rt)

문제 1
원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 이자를 구하는 함수 simple_interest()를 작성하세요.

예1
>>> simple_interest(10000000, 0.03875, 5)
1937500.0
예2
>>> simple_interest(1100000, 0.05, 5/12)
22916.666666666668

문제2
원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 원리금을 계산하는 함수 simple_interest_amount()를 작성하세요.

예1
>>> simple_interest_amount(10000000, 0.03875, 5)
11937500.0
예2
>>> simple_interest_amount(1100000, 0.05, 5/12)
1122916.6666666665
'''

'''
원금(Principal), 이율(rate), 기간(time)
이자(Interest)를 구하는 공식은 다음과 같습니다.
I = Prt
그리고 원리금(Amount)을 구하는 공식은 다음과 같습니다.
A = P(1 + rt)
'''
class SimpleInterest:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def simple_interest(self):
        return self.p * self.r * self.t
        
class SimpleInterestAmount():
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def simple_interest_amount(self):
        return self.p*(1 + self.r * self.t)

if __name__ == "__main__":
    print('문제 1')
    simpleInterest1 = SimpleInterest(10000000, 0.03875, 5)
    simpleInterest2 = SimpleInterest(1100000, 0.05, 5/12)
    print(simpleInterest1.simple_interest())
    print(simpleInterest2.simple_interest())

    print('문제 2')
    simpleInterestAmount1 = SimpleInterestAmount(10000000, 0.03875, 5)
    simpleInterestAmount2 = SimpleInterestAmount(1100000, 0.05, 5/12)
    print(simpleInterestAmount1.simple_interest_amount())
    print(simpleInterestAmount2.simple_interest_amount())

print('\n연습 문제 4')
'''
둘리와 도우너, 마이콜이 놀이 공원에 갔습니다. 
놀이 기구 중에는 탑승자의 키를 제한하는 것이 있네요.

문제
놀이 기구의 이름과 키 제한을 나타낸 문자열을 입력받아서, 
놀이 기구의 이름, 탑승 가능한 키의 하한(下限)과 상한(上限)을 각 행에 출력합니다.

def read(text):
    # 이곳에 코드를 작성하세요.
    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

입출력
예 1
입력: 
와일드 윙: 110cm 이상
출력:
이름: 와일드 윙
하한: 110
상한: None

예 2
입력:
툼 오브 호러: -
출력:
이름: 툼 오브 호러
하한: None
상한: None

예 3
입력:
플라이벤처: 140cm~195cm
출력:
이름: 플라이벤처
하한: 140
상한: 195

문자열의 split 메서드를 써서, 구분자(delimiter)를 기준으로 문자열을 분할할 수 있습니다. 다음 예에서는 콜론(:)을 구분자로 삼았습니다.
>>> hms = "13:48:03"
>>> hms.split(':')
['13', '48', '03']
str.strip으로 문자열 앞뒤의 공백을 제거할 수 있습니다.

>>> str.strip("  I am a boy. ")
'I am a boy.'
그리고 replace() 메서드를 이용해 문자열 일부를 다른 문자열로 바꾼 문자열을 얻을 수 있습니다.

>>> 'Python'.replace('P', 'J')
'Jython'
'''

def read(text):
    # 콜론을 기준으로 놀이기구 이름과 제한 조건을 분리합니다.
    ridename, restrictions = text.split(":")
    ridename = ridename.strip()  # 공백 제거
    restrictions = restrictions.strip()

    cmmin = cmmax = None  # 초깃값 설정

    # 제한 조건 분석
    if "~" in restrictions:
        parts = restrictions.split("~")
        cmmin = int(parts[0].replace("cm", "").strip())  # 하한 추출 및 변환
        cmmax = int(parts[1].replace("cm", "").strip())  # 상한 추출 및 변환
    else:
        if "이상" in restrictions:
            cmmin = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환
        elif "이하" in restrictions:
            cmmax = int(restrictions.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환

    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)