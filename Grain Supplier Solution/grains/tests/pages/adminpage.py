from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .basepage import BasePage

class AdminPage(BasePage):
    #admin page methods
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #admin page elements
        logo = self.driver.find_element_by_css_selector('a[href="/admin/"]')

        viewSiteLink =self.driver.find_element_by_css_selector('a[href="/"]')
        changePasswordLink = self.driver.find_element_by_css_selector('a[href="/admin/password_change/"]')
        logOutLink = self.driver.find_element_by_css_selector('a[href="/admin/logout/"]')
        
        authenticationAndAuthorizationHeader = self.driver.find_element_by_css_selector('a[href="/admin/auth/"]')
        groupsLink = self.driver.find_element_by_css_selector('a[href="/admin/auth/group/"]')
        addGroupsLink = self.driver.find_element_by_css_selector('a[href="/admin/auth/group/add/"]')
        changeGroupsLink = self.driver.find_element_by_css_selector('a[href="/admin/auth/group/"][class="changelink"]')
        
        coreHeader = self.driver.find_element_by_css_selector('a[href="/admin/core/"]')
        usersLink = self.driver.find_element_by_css_selector('a[href="/admin/core/user/"]')
        addUsersLink = self.driver.find_element_by_css_selector('a[href="/admin/core/user/add/"]')
        changeUsersLink = self.driver.find_element_by_css_selector('a[href="/admin/core/user/"][class="changelink"]')
        
        grainsHeader = self.driver.find_element_by_css_selector('a[href="/admin/grains/"]')
        grainsUserProfilesLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"]')
        addGrainsUserProfilesLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/add/"]')
        changeGrainsUserProfulesLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"][class="changelink"]')
        ordersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/order/"]')
        addOrdersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/order/add/"]')
        changeOrdersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/order/"][class="changelink"]')
        suppliersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"]')
        addSuppliersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/add/"]')
        changeSuppliersLink = self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"][class="changelink"]')

        listOfElementsInOrder = [logo, viewSiteLink, changePasswordLink, logOutLink, authenticationAndAuthorizationHeader, groupsLink, addGroupsLink, changeGroupsLink, coreHeader, usersLink, addUsersLink, changeUsersLink, grainsHeader, grainsUserProfilesLink, addGrainsUserProfilesLink, changeGrainsUserProfulesLink, ordersLink, addOrdersLink, changeOrdersLink, suppliersLink, addSuppliersLink, changeSuppliersLink]
    

    def checkTabOrder():
        actions = ActionChains()
        actions.send_keys(Keys.TAB)
    
        for i in range(len(AdminPage.listOfElementsInOrder)):
            actions.perform()
            assert BasePage.getCurrentlySelectedElement() == AdminPage.listOfElementsInOrder[i]