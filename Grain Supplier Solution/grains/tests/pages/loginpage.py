from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):
    #login page methods
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # #login page elements
        emailField = self.driver.find_element_by_css_selector('input[name="username"]')
        passwordField = self.driver.find_element_by_css_selector('input[name="password"]')
        loginButton = self.driver.find_element_by_css_selector('input[type="submit"]')