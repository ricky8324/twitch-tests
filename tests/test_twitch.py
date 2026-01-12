import pytest
from pages.twitch_home_page import HomePage
from pages.streamer_page import StreamerPage
from utils.webdriver import create_driver
from selenium.webdriver.common.by import By
import time
import random

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_open_streamer_and_take_screenshot(driver):
    home = HomePage(driver)
    streamer = StreamerPage(driver)

    home.open()
    home.click_search()
    home.search("StarCraft II")
    home.click_result()

    for _ in range(2):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    streamers = driver.find_elements(By.XPATH, "//*[@id='page-main-content-wrapper']/div/div/section[2]/div[2]/div[1]/button")
    if streamers:
        streamers[0].click()
    streamer.wait_until_loaded_and_screenshot("starcraft_streamer.png")
