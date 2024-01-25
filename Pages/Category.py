import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

class Category(BasePage):
    CONFIGURATIONTAB = (By.XPATH, '//a[@href="/configuration"]')
    CATEGORYTABBUTTON = (By.XPATH, '//*[@id="mat-tab-label-0-1"]/div')
    NEWCATEGORYBUTTON = (By.XPATH, '//div[2]/button/span')
    CHANNELNAME = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[3]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[1]/div/div[1]/div/mat-select')
    CHANNELNAMEVALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option')
    SAVEBUTTON = (By.XPATH, '//div[3]/div/button[1]/span')
    CATEGORYVALUE = (By.XPATH, '//*[@id="mat-input-171"]')
    CATEGORYPREFIX = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[3]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[3]/div/div[1]/div/input')
    COLORCODE = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[3]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[4]/div/div[1]/div/input')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    CATEGORY = (By.XPATH, "/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[3]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[2]/div/div[1]/div/input")
    SAVEDCATEGORY1 = (By.XPATH, "/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[2]/div/table/tbody/mat-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title/b")
    SAVEDCATEGORY1_PART = (By.XPATH, "/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[2]/div/category/div/div/div[2]/div/table/tbody/mat-expansion-panel/div/div/tbody/tr/td[1]")
    UPDATEBUTTON = (By.XPATH, "//div[3]/div/button[1]/span")

    text = "lkj"
    x = text.replace("lkj","fgh")


    def category_add_channelname(self):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.CATEGORYTABBUTTON)
        time.sleep(3)
        self.do_click(self.NEWCATEGORYBUTTON)
        self.do_click(self.CHANNELNAME)
        self.do_click(self.CHANNELNAMEVALUE)
        time.sleep(2)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def category_add_category(self ,categoryvalue):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.CATEGORYTABBUTTON)
        time.sleep(3)
        self.do_click(self.NEWCATEGORYBUTTON)
        self.do_click(self.CHANNELNAME)
        self.do_click(self.CHANNELNAMEVALUE)
        time.sleep(2)
        self.do_click(self.CATEGORY)
        self.do_send_keys(self.CATEGORY, categoryvalue)
        time.sleep(2)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def category_add_category_prefix(self ,categoryvalue , categoryprefixvalue):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.CATEGORYTABBUTTON)
        time.sleep(3)
        self.do_click(self.NEWCATEGORYBUTTON)
        self.do_click(self.CHANNELNAME)
        self.do_click(self.CHANNELNAMEVALUE)
        time.sleep(2)
        self.do_click(self.CATEGORY)
        self.do_send_keys(self.CATEGORY, categoryvalue)
        time.sleep(2)
        self.do_click(self.CATEGORYPREFIX)
        self.do_send_keys(self.CATEGORYPREFIX, categoryprefixvalue)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def category_add_colorcode(self ,categoryvalue , categoryprefixvalue ,colorcode):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.CATEGORYTABBUTTON)
        time.sleep(3)
        self.do_click(self.NEWCATEGORYBUTTON)
        self.do_click(self.CHANNELNAME)
        self.do_click(self.CHANNELNAMEVALUE)
        time.sleep(2)
        self.do_click(self.CATEGORY)
        self.do_send_keys(self.CATEGORY, categoryvalue)
        time.sleep(2)
        self.do_click(self.CATEGORYPREFIX)
        self.do_send_keys(self.CATEGORYPREFIX, categoryprefixvalue)
        time.sleep(2)
        self.do_click(self.COLORCODE)
        self.do_send_keys(self.COLORCODE, colorcode)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    def category_update(self ,categoryvalue , categoryprefixvalue ,colorcode ,x):
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.CATEGORYTABBUTTON)
        time.sleep(3)
        self.do_click(self.NEWCATEGORYBUTTON)
        self.do_click(self.CHANNELNAME)
        self.do_click(self.CHANNELNAMEVALUE)
        time.sleep(2)
        self.do_click(self.CATEGORY)
        self.do_send_keys(self.CATEGORY, categoryvalue)
        time.sleep(2)
        self.do_click(self.CATEGORYPREFIX)
        self.do_send_keys(self.CATEGORYPREFIX, categoryprefixvalue)
        time.sleep(2)
        self.do_click(self.COLORCODE)
        self.do_send_keys(self.COLORCODE, colorcode)
        self.do_click(self.SAVEDCATEGORY1)
        self.do_click(self.SAVEDCATEGORY1_PART)
        time.sleep(2)
        self.do_click(self.COLORCODE)
        self.do_clear(self.COLORCODE)
        self.do_send_keys(self.COLORCODE, x)
        self.do_click(self.UPDATEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    