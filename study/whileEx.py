print('1 ~ 5 출력하는 방법')
print('print 메서드를 사용하여 1 ~ 5까지 모두 입력하는 방법도 있지만')

num = 1
while num <= 5: # num이 11이 되기 전까지 반복
    print(num) # num의 값을 출력
    num = num + 1 # num 값에 1씩 증가할 수 있도록 설정

print('이렇게 while문을 사용하면 쉽게 1 ~ 10까지 출력할 수 있습니다.')

print('\n입력 값 만큼 while문 반복하면서 입력 값 출력해보기')
num1 = input()
numVal = 1
print('입력 값 ', num1)
while numVal <= int(num1):
    print(num1)
    numVal += 1

num2 = input()
numVal = 1
print('입력 값 ', num2)
while numVal <= int(num2):
    print(num2)
    numVal += 1

print('\n입력 값 만큼 while문 반복하면서 순회하고 있는 값 제곱하여 출력해보기')
numVal = 1
print('입력 값 ', num1)
while numVal <= int(num1):
    answer = numVal
    print(numVal, ' ', answer ** 2)
    numVal += 1

numVal = 1
print('입력 값 ', num2)
while numVal <= int(num2):
    answer = numVal
    print(numVal, ' ', answer ** 2)
    numVal += 1

print('\nwhile문을 이용한 연습 문제')
print('문제: 고무 공을 100 미터 높이에서 떨어뜨리는데, '
      '이 공은 땅에 닿을 때마다 원래 높이의 3 / 5 만큼 튀어오릅니다.'
      '공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.')
answer = 100
height = 3 / 5
num = 1
while num <= 10:
    answer = answer * height
    print(num, ' ', answer)
    num += 1

print('\n라운드 함수를 이용하여 소수점 아래 네 자리까지 출력해 보겠습니다.')
answer = 100
height = 3 / 5
num = 1
while num <= 10:
    answer = answer * height
    print(num, ' ', round(answer, 4))
    num += 1