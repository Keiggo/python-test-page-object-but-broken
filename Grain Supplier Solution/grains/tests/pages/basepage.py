from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def getCurrentlySelectedElement(self, obj):
        driver = obj.driver
        return driver.switch_to.active_element

