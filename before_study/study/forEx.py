print('직각삼각형 그리기\n')
leg = int(input('변의 길이: '))

for i in range(leg):
    print('* ' * (i + 1))

area = (leg ** 2) / 2
print('넓이: ', area)

print('\n활용 예제\n')
inputVal = int(input('입력: '))

answer = inputVal ** 2
print(answer)

print('\nfor문 사용법')
family = ['mother', 'father', 'gentleman', 'sexy lady']

for x in family:
    print(x, len(x))

print('for문에 range 사용해보기')
print(list(range(2, 7)))
a = [4, 5, 6, 7]
for i in a:
    print(i, end='')
print('')
for i in range(4, 8):
    print(i, end='')

print('\n입력 값 만큼 for문을 반복하면서 입력 값 출력')
num1 = int(input())
for i in range(num1):
    print(num1)

num2 = int(input())
for i in range(num2):
    print(i + 1, ' : ', (i + 1) ** 2)

print('\nfor문으로 활용한 연습 문제 1')
print('대학교의 화학자들은 상처를 매우 빠르게 치료하는 약물을 제조하는 새로운 과정을 개발했다. '
      '제조 과정은 매우 길고 화학 약품을 매번 모니터링해야 하므로 몇 시간씩 걸린다! '
      '학생들은 졸거나 딴짓을 하므로 이 일을 믿고 맏길 수가 없다. '
      '그러므로 약물의 제조를 모니터링하는 자동 장치를 프로그래밍해야 한다. '
      '장치는 15초마다 온도를 측정해 프로그램에 제공한다.'
      '프로그램은 먼저 최소와 최대의 안전 온도를 나타내는 두 개의 정수를 읽는다. '
      '그 다음에, 장치가 제공하는 온도(정수)를 계속 읽는다. '
      '화학 반응이 완료되면 장치는 끝을 알리는 -999를 보낸다. '
      '기록된 온도가 올바른 범위에 있을 경우(최솟값 또는 최댓값과 같아도 된다) '
      'Nothing to report를 표시해야 한다. '
      '하지만 온도가 위험 수준에 도달하면 Alert!를 표시하고 온도 측정을 중단한다(장치가 온도값을 계속 보내더라도).')
# L = input().split()
# mini = int(L[0])
# maxi = int(L[1])
# # mini, maxi = map(int, input().split())
#
# temp = int(input())
#
# while temp != -999:
#     if mini <= temp <= maxi:
#         print('Nothing to report')
#         temp = int(input())
#     else:
#         print('Alert!')
#         break

print('\nfor-else와 while-else')
for i in [1, 2, 3, 4]:
    print(i)
else:
    print("리스트의 원소를 모두 출력했어요")

print('\n위 예시로 보면 else문의 print는 for문 뒤에 오도록 하면 될 것 같지만 다음과 같은 예시의 경우 필요합니다.')
for i in [1, 2, 3, 4]:
    if i % 3:
        print(i) # i가 3의 배수가 아니면 출력
    else:
        break # i가 3의 배수이면 반복문에서 빠져나감
else:
    print("리스트의 원소를 모두 출력했어요")

print('\nwhile-else')
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == 'break':
        break
else:
    print('발사!')
