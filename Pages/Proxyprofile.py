import time
from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

TIMECODE_OVERLAY = "//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[4]/div/div[1]/div/mat-select"
TIMECODE_OVERLAY_VALUE = '//*[@value="0"]'
TIMECODE_OVERLAY_VALUE_TRUE = '//*[@value="1"]'
TIME_CODE_OVERLAY_POSITION = "//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[5]/div/div[1]/div/mat-select"
TIME_CODE_OVERLAY_POSITION_VALUE = '//*[@value="1"]'
WATERMARK_OVERLAY = "//mat-expansion-panel[1]/div/div/mat-form-field[8]/div/div[1]/div/mat-select"
WATERMARK_OVERLAY_VALUE_TRUE = '//*[@value="1"]'
WATERMARK_OVERLAY_VALUE = '//*[@value="1"]'
MULTIPLE_FORMET_PROXY = '//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[10]/div/div[1]/div/mat-select'
MULTIPLE_FORMET_PROXY_VALUE = '//*[@value="0"]'
TABONE = "//proxyprofile/div/div/div[3]/mat-accordion/mat-expansion-panel[2]/mat-expansion-panel-header"
TABTWO = "//proxyprofile/div/div/div[3]/mat-accordion/mat-expansion-panel[3]/mat-expansion-panel-header"
VIDEO_DECODER = "//mat-accordion/mat-expansion-panel[2]/div/div/mat-form-field[2]/div/div[1]/div/mat-select"
VIDEO_DECODER_VALUE = '//*[@value="libx264"]'
ADUDIO_BITRATE = '//mat-accordion/mat-expansion-panel[3]/div/div/mat-form-field[1]/div/div[1]/div/mat-select'
ADUDIO_BITRATE_VALUE = '//*[@value="64"]'
SAVE_BUTTON_WITHOUT = "//mat-tab-body[2]/div/proxyprofile/div/div/div[3]/div/button[1]"
SELEF_TEST ="//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[3]/div/div[1]/div/mat-select"



class Proxyprofile(BasePage):
    PROFILE_NAME = (By.XPATH, '//*[@placeholder="Profile Name"]')
    PROFILE_PREFIX = (By.XPATH, '//*[@placeholder="Prefix"]')
    PROFILEBUTTON = (By.XPATH, '//a[@href="/profile"]')
    PROXY_TAB= (By.XPATH,'//mat-tab-header/div[2]/div/div/div[2]')
    NEW_PROFILE_BUTTON = (By.XPATH, '//div/proxyprofile/div/div/div[2]/button')
    PROXYTABBUTTON = (By.XPATH, '//mat-tab-group/mat-tab-header/div[2]/div/div/div[2]')
    EXTENTION = (By.XPATH, '//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[3]/div/div[1]/div/mat-select')
    EXTENTION_VALUE = (By.XPATH, '//*[@value=".MXF"]')
    SAVE_BUTTON = (By.XPATH, '//mat-tab-body[2]/div/proxyprofile/div/div/div[3]/div/button[1]')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    TIMECODE_SIZE = (By.XPATH, '//*[@placeholder="TimeCode Size"]')
    DTAT_TABLE = (By.XPATH, '//mat-tab-body[3]/div/qcprofile/div/div/div[2]/mat-tree/mat-tree-node/mat-panel-title')
    UPDATE_BUTTON = (By.XPATH, '//mat-tab-body[3]/div/qcprofile/div/div/div[3]/div/button[1]')
    DTAT_TABLE_dete = (By.XPATH,
                       '//mat-tab-body[3]/div/qcprofile/div/div/div[2]/mat-tree/mat-tree-node[1]/button[2]')
    DELETE_BUTTON = (By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/dialog-qcprofile/div[2]/button[2]')

    def validation_profilename(self, profilename, prifix):
        self.do_click(self.PROFILEBUTTON)
        # time.sleep(2)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        # self.do_click(self.EXTENTION)
        # self.do_click(self.EXTENTION_VALUE)
        time.sleep(5)
        self.do_click(self.SAVE_BUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_extantion(self, profilename, prifix):
        self.do_click(self.PROFILEBUTTON)
        # time.sleep(2)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_timedode(self, profilename, prifix):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SELEF_TEST))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_timedodeposition(self, profilename, prifix):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION_VALUE))
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_timecodesize(self, profilename, prifix, timecodesize):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION_VALUE))
        self.do_send_keys(self.TIMECODE_SIZE, timecodesize)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_watermarkoverlay(self, profilename, prifix, timecodesize):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION_VALUE))
        self.do_send_keys(self.TIMECODE_SIZE, timecodesize)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", WATERMARK_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", WATERMARK_OVERLAY_VALUE_TRUE))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_watermarkoverlayposition(self, profilename, prifix, timecodesize):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION_VALUE))
        self.do_send_keys(self.TIMECODE_SIZE, timecodesize)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", WATERMARK_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", WATERMARK_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", MULTIPLE_FORMET_PROXY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", MULTIPLE_FORMET_PROXY_VALUE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def validation_AUDIOBITRATE(self, profilename, prifix, timecodesize):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        self.do_click(self.NEW_PROFILE_BUTTON)
        self.do_send_keys(self.PROFILE_NAME, profilename)
        self.do_send_keys(self.PROFILE_PREFIX, prifix)
        self.do_click(self.EXTENTION)
        self.do_click(self.EXTENTION_VALUE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TIMECODE_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIMECODE_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", TIME_CODE_OVERLAY_POSITION_VALUE))
        self.do_send_keys(self.TIMECODE_SIZE, timecodesize)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", WATERMARK_OVERLAY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", WATERMARK_OVERLAY_VALUE_TRUE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", MULTIPLE_FORMET_PROXY))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", MULTIPLE_FORMET_PROXY_VALUE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ADUDIO_BITRATE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ADUDIO_BITRATE_VALUE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", SAVE_BUTTON_WITHOUT))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Proxy_profile_update(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        if self.get_element_text(self.DTAT_TABLE) == 'testing_automation':
            self.do_click(self.DTAT_TABLE)
            self.do_click(self.UPDATE_BUTTON)
            time.sleep(4)
            if self.is_visible(self.ALERT_MESSAGE):
                return self.get_element_text(self.ALERT_MESSAGE)

    def Proxy_profile_delete(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.PROXY_TAB)
        if self.get_element_text(self.DTAT_TABLE) == 'testing_automation':
            self.do_click(self.DTAT_TABLE_dete)
            self.do_click(self.DELETE_BUTTON)
            time.sleep(4)
            if self.is_visible(self.ALERT_MESSAGE):
                return self.get_element_text(self.ALERT_MESSAGE)