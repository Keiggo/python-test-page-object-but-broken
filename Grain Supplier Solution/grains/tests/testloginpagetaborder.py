from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.loginpage import LoginPage

#login page tab order accessibility test
#arrange
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000/admin/')
driver.maximize_window()
loginPage = LoginPage(driver)

#ensure that the field selected by default is the email field
assert loginPage.getCurrentlySelectedElement() == loginPage.emailField()

#act
loginPage.hideDjdtPane()

#assert
loginPage.checkLoginPageElementsInRightOrder()

#teardown
driver.quit()