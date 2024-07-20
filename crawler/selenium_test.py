# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
# from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

class SeleniumTest:
    def start_selenium(self):
        # 크롬드라이버 실행
        driver = webdriver.Chrome()

        # 크롬 드라이버에 url 주소 넣고 실행
        driver.get('https://www.google.co.kr/')

        # 페이지가 완전히 로딩되도록 3초동안 기다림
        time.sleep(3)

if __name__ == '__main__':
    selenium_test = SeleniumTest()
    selenium_test.start_selenium()


# todo: 파일 이름 또는 클래스 이름이 라이브러리 이름과 같을 경우 에러 발생 예약어 조심