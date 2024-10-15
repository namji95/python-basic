from datetime import datetime, timedelta
import json
import requests

class OpenApiWeather:
    def __init__(self):
        self.res = []
        self.informations = dict()
        self.dataType = ''
        self.nx = 0
        self.ny = 0
        self.pty_code = {0: '강수 없음', 1: '비', 2: '비/눈', 3: '눈', 5: '빗방울눈날림', 6: '진눈깨비', 7: '눈날림'}
        self.sky_code = {1: '맑음', 3: '구름많음', 4: '흐림'}
        self.temp = []

    # 날씨 정보 가져오기
    def weather_response(self):
        rink = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
        serviceKey = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
        numOfRows = 60
        pageNO = 1
        dataType = 'json'
        self.base_date = datetime.now().strftime('%Y%m%d')
        base_time = (datetime.now() - timedelta(hours=1)).strftime('%H%M')
        self.nx = 59
        self.ny = 125

        url = f"{rink}?serviceKey={serviceKey}&numOfRows={numOfRows}&pageNo={pageNO}&dataType={dataType}&base_date={self.base_date}&base_time={base_time}&nx={self.nx}&ny={self.ny}"

        response = requests.get(url)
        self.res = json.loads(response.text)

    # 받아온 날씨 정보 시간별로 분류
    def classification_by_time(self):
        for items in self.res['response']['body']['items']['item']:
            category = items['category']
            fcstTime = items['fcstTime']
            fcstValue = items['fcstValue']
            temp = dict()
            temp[category] = fcstValue

            if fcstTime not in self.informations.keys():
                self.informations[fcstTime] = dict()

            self.informations[fcstTime][category] = fcstValue

    def deg_to_dir(self, deg):
        deg_code = {0: 'N', 360: 'N', 180: 'S', 270: 'W', 90: 'E', 22.5: 'NNE', 45: 'NE',
                    67.5: 'ENE', 112.5: 'ESE', 135: 'SE', 157.5: 'SSE', 202.5: 'SSW',
                    225: 'SW', 247.5: 'WSW', 292.5: 'WNW', 315: 'NW', 337.5: 'NNW'}
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

    def weather_open_api(self):
        for key, val in zip(self.informations.keys(), self.informations.values()):
            # 날씨 정보를 담을 딕셔너리 초기화
            weather_entry = {
                "날짜 및 시간": f"{self.base_date[:4]}년 {self.base_date[4:6]}월 {self.base_date[-2:]}일 {key[:2]}시 {key[2:]}분",
                "지역 좌표": (int(self.nx), int(self.ny)),
                "날씨 정보": "",
                "강수": "",
                "시간당 강수": "",
                "기온": "",
                "습도": "",
                "동서 바람": "",
                "남북 바람": "",
                "풍향": "",
                "풍속": "",
                "낙뢰": ""
            }

            # 날씨 정보
            if val['SKY']:
                sky_temp = self.sky_code[int(val['SKY'])]
                weather_entry["날씨 정보"] = sky_temp

            # 강수
            if val['PTY']:
                pty_temp = self.pty_code[int(val['PTY'])]
                weather_entry["강수"] = pty_temp

            # 시간당 강수
            if val['RN1']:
                rn1_temp = val['RN1']
                weather_entry["시간당 강수"] = f"시간당 {rn1_temp}"

            # 기온
            if val['T1H']:
                t1h_temp = float(val['T1H'])
                weather_entry["기온"] = f"기온 {t1h_temp}°C"

            # 습도
            if val['REH']:
                reh_temp = float(val['REH'])
                weather_entry["습도"] = f"습도 {reh_temp}%"

            # 동서 바람
            if val['UUU']:
                uuu_temp = float(val['UUU'])
                weather_entry["동서 바람"] = f"동서 바람 성분 {uuu_temp}m/s"

            # 남북 바람
            if val['VVV']:
                vvv_temp = float(val['VVV'])
                weather_entry["남북 바람"] = f"남북 바람 성분 {vvv_temp}m/s"

            # 풍향
            if val['VEC']:
                vec_temp = self.deg_to_dir(float(val['VEC']))
                weather_entry["풍향"] = f"풍향 {vec_temp}"

            # 풍속
            if val['WSD']:
                wsd_temp = val['WSD']
                weather_entry["풍속"] = f"풍속 {wsd_temp}m/s"

            # 낙뢰
            if val['LGT']:
                lgt_temp = val['LGT']
                weather_entry["낙뢰"] = f"낙뢰 {lgt_temp}kA"

                self.temp.append(weather_entry)

        return self.temp
            
if __name__ == "__main__":
    weather_class = OpenApiWeather()
    weather_class.weather_response()
    weather_class.classification_by_time()
    temp = weather_class.weather_open_api()
    print(temp)