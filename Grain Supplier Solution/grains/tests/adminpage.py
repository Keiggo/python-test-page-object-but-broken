from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .basepage import BasePage

class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #admin page elements
    def logo(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/"]')

    def viewSiteLink(self):
        return self.driver.find_element_by_css_selector('a[href="/"]')
        
    def changePasswordLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/password_change/"]')
        
    def logOutLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/logout/"]')
        
    def authenticationAndAuthorizationHeader(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/auth/"]')
    
    def groupsLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/auth/group/"]')
        
    def addGroupsLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/auth/group/add/"]')
        
    def changeGroupsLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/auth/group/"][class="changelink"]')
        
    def coreHeader(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/core/"]')
        
    def usersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/core/user/"]')
        
    def addUsersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/core/user/add/"]')
        
    def changeUsersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/core/user/"][class="changelink"]')
        
    def grainsHeader(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/"]')
        
    def grainsUserProfilesLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"]')
        
    def addGrainsUserProfilesLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/add/"]')
        
    def changeGrainsUserProfulesLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"][class="changelink"]')
        
    def ordersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/order/"]')
        
    def addOrdersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/order/add/"]')
        
    def changeOrdersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/order/"][class="changelink"]')
        
    def suppliersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"]')
        
    def addSuppliersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/add/"]')
        
    def changeSuppliersLink(self):
        return self.driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"][class="changelink"]')

    # listOfElementsInOrder = [logo(), viewSiteLink(), changePasswordLink(), logOutLink(), authenticationAndAuthorizationHeader(), groupsLink(), addGroupsLink(), changeGroupsLink(), coreHeader(), usersLink(), addUsersLink(), changeUsersLink(), grainsHeader(), grainsUserProfilesLink(), addGrainsUserProfilesLink(), changeGrainsUserProfulesLink(), ordersLink(), addOrdersLink(), changeOrdersLink(), suppliersLink(), addSuppliersLink(), changeSuppliersLink()]

    #admin page methods
    def listOfElementsInOrder(self):
        return [AdminPage.logo(self), AdminPage.viewSiteLink(self), AdminPage.changePasswordLink(self), AdminPage.logOutLink(self), AdminPage.authenticationAndAuthorizationHeader(self), AdminPage.groupsLink(self), AdminPage.addGroupsLink(self), AdminPage.changeGroupsLink(self), AdminPage.coreHeader(self), AdminPage.usersLink(self), AdminPage.addUsersLink(self), AdminPage.changeUsersLink(self), AdminPage.grainsHeader(self), AdminPage.grainsUserProfilesLink(self), AdminPage.addGrainsUserProfilesLink(self), AdminPage.changeGrainsUserProfulesLink(self), AdminPage.ordersLink(self), AdminPage.addOrdersLink(self), AdminPage.changeOrdersLink(self), AdminPage.suppliersLink(self), AdminPage.addSuppliersLink(self), AdminPage.changeSuppliersLink(self)]
    
    # def checkTabOrder(self):
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(Keys.TAB)
    
    #     for i in range(len(AdminPage.listOfElementsInOrder(self))):
    #         actions.perform()
    #         assert BasePage.getCurrentlySelectedElement(self) == AdminPage.listOfElementsInOrder(self)[i]
    
    def checkAdminPageElementsInRightOrder(self):
        listOfAdminPageElementsInOrder = AdminPage.listOfElementsInOrder(self)
        BasePage.checkElementTabOrder(self, listOfAdminPageElementsInOrder)