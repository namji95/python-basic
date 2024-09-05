from datetime import datetime, timedelta
import json
import requests

'''
End point = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
Encoding = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
Decoding = "SJpTwB+9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6/K4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ=="

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
params ={'serviceKey' : 'SJpTwB+9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6/K4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ==', 'pageNo' : '1', 'numOfRows' : '60', 'dataType' : 'xml', 'base_date' : '20240905', 'base_time' : '1000', 'nx' : '59', 'ny' : '125' }

response = requests.get(url, params=params)
print(response.content)
'''

# 설정 시간의 날씨 정보 모두 받아오기
rink = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
serviceKey = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
numOfRows = 100
pageNO = 1
dataType = 'json'
base_date = '20240905'
base_time = '1200'
nx = 59
ny = 125

url = f"{rink}?serviceKey={serviceKey}&numOfRows={numOfRows}&pageNo={pageNO}&dataType={dataType}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

response = requests.get(url)
res = json.loads(response.text)

# 받아온 날씨 정보를 원하는 형식으로 수정
# category를 한 줄로 취합하여 시간대 별로 분류
informations = dict()
for items in res['response']['body']['items']['item']:
    cate = items['category']
    fcstTime = items['fcstTime']
    fcstValue = items['fcstValue']
    temp = dict()
    temp[cate] = fcstValue
    
    if fcstTime not in informations.keys():
        informations[fcstTime] = dict()
    
    informations[fcstTime][cate] = fcstValue

# 시간대 별로 분류한 것들에 대한 방위 정보 담기
deg_code = {0 : 'N', 360 : 'N', 180 : 'S', 270 : 'W', 90 : 'E', 22.5 :'NNE',
           45 : 'NE', 67.5 : 'ENE', 112.5 : 'ESE', 135 : 'SE', 157.5 : 'SSE',
           202.5 : 'SSW', 225 : 'SW', 247.5 : 'WSW', 292.5 : 'WNW', 315 : 'NW',
           337.5 : 'NNW'}

def deg_to_dir(deg):
    close_dir = ''
    min_abs = 360
    if deg not in deg_code.keys():
        for key in deg_code.keys():
            if abs(key - deg) < min_abs:
                min_abs = abs(key - deg)
                close_dir = deg_code[key]
    else:
        close_dir = deg_code[deg]
    return close_dir

# category 값 커스텀
pty_code = {0 : '강수 없음', 1 : '비', 2 : '비/눈', 3 : '눈', 5 : '빗방울눈날림', 6 : '진눈깨비', 7 : '눈날림'}
sky_code = {1 : '맑음', 3 : '구름많음', 4 : '흐림'}

for key, val in zip(informations.keys(), informations.values()):
    template = f"""{base_date[:4]}년 {base_date[4:6]}월 {base_date[-2:]}일 {key[:2]}시 {key[2:]}분 {(int(nx), int(ny))} 지역의 날씨는 """
    
    # 하늘 상태 - 맑음(1), 구름많음(3), 흐림(4)
    if val['SKY']:
        sky_temp = sky_code[int(val['SKY'])]
        template += sky_temp + " | "
        
    # 강수 형태 - (초단기) 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울눈날림(5), 진눈깨비(6), 눈날림(7)
    if val['PTY']:
        pty_temp = pty_code[int(val['PTY'])]
        template += pty_temp + " | "
        
    # 1시간 강수량 (mm)
    if val['RN1']:
        rn1_temp = val['RN1']
        template += f"시간당 {rn1_temp} | "
            
    # 기온 (°C)
    if val['T1H']:
        t1h_temp = float(val['T1H'])
        template += f"기온 {t1h_temp}°C | "
        
    # 습도 (%)
    if val['REH']:
        reh_temp = float(val['REH'])
        template += f"습도 {reh_temp}% | "
        
    # 동서 바람 성분 (m/s)
    if val['UUU']:
        uuu_temp = float(val['UUU'])
        template += f"동서 바람 성분 {uuu_temp}m/s | "
        
    # 남북 바람 성분 (m/s)
    if val['VVV']:
        vvv_temp = float(val['VVV'])
        template += f"동서 바람 성분 {vvv_temp}m/s | "
    
    # 풍향 (deg)
    if val['VEC']:
        vec_temp = deg_to_dir(float(val['VEC']))
        template += f"풍향 {vec_temp} | "
    
    # 풍속 (m/s)
    if val['WSD']:
        wsd_temp = val['WSD']
        template += f"풍속 {wsd_temp}m/s | "
        
    # 낙뢰 (kA)
    if val['LGT']:
        lgt_temp = val['LGT']
        template += f"낙뢰 {lgt_temp}kA"
    
    print(template)