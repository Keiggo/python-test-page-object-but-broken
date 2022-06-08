from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pages.adminpage import AdminPage
from pages.loginpage import LoginPage
import unittest

# def test_accessibility_tab_order_admin_page(self):
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000/admin/')
driver.maximize_window()

loginPage = LoginPage(driver)

#Ensure that the field selected by default is the email field
assert driver.switch_to.active_element == loginPage.emailField
driver.find_element_by_id('djHideToolBarButton').click()

loginPage.emailField.send_keys("admin@admin.com")
loginPage.passwordField.send_keys("admin")
loginPage.loginButton.click()

adminPage = AdminPage(driver)
adminPage.checkTabOrder()

driver.quit()

