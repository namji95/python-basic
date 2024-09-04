print('\n문자열 인덱스 호출 방법 문자열 뒤에 [인덱스 번호] 이렇게 이용하면 됩니다.')
x = 'python'
print("x[0] : ", x[0])
print("x[0:4] : ", x[0:4])
print("x[:4] : ", x[:4])
print("x[4:] : ", x[4:])

print('\n문자열 인덱스를 이용한 문자 수정')
print("x[0] = 'b' 이렇게 작성하면 TypeError: 'str' object does not support item assignment 이런 에러가 발생합니다.")
x = 'b' + x[1:]
print("x = 'b' + x[1:] 이렇게 사용할 수 있습니다. "
      "하지만 이 형태는 문자열의 p를 b로 바꾼 것이 아닌 "
      "b와 p이후 문자열인 ython을 합친 새로운 문자열인 것입니다.")
print(x)

print('\n문자열의 원하는 문자가 어디 있는지 확인하는 방법 => find 함수 이용')
s = 'hello python'
print("s.find('p') : ", s.find('p'))
print("\n인덱스를 이용해 원래 존재하는 문자열을 다른 문자열 변수에 저장하여 활용할 수도 있습니다.")
h = s[0:6]
print("h = s[0:6] : ", h)
print('\n위 h 변수의 끝에는 공백이 포함되었는데, 다음과 같이 슬라이싱을 하거나 rstrip()으로 제거할 수 있습니다.')
print("split 함수를 사용하면 문자열을 분할하는 것도 가능합니다.")
splitStr = s.split()
print("s.split() : ", splitStr)
print("\n분할된 문자열도 인덱스를 이용하여 원하는 문자열만 추출할 수 있습니다.")
print("splitStr[1] : ", splitStr[1])

print("\n 리스트 활용")
ls = [3, 2, 1, 4]
ls.append(5)
print("append() 함수 이용하여 원소 추가 - ls.append(5) : ", ls)
ls.sort()
print("sort() 함수 이용하여 정렬 - ls.sort() : ", ls)
del ls[4]
print("del 이용하여 원소 삭제 - del ls[4] : ", ls)
d = ls.pop()
print("pop 함수 이용하여 원소 삭제, pop 함수는 삭제된 원소를 반환도 해주기 때문에 변수에 저장했다 다시 사용할 수 있습니다.")
print("d = ls.pop() : ", ls)
print("d = ls.pop() : ", d)
ls[2] = 30
print("배열 인덱스를 이용하여 원소 값도 수정할 수 있습니다. - ls[2] = 30 : ", ls)
print("리스트에 리스트를 넣어 작성할 수도 있습니다.")
twoList = ['1', ['2', '3', '4'], '5']
print("twoList = ['1', ['2', '3', '4'], '5'] : ", twoList)
print("2차원 배열 인덱스를 이용한 원소 추출")
print("['1', ['2', '3', '4'], '5'] 해당 배열은 인덱스 1번에 3개의 원소를 갖고 있다는 의미입니다. 그래서 원소를 꺼낼 때에는 배열이름[1][0] 이런식으로 꺼낼 수 있습니다.")
print("twoList[2] : ", twoList[2])
print("twoList[1][0] : ", twoList[1][0])
print("리스트 원소합")
one_to_ten = list(range(1, 11))
print("one_to_ten = list(range(1, 11)) : ", one_to_ten)

print("\n 문자열을 문자열 리스트로 바꿔보기")
print("for문 이용")
character = []
s = 'hello python'
for char in s:
    character.append(char)
    
print("for문 이용 : ", character)
print("list 함수 이용")
print("list(s) : ", list(s))

print("\nint 함수와 str 함수를 이용한 형변환")
num = 123
s = "123"
print("int(s) : ", int(s))
print("str(num) : ", str(num))
intStr = int(s)
print("intNum = int(s) : ", intStr)
print("type(intNum) : ", type(intStr))
strNum = str(num)
print("strNum = str(num) : ", strNum)
print("type(strNum) : ", type(strNum))
floatStr = float(s)
print("floatStr = float(s) : ", floatStr)
print("type(floatStr) : ", type(floatStr))