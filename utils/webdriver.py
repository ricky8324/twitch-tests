from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    chrome_options = Options()

    mobile_emulation = {
        "deviceMetrics": {
            "width": 393,
            "height": 851,
            "pixelRatio": 3.0
        },
        "userAgent": (
            "Mozilla/5.0 (Linux; Android 13; Pixel 5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Mobile Safari/537.36"
        )
    }

    chrome_options.add_experimental_option(
        "mobileEmulation", mobile_emulation
    )

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    return driver
