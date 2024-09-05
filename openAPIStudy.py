from datetime import datetime, timedelta
import json
import requests

'''
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084
여기서 OpenAPI까지 발급
API 활용하여 날씨 정보 받아오는 방법 찾아보고 실습해보기
End point = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
Encoding = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
Decoding = "SJpTwB+9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6/K4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ=="
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'"
'''

# url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# params ={'serviceKey' : 'SJpTwB+9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6/K4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ==', 'pageNo' : '1', 'numOfRows' : '60', 'dataType' : 'xml', 'base_date' : '20240905', 'base_time' : '1000', 'nx' : '59', 'ny' : '125' }

# response = requests.get(url, params=params)
# print(response.content)

# input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
# print('datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1) : ', input_d, " : ", type(input_d))

# input_datetime = datetime.strftime(input_d, "%Y%m%d%H%M")
# input_date = input_datetime[:-4]
# input_time = input_datetime[-4:]
# print('datetime.strftime(input_d, "%Y%m%d%H%M") : ', input_datetime, ' : ', type(input_datetime))
# print("input_datetime[:-4] : ", input_date, ' : ', type(input_date))
# print("input_datetime[-4:] : ", input_time, ' : ', type(input_time))

serviceKey = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
numOfRows = 60
pageNO = 1
dataType = 'json'
base_date = '20240905'
base_time = '1000'
nx = 59
ny = 125

url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={serviceKey}&numOfRows={numOfRows}&pageNo={pageNO}&dataType={dataType}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

response = requests.get(url, verify=True)
res = json.loads(response.text)
print(res)