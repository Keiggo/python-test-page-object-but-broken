from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):
    # #login page elements
    emailField = By.CSS_SELECTOR('input[name="username"]')
    passwordField = By.CSS_SELECTOR('input[name="password"]')
    loginButton = By.CSS_SELECTOR('input[type="submit"]')

    #login page methods
    def __init__(self, driver):
        super().__init__(driver)

    def enterUsername(self):
        self.driver.find