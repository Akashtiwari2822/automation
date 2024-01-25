import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

class userchannelmapping(BasePage):
    CONFIGURATIONTAB = (By.XPATH, '//a[@href="/configuration"]')
    MAPPINGSTAB = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[5]/div')
    NEWMAPPINGTAB = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[1]/button/span')
    USERCHANNEL_MAPPING = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[1]/div[2]')
    USER_NAME = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[1]/div/div[1]/div/mat-select/div/div[1]/span')
    CHANNELBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[2]/div/div[1]/div/mat-select/div/div[1]/span')
    CHANNELBUTTON_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option/span')
    STATUSBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[3]/div/div[1]/div/mat-select/div/div[1]/span')
    STATUSBUTTON_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option[1]/span')
    SAVEBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/div/button[1]/span')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    CANCELBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/div/button[2]')
    USER_NAME_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option[1]/span')

    # def userchannel_mapping_add(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.USERCHANNEL_MAPPING)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     time.sleep(5)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)
        
    # def userchannel_mapping_add_user(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.USERCHANNEL_MAPPING)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     self.do_click(self.USER_NAME)
    #     self.do_click(self.USER_NAME_VALUE)
    #     time.sleep(5)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)

    # def userchannel_mapping_add_channel(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.USERCHANNEL_MAPPING)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     self.do_click(self.USER_NAME)
    #     self.do_click(self.USER_NAME_VALUE)
    #     self.do_click(self.CHANNELBUTTON)
    #     self.do_click(self.CHANNELBUTTON_VALUE)
    #     time.sleep(5)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)

    def userchannel_mapping_add_status(self): 
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.MAPPINGSTAB)
        self.do_click(self.USERCHANNEL_MAPPING)
        self.do_click(self.NEWMAPPINGTAB)
        self.do_click(self.USER_NAME)
        self.do_click(self.USER_NAME_VALUE)
        self.do_click(self.CHANNELBUTTON)
        self.do_click_force(self.CHANNELBUTTON_VALUE)
        time.sleep(3)
        self.do_click(self.STATUSBUTTON)
        self.do_click(self.STATUSBUTTON_VALUE)
        time.sleep(3)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

