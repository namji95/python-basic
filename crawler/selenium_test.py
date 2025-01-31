from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumTest:
    def start_selenium(self):
        options = Options()
        options.add_argument("")
        options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)

        # DevTools로 탐지 방지
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.get('https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2')

        time.sleep(3)

        win_numbers = driver.find_element(By.CLASS_NAME, "num.win")

        print("win_numbers.text: ", win_numbers.text)

        time.sleep(3)

        bonus_number = driver.find_element(By.CLASS_NAME, "num.bonus")

        print("bonus_number.text: ", bonus_number.text)

        driver.quit()

if __name__ == '__main__':
    selenium_test = SeleniumTest()
    selenium_test.start_selenium()
