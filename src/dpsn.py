from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

import pyautogui

def click_with_retry(wait, driver, x_path):
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

    return clicked


def reservation(_ = None):
    driver = webdriver.Chrome()
    url = "https://www.dpsnnn.com/reserve"
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    while True:
        # select button
        clicked = click_with_retry(
            wait,
            driver,
            "/html/body/div[3]/main/div[1]/div[8]/div/div/div/div/div[2]/div/table/tbody/tr/td/div[1]/div/div/div/table/tbody/tr[5]/td[5]/div/div[3]/div[7]/a/div/div/span[1]"
        )

        if(clicked is True):
            break
        else:
            driver.refresh()

    pyautogui.alert("계속 하려면 클릭하세요")

if __name__ == "__main__":
    reservation()