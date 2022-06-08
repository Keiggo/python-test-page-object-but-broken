from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #base page methods
    def getCurrentlySelectedElement(self):
        return self.driver.switch_to.active_element

    def clickElement(self, element):
        element.click()

    def enterText(self, element, textToEnter):
        element.send_keys(textToEnter)

    def hideDjdtPane(self):
        self.driver.find_element_by_id('djHideToolBarButton').click()