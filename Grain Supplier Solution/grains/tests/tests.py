from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.adminpage import AdminPage
from pages.loginpage import LoginPage

# def test_accessibility_tab_order_admin_page(self):
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000/admin/')
driver.maximize_window()

loginPage = LoginPage(driver)
adminPage = AdminPage(driver)

#ensure that the field selected by default is the email field
assert loginPage.getCurrentlySelectedElement() == loginPage.emailField()

loginPage.hideDjdtPane()
loginPage.logInAsAdmin()

#this tabs through all selectable page element and asserts that each one is in the correct order
adminPage.checkTabOrder()

driver.quit()