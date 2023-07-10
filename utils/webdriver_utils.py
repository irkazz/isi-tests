import os

from selenium import webdriver
import selenium.webdriver.support.wait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverUtils:

    def __init__(self):
        self.driver = None

    def get_wait(self, wait_time: int) -> selenium.webdriver.support.wait.WebDriverWait:
        return selenium.webdriver.support.wait.WebDriverWait(self.driver, wait_time)

    def create_driver(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()

    def quit_driver(self):
        if self.driver:
            self.driver.quit()


