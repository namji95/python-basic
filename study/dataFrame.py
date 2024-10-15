import pandas as pd

# pip install pandas를 입력하여 pandas 패키지 다운받기
# 데이터 프레임 생성 (list)
listFrame = pd.DataFrame([[1,2,3], [4,5,6],[7,8,9]])
print('--------------리스트 데이터 프레임--------------')
print(listFrame)

# 데이터 프레임 생성 (dictionary)
data = {
    'age' : [20, 30, 40],
    'height' : [160, 170, 180],
    'weight' : [60, 70, 80]
}
indexName = ['python', 'pandas', 'dataframe']

dictionaryFrame = pd.DataFrame(data, index=indexName)
print('\n--------------딕셔너리 데이터 프레임--------------')
print(dictionaryFrame)

# 데이터 프레임 조회
# 열(Column) 조회
print('\n--------------dictionary 열 조회--------------')
print('-------딕셔너리 열 조회 방법 1-------')
print(dictionaryFrame['age'])
print('-------딕셔너리 열 조회 방법 2-------')
print(dictionaryFrame.age)

# 특정 열 조회
print('\n--------------dictionary 특정 열 조회--------------')
print('-------딕셔너리 특정 열 조회 방법 1-------')
print(dictionaryFrame['height']['python'])
print('-------딕셔너리 특정 열 조회 방법 2-------')
print(dictionaryFrame.height['python'])

# 행(Row) 조회
print('\n--------------dictionary 행 조회--------------')
print('-------딕셔너리 행 조회 방법 1-------')
print(dictionaryFrame.loc[['python']])
print('-------딕셔너리 행 조회 방법 2-------')
print(dictionaryFrame.iloc[0])

# 데이터 프레임 수정
print('\n--------------딕셔너리 데이터 프레임 수정--------------')
frame_add_col = pd.DataFrame(dictionaryFrame, columns=['age', 'height', 'weight', 'num'])
print('\n--------------딕셔너리 데이터 프레임 열 추가--------------')
print(frame_add_col)

print('\n--------------추가된 열에 대한 값 추가--------------')
frame_add_col['num'] = [1, 2, 3]
print(frame_add_col)

print('\n--------------딕셔너리 데이터 프레임 행 추가--------------')
frame_add_index = frame_add_col.copy()
frame_add_index.loc['pycharm'] = [50, 190, 90, 4]
print(frame_add_index)

print('\n--------------딕셔너리 데이터 프레임 행, 열 삭제--------------')
print('원본 데이터 : ')
print(frame_add_index)
print('--------------열 삭제--------------')
frame_add_index.drop('num', axis=1, inplace=True)
print(frame_add_index)
print('--------------행 삭제--------------')
frame_add_index.drop('pycharm', axis=0, inplace=True)
print(frame_add_index)