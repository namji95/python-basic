import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumTest:
    def start_selenium(self):
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)

        # DevTools로 탐지 방지
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.get('https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2')

        time.sleep(3)

        # 부모 div 요소를 기준으로 내부 span 태그 모두 찾기
        span_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'num win')]//span"))
        )

        number_list = []

        for idx, element in enumerate(span_elements):
            number_list.append({f"{idx+1}번 볼": element.text})

        time.sleep(2)

        # 부모 div 요소를 기준으로 내부 span 태그 모두 찾기
        span_element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'num bonus')]//span"))
        )
        
        for idx, element in enumerate(span_element):
            number_list.append({"bonus 볼": element.text})

        print(number_list)

        driver.quit()

if __name__ == '__main__':
    selenium_test = SeleniumTest()
    selenium_test.start_selenium()
