from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def checkElementTabOrder(self, listOfPageElements):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)

        for i in range(len(listOfPageElements(self))):
            actions.perform()
            assert BasePage.getCurrentlySelectedElement(self) == listOfPageElements(self)[i]