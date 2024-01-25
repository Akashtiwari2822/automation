import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

class Subtitles(BasePage):
    PROFILEBUTTON = (By.XPATH, '//a[@href="/profile"]')
    SUBTITLESBUTTON = (By.XPATH, '//mat-tab-group/mat-tab-header/div[2]/div/div/div[6]')
    ADDBUTTON =(By.XPATH,'//app-subtitleprofile/div/div/div[2]/button')
    PROFILENAME = (By.XPATH, "//*[@Placeholder='Profile Name']")
    PREFIX = (By.XPATH, "//*[@Placeholder='Prefix']")
    POSTFIX = (By.XPATH, "//*[@Placeholder='Postfix']")
    INPUTSUBTYPE =(By.XPATH,"//mat-expansion-panel/div/div/mat-form-field[4]/div/div[1]/div/mat-select")
    INPUTSUBTYPEVALUE = (By.XPATH, "//*[@Value='fpc']")
    INPUTSUBPATH = (By.XPATH, "//*[@Placeholder='Input Sub Path']")
    OUTPUTSUBTYPE = (By.XPATH,"//mat-expansion-panel/div/div/mat-form-field[6]/div/div[1]/div/mat-select")
    OUTPUTSUBTYPEVALUE = (By.XPATH, "//*[@Value='ts']")
    DVBPROFILEPATH = (By.XPATH, "//*[@Placeholder='DVB Profile Path']")
    DVBPROFILEOUTPATH = (By.XPATH, "//*[@Placeholder='DVB Output Path']")
    TSPATH = (By.XPATH, "//*[@Placeholder='TS Input Path']")
    TSOUTPATH = (By.XPATH, "//*[@Placeholder='TS Output Path']")
    SRTPATH = (By.XPATH, "//*[@Placeholder='SRT Path']")
    SRTPROFILEPATH = (By.XPATH, "//*[@Placeholder='SRT Profile Path']")
    LANGUAGECODE = (By.XPATH, "//*[@Placeholder='Language Code']")
    CLIPLENGTH = (By.XPATH, "//*[@Placeholder='Clip Length(numeric)']")
    SAVEBUTTON =(By.XPATH,"//app-subtitleprofile/div/div/div[3]/div/button[1]")
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    UPDATEDATA=(By.XPATH,"//app-subtitleprofile/div/div/div[2]/mat-tree/mat-tree-node/mat-panel-title/div")
    UPDATEDATA_NEW=(By.XPATH,"//app-subtitleprofile/div/div/div[2]/mat-tree/mat-tree-node/mat-panel-title/div")
    DELETEBUTTON = (By.XPATH,"//app-subtitleprofile/div/div/div[2]/mat-tree/mat-tree-node/mat-panel-title/div[normalize-space(text())='automationtesting']/following-sibling::td/button")
    YESBUTTON=(By.XPATH,"//mat-dialog-container/dialog-vodprofile/div[2]/button[2]")
    
    
    def check_validation_subtitles(self,type,profilename,prefix,postfix,inputsubpath,devprofilepath,dvboutputpath,tspath,tsoutputpath,srtpath,srtprofilepath,languagecode,cliplength):
        time.sleep(4)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.SUBTITLESBUTTON)
        self.do_click(self.ADDBUTTON)
        if(type=="profilename"):
            time.sleep(3)
            self.do_click(self.SAVEBUTTON)
            if self.is_visible(self.ALERT_MESSAGE):
                return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.PROFILENAME,profilename)
        if(type=="prefix"):
                time.sleep(3)
                self.do_click(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.PREFIX,prefix)
        if(type=="postfix"):
                time.sleep(3)
                self.do_click(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.POSTFIX,postfix)
        if(type=="inputsub"):
                time.sleep(3)
                self.do_click(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_click(self.INPUTSUBTYPE)
        self.do_click(self.INPUTSUBTYPEVALUE)
        if(type=="inputsubpath"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.INPUTSUBPATH,inputsubpath)
        if(type=="outputsubtype"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_click_force(self.OUTPUTSUBTYPE)
        self.do_click_force(self.OUTPUTSUBTYPEVALUE)
        if(type=="debprofile"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.DVBPROFILEPATH,devprofilepath)        
        if(type=="debprofileout"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.DVBPROFILEOUTPATH,dvboutputpath)    
        if(type=="tsinput"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.TSPATH,tspath)    
        if(type=="tsoutput"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.TSOUTPATH,tsoutputpath)
        if(type=="srtpath"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.SRTPATH,srtpath)
        if(type=="srtprofilepath"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.SRTPROFILEPATH,srtprofilepath)
        if(type=="languagecode"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.LANGUAGECODE,languagecode)
        if(type=="cliplenth"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        self.do_send_keys(self.CLIPLENGTH,cliplength)
        if(type=="save"):
                time.sleep(3)
                self.do_click_force(self.SAVEBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                 return self.get_element_text(self.ALERT_MESSAGE)
        
        
    def update_data(self,profilename):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.SUBTITLESBUTTON)
        time.sleep(5)
        if self.is_visible(self.UPDATEDATA):
            time.sleep(5)
            if(self.get_element_text(self.UPDATEDATA)=="automationtesting"):
                # time.sleep(5)
                self.do_click(self.UPDATEDATA)
                # time.sleep(5)
                self.do_send_keys(self.PREFIX,profilename)
                # time.sleep(5)
                self.do_click(self.SAVEBUTTON)
                time.sleep(1)
                if(self.get_element_text(self.UPDATEDATA_NEW)=="automationtesting"):
                    if self.is_visible(self.ALERT_MESSAGE):
                        return self.get_element_text(self.ALERT_MESSAGE)
                        #time.sleep(5)        

    def delete_data(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.SUBTITLESBUTTON)
        if self.is_visible(self.UPDATEDATA_NEW):
            if(self.get_element_text(self.UPDATEDATA_NEW)=="automationtesting"):
                time.sleep(5)
                self.do_click(self.DELETEBUTTON)
                self.do_click(self.YESBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                    return self.get_element_text(self.ALERT_MESSAGE)