from selenium import webdriver
from selenium.common import StaleElementReferenceException
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
click_time = start_time
current_time = start_time

while current_time - start_time <= 300:
    # クッキーをクリック
    cookie.click()

    # 現在タイムの取得
    current_time = time.time()

    # 5秒ごとに実行
    if current_time - click_time >= 5:

        # タイマーのリセット
        click_time = current_time

        money = driver.find_element(By.ID, "money")
        money_int = int(money.text.replace(",", ""))

        # Time Machineの価格取得
        time_machine_price = driver.find_element(By.CSS_SELECTOR, "#buyTime\\ machine > b")
        time_machine_price_int = int(time_machine_price.text.split()[3].replace(",", ""))
        if money_int > time_machine_price_int:
            time_machine_price = driver.find_element(By.CSS_SELECTOR, "#buyTime\\ machine > b")
            time_machine_price_int = int(time_machine_price.text.split()[3].replace(",", ""))
            buy_time_machine = driver.find_element(By.ID, "buyTime\\ machine")
            buy_time_machine.click()
            continue

        # Portalの価格取得
        portal_price = driver.find_element(By.CSS_SELECTOR, "#buyPortal > b")
        portal_price_int = int(portal_price.text.split()[2].replace(",", ""))
        if money_int > portal_price_int:
            buy_portal = driver.find_element(By.ID, "buyPortal")
            buy_portal.click()
            continue

        # Alchemyの価格取得
        alchemy_price = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\\ lab > b")
        alchemy_price_int = int(alchemy_price.text.split()[3].replace(",", ""))
        if money_int > alchemy_price_int:
            buy_alchemy = driver.find_element(By.ID, "buyAlchemy\\ lab")
            buy_alchemy.click()
            continue

        # Shipmentの価格取得
        shipment_price = driver.find_element(By.CSS_SELECTOR, "#buyShipment > b")
        shipment_price_int = int(shipment_price.text.split()[2].replace(",", ""))
        if money_int > shipment_price_int:
            buy_shipment = driver.find_element(By.ID, "buyShipment")
            buy_shipment.click()
            continue

        # Mineの価格取得
        mine_price = driver.find_element(By.CSS_SELECTOR, "#buyMine > b")
        mine_price_int = int(mine_price.text.split()[2].replace(",", ""))
        if money_int > mine_price_int:
            buy_mine = driver.find_element(By.ID, "buyMine")
            buy_mine.click()
            continue

        # Factoryの価格取得
        factory_price = driver.find_element(By.CSS_SELECTOR, "#buyFactory > b")
        factory_price_int = int(factory_price.text.split()[2].replace(",", ""))
        if money_int > factory_price_int:
            buy_factory = driver.find_element(By.ID, "buyFactory")
            buy_factory.click()
            continue

        # Grandmaの価格取得
        grandma_price = driver.find_element(By.CSS_SELECTOR, "#buyGrandma > b")
        grandma_price_int = int(grandma_price.text.split()[2].replace(",", ""))
        if money_int > grandma_price_int:
            buy_grandma = driver.find_element(By.ID, "buyGrandma")
            buy_grandma.click()
            continue

        # Cursorの価格取得
        cursor_price = driver.find_element(By.CSS_SELECTOR, "#buyCursor > b")
        cursor_price_int = int(cursor_price.text.split()[2].replace(",", ""))
        if money_int > cursor_price_int:
            buy_cursor = driver.find_element(By.ID, "buyCursor")
            buy_cursor.click()

cps = driver.find_element(By.ID, "cps")

print(f"cookies/second : {cps.text}")
