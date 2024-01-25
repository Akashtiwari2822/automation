import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

class Mappings(BasePage):
    CONFIGURATIONTAB = (By.XPATH, '//a[@href="/configuration"]')
    MAPPINGSTAB = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[5]/div')
    NEWMAPPINGTAB = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[1]/button/span')
    DEVICECHANNELMAPPING = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[4]')
    DEVICEBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[1]/div/div[1]/div/mat-select/div/div[1]/span')
    # DEVICEBUTTON_VALUE = (By.XPATH, '/html/body/div[2]/div[2]/div/div/mat-option[1]')
    DEVICEBUTTON_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option[1]')
    CHANNELSBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[2]/div/div[1]/div/mat-select/div/div[1]/span')
    STATUSBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/div/div/mat-form-field[3]/div/div[1]/div/mat-select/div/div[1]/span')
    SAVEBUTTON = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/div/button[1]/span')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    CHANNELSBUTTON_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option[1]/span')
    ALLPAGECLICK = (By.XPATH, '/html/body/app-root/body/configuration/div/mat-tab-group/div/mat-tab-body[5]/div/mapping/div/div/div/div/div[2]/div[2]/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title')
    STATUSBUTTON_VALUE = (By.XPATH, '/html/body/div[3]/div[2]/div/div/mat-option[1]/span')
    
    # def mappings_add(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     time.sleep(5)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)
        
    # def mappings_add_device(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     self.do_click(self.DEVICEBUTTON)
    #     time.sleep(5)
    #     self.do_click(self.DEVICEBUTTON_VALUE)
    #     time.sleep(4)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)
        
    # def mappings_add_channel(self): 
    #     self.do_click(self.CONFIGURATIONTAB)
    #     self.do_click(self.MAPPINGSTAB)
    #     self.do_click(self.NEWMAPPINGTAB)
    #     self.do_click(self.CHANNELSBUTTON)
    #     self.do_click(self.CHANNELSBUTTON_VALUE)
    #     time.sleep(4)
    #     self.do_click(self.ALLPAGECLICK)
    #     time.sleep(3)
    #     self.do_click(self.SAVEBUTTON)
    #     if self.is_visible(self.ALERT_MESSAGE):
    #         return self.get_element_text(self.ALERT_MESSAGE)
        
    def mappings_add_status(self): 
        self.do_click(self.CONFIGURATIONTAB)
        self.do_click(self.MAPPINGSTAB)
        self.do_click(self.NEWMAPPINGTAB)
        self.do_click(self.DEVICEBUTTON)
        self.do_click(self.DEVICEBUTTON_VALUE)
        time.sleep(3)
        self.do_click(self.CHANNELSBUTTON)
        self.do_click_force(self.CHANNELSBUTTON_VALUE)
        time.sleep(2)
        self.do_click_force(self.STATUSBUTTON)
        self.do_click_force(self.STATUSBUTTON_VALUE)
        time.sleep(3)
        self.do_click_force(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
