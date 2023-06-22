from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

import time


def click_with_retry(wait, x_path, max_retry=100, sleep_interval=0.1):
    retry_count = 0
    clicked = False
    while not clicked and retry_count < max_retry:
        try:
            theme_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, x_path)
                )
            )
            theme_button.click()
            clicked = True
        except StaleElementReferenceException as e:
            print("클릭할 엘리먼트를 찾을 수 없습니다.")
            retry_count += 1
            time.sleep(sleep_interval)  # 잠시 대기 후 다음 시도

def reservation(_):
    driver = webdriver.Chrome()
    url = "https://www.keyescape.co.kr/web/home.php?go=rev.make"
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    retry = 10

    # LOG_IN 2
    # LOG_IN 1
    # 메모리컴퍼니
    # 우주라이크
    # 강남 더오름
    # ...
    location = "메모리컴퍼니"
    click_with_retry(
        wait,
        f"//a[contains(@href, 'javascript:fun_zizum_select')]/li[text()='{location}']"
    )

    # select day
    tr_number = 6
    td_number = 4
    click_with_retry(
        wait,
        f"//*[@id='calendar_data']/table/tbody/tr[{tr_number}]/td[{td_number}]/a"
    )

    # select theme
    click_with_retry(
        wait,
        f"/html/body/div[3]/div/div/div/div/div[4]/dl[3]/dd/div/ul/a[2]/li"
    )

    # select time
    click_with_retry(
        wait,
        "//*[@id='theme_time_data']/li[9]"
    )

    while True:
        pass

if __name__ == "__main__":
    iteration = 4
    with Pool(iteration) as pool:
        pool.map(reservation, [_ for _ in range(iteration)])