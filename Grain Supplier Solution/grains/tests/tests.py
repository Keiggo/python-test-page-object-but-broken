from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pages.adminpage import AdminPage
from pages.loginpage import LoginPage
import unittest

def test_accessibility_tab_order_admin_page(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get('http://localhost:8000/admin/')
    self.driver.maximize_window()

    loginPage = LoginPage(self.driver)
    adminPage = AdminPage(self.driver)

    #Ensure that the field selected by default is the email field
    assert self.driver.switch_to.active_element == LoginPage.emailField
    self.driver.find_element_by_id('djHideToolBarButton').click()

    loginPage.emailField.send_keys("admin@admin.com")
    loginPage.passwordField.send_keys("admin")
    loginPage.loginButton.click()

    adminPage.checkTabOrder()

    self.driver.quit()