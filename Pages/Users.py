import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage


class Users(BasePage):
    CONFIGURATIONTAB = (By.XPATH, '//a[@href="/configuration"]')
    USERSTAB = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[6]/div')
    NEWUSERPROFILETAB = (By.XPATH, '//mat-tab-header/div[2]/div/div/div[6]/div')
    ADDNEWUSERPROFILETAB = (By.XPATH, '//mat-tab-body[6]/div/user/div/div/div[2]/div[2]/button')
    NAME = (By.XPATH, '//mat-tab-body[6]/div/user/div/div/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[1]/div/div[1]/div/input')
    USERNAME = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[6]/div/user/div/div/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[2]/div/div[1]/div/input')
    PASSWORD = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[6]/div/user/div/div/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[3]/div/div[1]/div/input')
    SAVEBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[6]/div/user/div/div/div[3]/div/button[1]')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    ROLES = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[6]/div/user/div/div/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[6]/div/div[1]/div/mat-select/div/div[1]/span')
    ROLES_VALUE = (By.XPATH, '//*[@value="3"]')
    STATUS = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[6]/div/user/div/div/div[3]/mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[8]/div/div[1]/div/mat-select/div/div[1]')
    STATUS_VALUE = (By.XPATH, '//*[@value="1"]')

    def user_add(self , name):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.USERSTAB)
        self.do_click(self.NEWUSERPROFILETAB)
        time.sleep(5)
        self.do_click(self.ADDNEWUSERPROFILETAB)
        self.do_send_keys(self.NAME , name)
        time.sleep(2)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def user_add_with_username(self , name , username):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.USERSTAB)
        self.do_click(self.NEWUSERPROFILETAB)
        time.sleep(5)
        self.do_click(self.ADDNEWUSERPROFILETAB)
        self.do_send_keys(self.NAME , name)
        time.sleep(2)
        self.do_click(self.USERNAME)
        self.do_send_keys(self.USERNAME , username)
        time.sleep(2)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def user_add_with_password(self , name , username, password):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.USERSTAB)
        self.do_click(self.NEWUSERPROFILETAB)
        self.do_click(self.ADDNEWUSERPROFILETAB)
        self.do_send_keys(self.NAME , name)
        time.sleep(2)
        self.do_click(self.USERNAME)
        self.do_send_keys(self.USERNAME , username)
        time.sleep(2)
        self.do_click(self.PASSWORD)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def user_add_with_roles(self , name , username, password):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.USERSTAB)
        self.do_click(self.NEWUSERPROFILETAB)
        self.do_click(self.ADDNEWUSERPROFILETAB)
        self.do_send_keys(self.NAME , name)
        time.sleep(2)
        self.do_click(self.USERNAME)
        self.do_send_keys(self.USERNAME , username)
        time.sleep(2)
        self.do_click(self.PASSWORD)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.ROLES)
        self.do_click(self.ROLES_VALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def user_add_with_status(self , name , username, password):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.USERSTAB)
        self.do_click(self.NEWUSERPROFILETAB)
        self.do_click(self.ADDNEWUSERPROFILETAB)
        self.do_send_keys(self.NAME , name)
        time.sleep(2)
        self.do_click(self.USERNAME)
        self.do_send_keys(self.USERNAME , username)
        time.sleep(2)
        self.do_click(self.PASSWORD)
        self.do_send_keys(self.PASSWORD,password)
        time.sleep(1)
        self.do_click(self.ROLES)
        self.do_click(self.ROLES_VALUE)
        time.sleep(1)
        self.do_click(self.STATUS)
        self.do_click(self.STATUS_VALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)