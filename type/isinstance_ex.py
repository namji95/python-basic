# isinstance 예제
print(f"isinstance 문자열 체크 예제")
data_str = "문자열 체크 테스트"
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance str로 설정 결과: {isinstance(data_str, str)}")
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance int로 설정 결과: {isinstance(data_str, int)}")

data_int = 123
print(f"({data_int}) 데이터가 {type(data_int)}일 때 isinstance str로 설정 결과: {isinstance(data_int, int)}")
print(f"({data_int}) 데이터가 {type(data_int)}일 때 isinstance int로 설정 결과: {isinstance(data_int, str)}")