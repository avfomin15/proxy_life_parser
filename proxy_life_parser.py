import os
import time
import re
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


load_dotenv()


URL_MAIN = 'https://proxy6.net/'
URL_USER = 'https://proxy6.net/user/proxy'
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def get_source_html(url):
    service = Service(executable_path='chromedriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    try:
        driver.get(url=URL_MAIN)
        time.sleep(3)

        login_button = driver.find_element(By.LINK_TEXT, 'Войти')
        login_button.click()
        time.sleep(5)

        driver.find_element(By.NAME, 'email').send_keys(LOGIN)
        driver.find_element(By.NAME, 'password').send_keys(PASSWORD)

        WebDriverWait(driver, 120).until(EC.url_contains('user'))
        driver.get(url=URL_USER)
        time.sleep(3)

        result_ip = []
        result_data = []
        data_class = driver.find_elements(
            By.CSS_SELECTOR, '.list-dotted.user_list_dotted'
            )

        ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}')
        data_pattern = re.compile(r'\d{2}\.\d{2}\.\d{2}, \d{2}:\d{2}')

        for tags in data_class:
            raw_text = tags.text

            date_matches = data_pattern.findall(raw_text)
            ip_matches = ip_pattern.findall(raw_text)

            result_data.extend(date_matches)
            result_ip.extend(ip_matches)

        for i in range(len(result_data)):
            print(f'{result_ip[i]} - {result_data[i]}')

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(URL_MAIN)


if __name__ == '__main__':
    main()
