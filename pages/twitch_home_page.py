from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    browse_icon = (By.XPATH, "//*[@id=\"root\"]/div[2]/a[2]/div/div[1]")
    search_input = (By.XPATH, "//*[@id='twilight-sticky-header-root']/div/div/div/div/input")
    result = (By.XPATH, "//*[@id='page-main-content-wrapper']/div/ul/li[1]/a/div/p")

    def open(self):
        self.driver.get("https://www.twitch.tv")

    def click_search(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.browse_icon)
        )
        self.click(self.browse_icon)

    def search(self, keyword, timeout=10):
        search_box = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.search_input)
        )
        search_box.clear()
        search_box.send_keys(keyword)

    def click_result(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.result)
        )
        self.click(self.result)


