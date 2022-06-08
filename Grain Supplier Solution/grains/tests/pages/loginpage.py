from django.forms import EmailField
from pages.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #login page elements
    def emailField(self):
        return self.driver.find_element_by_css_selector('input[name="username"]')

    def passwordField(self):
        return self.driver.find_element_by_css_selector('input[name="password"]')

    def loginButton(self):
        return self.driver.find_element_by_css_selector('input[type="submit"]')

    def clickLoginButton(self):
        loginButton = LoginPage.loginButton(self)
        BasePage.clickElement(self, loginButton)

    def enterUsername(self, username):
        emailField = LoginPage.emailField(self)

        BasePage.enterText(self, emailField, username)

    def enterPassword(self, password):
        passwordField = LoginPage.passwordField(self)        
        BasePage.enterText(self, passwordField, password)

    def logInAsAdmin(self):
        LoginPage.enterUsername(self, "admin@admin.com")
        LoginPage.enterPassword(self, "admin")
        LoginPage.clickLoginButton(self)