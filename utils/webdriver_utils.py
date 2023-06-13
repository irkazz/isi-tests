from selenium import webdriver
import selenium.webdriver.support.wait


class WebDriverUtils:

    def get_wait(self, wait_time: int) -> selenium.webdriver.support.wait.WebDriverWait:
        return selenium.webdriver.support.wait.WebDriverWait(self.driver, wait_time)

    def create_driver(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
