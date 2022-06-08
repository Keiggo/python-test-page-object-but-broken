from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.adminpage import AdminPage
from pages.loginpage import LoginPage

#admin page tab order accessibility test
#arrange
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000/admin/')
driver.maximize_window()
loginPage = LoginPage(driver)
adminPage = AdminPage(driver)

#act
loginPage.hideDjdtPane()
loginPage.logInAsAdmin()

#assert
#this tabs through all selectable page element and asserts that each one is in the correct order
adminPage.checkAdminPageElementsInRightOrder()

#teardown
driver.quit()