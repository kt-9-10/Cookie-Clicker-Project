from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

# タイマーの初期化
start_time = time.time()
check_time = time.time()

while time.time() - start_time <= 300:
    cookie.click()
    if time.time() - check_time > 10:
        add_ons_list = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
        add_ons_list[-1].click()
        check_time = time.time()

cps = driver.find_element(By.ID, "cps")
print(cps.text)