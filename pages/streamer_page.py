from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
import os

class StreamerPage(BasePage):
    streaming_video = (By.XPATH, "//video")

    def wait_until_loaded_and_screenshot(self, filename="streamer.png", timeout=60):

        video_element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.streaming_video)
        )

        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script(
                "return arguments[0].currentTime > 0;", video_element
            )
        )

        time.sleep(5)

        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"starcraft_streamer_{timestamp}.png"
        full_path = os.path.join(folder, filename)

        self.driver.save_screenshot(full_path)

 
