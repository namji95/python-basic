from datetime import datetime, timedelta
import json
import requests

class OpenApiWeather:
    def __init__(self):
        self.res = []
        self.informations = dict()
    
    # 날씨 정보 가져오기    
    def weather_response(self):
        rink = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
        serviceKey = "SJpTwB%2B9NLadh2zz0JcxICsLgq3BYrPpGHh9M9cLDuWS4ifD3Z6%2FK4eyHmegOkiMGXVYB5TpJ0QKkoThu410hQ%3D%3D"
        numOfRows = 60
        pageNO = 1
        dataType = 'json'
        base_date = '20240905'
        base_time = '1200'
        nx = 59
        ny = 125

        url = f"{rink}?serviceKey={serviceKey}&numOfRows={numOfRows}&pageNo={pageNO}&dataType={dataType}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
        
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
            
if __name__ == "__main__":
    weather_class = OpenApiWeather()
    weather_class.weather_response()
    weather_class.classification_by_time()