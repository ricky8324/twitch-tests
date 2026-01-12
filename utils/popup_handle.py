from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_possible_popup(driver):
    try:
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Accept') or contains(text(),'Start Watching')]")
            )
        )
        button.click()
    except:
        pass  # 沒 popup 直接忽略
