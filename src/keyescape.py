from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

import time
import pyautogui

def click_with_retry(wait, x_path):
    clicked = False
    try:
        theme_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, x_path)
            )
        )
        theme_button.click()
        if theme_button.get_attribute("class") == "on":
            clicked = True
    except StaleElementReferenceException as e:
        print("클릭할 엘리먼트를 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(e)
        return False
    return clicked

def reservation(_=None):
    driver = webdriver.Chrome()
    url = "https://www.keyescape.co.kr/web/home.php?go=rev.make"
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    while True:
        # LOG_IN 2
        # LOG_IN 1
        # 메모리컴퍼니
        # 우주라이크
        # 강남 더오름
        # ...
        location = "메모리컴퍼니"
        clicked = click_with_retry(
            wait,
            f"//a[contains(@href, 'javascript:fun_zizum_select')]/li[text()='{location}']"
        )
        if(clicked is False):
            driver.refresh
            continue

        # select day
        tr_number = 6
        td_number = 4
        click_with_retry(
            wait,
            f"//*[@id='calendar_data']/table/tbody/tr[{tr_number}]/td[{td_number}]/a"
        )
        if(clicked is False):
            driver.refresh
            continue

        # select theme
        click_with_retry(
            wait,
            f"/html/body/div[3]/div/div/div/div/div[4]/dl[3]/dd/div/ul/a[2]/li"
        )
        if(clicked is False):
            driver.refresh
            continue

        # select time
        click_with_retry(
            wait,
            "//*[@id='theme_time_data']/li[9]"
        )
        if(clicked is False):
            driver.refresh
            continue

        # 신청
        click_with_retry(
            wait,
            "/html/body/div[3]/div/div/div/div/form/div/a[1]"
        )
        if(clicked is False):
            driver.refresh
            continue

        break

    pyautogui.alert("계속 하려면 클릭하세요")

    while True:
        pass

if __name__ == "__main__":
    reservation()
