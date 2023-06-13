from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    BASE_URL = "https://test.isi-technology.com/#!/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: object) -> WebElement:
        return self.driver.find_element(*locator)

    def wait_for_element_present(self, locator: (By, str)) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator: (By, str)) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))
