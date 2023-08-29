import os

from selenium import webdriver
import selenium.webdriver.support.wait
from selenium.webdriver.chrome.service import Service


class WebDriverUtils:

    def __init__(self):
        self.driver = None

    def get_wait(self, wait_time: int) -> selenium.webdriver.support.wait.WebDriverWait:
        return selenium.webdriver.support.wait.WebDriverWait(self.driver, wait_time)

    def create_driver(self, browser="chrome"):
        if browser == "chrome":
            service = Service()
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

    def quit_driver(self):
        if self.driver:
            self.driver.quit()


