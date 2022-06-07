from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from grains.tests.pages.basepage import BasePage

class AdminPage(BasePage):
    #admin page elements
    logo = By.CSS_SELECTOR('a[href="/admin/"]')

    viewSiteLink = By.CSS_SELECTOR('a[href="/"]')
    changePasswordLink = By.CSS_SELECTOR('a[href="/admin/password_change/"]')
    logOutLink = By.CSS_SELECTOR('a[href="/admin/logout/"]')
    
    authenticationAndAuthorizationHeader = By.CSS_SELECTOR('a[href="/admin/auth/"]')
    groupsLink = By.CSS_SELECTOR('a[href="/admin/auth/group/"]')
    addGroupsLink = By.CSS_SELECTOR('a[href="/admin/auth/group/add/"]')
    changeGroupsLink = By.CSS_SELECTOR('a[href="/admin/auth/group/"][class="changelink"]')
    
    coreHeader = By.CSS_SELECTOR('a[href="/admin/core/"]')
    usersLink = By.CSS_SELECTOR('a[href="/admin/core/user/"]')
    addUsersLink = By.CSS_SELECTOR('a[href="/admin/core/user/add/"]')
    changeUsersLink = By.CSS_SELECTOR('a[href="/admin/core/user/"][class="changelink"]')
    
    grainsHeader = By.CSS_SELECTOR('a[href="/admin/grains/"]')
    grainsUserProfilesLink = By.CSS_SELECTOR('a[href="/admin/grains/grainsuserprofile/"]')
    addGrainsUserProfilesLink = By.CSS_SELECTOR('a[href="/admin/grains/grainsuserprofile/add/"]')
    changeGrainsUserProfulesLink = By.CSS_SELECTOR('a[href="/admin/grains/grainsuserprofile/"][class="changelink"]')
    ordersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/order/"]')
    addOrdersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/order/add/"]')
    changeOrdersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/order/"][class="changelink"]')
    suppliersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/supplier/"]')
    addSuppliersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/supplier/add/"]')
    changeSuppliersLink = By.CSS_SELECTOR.find_element_by_css_selector('a[href="/admin/grains/supplier/"][class="changelink"]')

    listOfElementsInOrder = [logo, viewSiteLink, changePasswordLink, logOutLink, authenticationAndAuthorizationHeader, groupsLink, addGroupsLink, changeGroupsLink, coreHeader, usersLink, addUsersLink, changeUsersLink, grainsHeader, grainsUserProfilesLink, addGrainsUserProfilesLink, changeGrainsUserProfulesLink, ordersLink, addOrdersLink, changeOrdersLink, suppliersLink, addSuppliersLink, changeSuppliersLink]
    
    #admin page methods
    def __init__(self, driver):
        super().__init__(driver)

    def checkTabOrder():
        actions = ActionChains()
        actions.send_keys(Keys.TAB)
    
        for i in range(len(AdminPage.listOfElementsInOrder)):
            actions.perform()
            assert BasePage.getCurrentlySelectedElement() == AdminPage.listOfElementsInOrder[i]