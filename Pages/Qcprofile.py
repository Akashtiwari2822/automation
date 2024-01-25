import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

TABONE = '//mat-accordion/mat-expansion-panel[2]/mat-expansion-panel-header'
CHECK_BLACK_VIDEO = "//mat-expansion-panel[2]/div/div/mat-form-field[1]/div/div[1]/div/mat-select"
CHECK_BLACK_VIDEO_VALUE = '//*[@value="0"]'
CHECK_BLACK_VIDEO_VALUE_TRUE = '//*[@value="1"]'
CHECK_FREZZ_VIDEO = "//mat-expansion-panel[2]/div/div/mat-form-field[3]/div/div[1]/div/mat-select"
CHECK_VIDEO_DECODER = "//mat-expansion-panel[2]/div/div/mat-form-field[5]/div/div[1]/div/mat-select"
CHECK_VIDEO_DECODER_VALUE = '//*[@value="DemuxVideo"]'
SAVEBUTTON_one = "//mat-tab-body[3]/div/qcprofile/div/div/div[3]/div/button[1]"
REGULATION_MAIN = "//mat-expansion-panel[2]/div/div/mat-form-field[6]/div/div[1]/div/mat-select"
REGULATION_MAIN_VALUE = '//*[@value="1920x1080"]'
ASPECT_RATIO = '//mat-expansion-panel[2]/div/div/mat-form-field[7]/div/div[1]/div/mat-select'
ASPECT_RATIO_VALUE = '//*[@value="16:9"]'
FRAMERATE = '//mat-expansion-panel[2]/div/div/mat-form-field[8]/div/div[1]/div/mat-select'
FRAMERATE_VALUE = '//*[@value="15"]'
PIXEL_FORMAT = '//mat-expansion-panel[2]/div/div/mat-form-field[9]/div/div[1]/div/mat-select'
PIXEL_FORMAT_VALUE = '//*[@value="yuv420p"]'
PAL_NTSC = '//mat-expansion-panel[2]/div/div/mat-form-field[10]/div/div[1]/div/mat-select'
PAL_NTSC_VALUE = '//*[@value="PAL"]'



class Qcprofile(BasePage):
    PROFILEBUTTON = (By.XPATH, '//a[@href="/profile"]')
    QCTABBUTTON = (By.XPATH, '//mat-tab-group/mat-tab-header/div[2]/div/div/div[3]')
    NEWADDBUTTON = (By.XPATH, '//mat-tab-group/div/mat-tab-body[3]/div/qcprofile/div/div/div[2]/button')
    PROFILENAME = (By.XPATH, '//*[@placeholder="Profile Name"]')
    PRIFIX = (By.XPATH, '//*[@placeholder="Prefix"]')
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    SAVEBUTTON = (By.XPATH, "//mat-tab-body[3]/div/qcprofile/div/div/div[3]/div/button[1]")

    EXSTANTION = (
        By.XPATH, '//mat-accordion/mat-expansion-panel[1]/div/div/mat-form-field[3]/div/div[1]/div/mat-select')
    EXSTANTIONVALUE = (By.XPATH, '//*[@value=".MXF"]')
    INVALID_ID_SKIP = (By.XPATH, '//*[@placeholder="Invalid Id Skip"]')
    DTAT_TABLE = (By.XPATH, '//mat-tab-body[3]/div/qcprofile/div/div/div[2]/mat-tree/mat-tree-node/mat-panel-title')
    UPDATE_BUTTON = (By.XPATH, '//mat-tab-body[3]/div/qcprofile/div/div/div[3]/div/button[1]')
    TABTWO=(By.XPATH,"//mat-expansion-panel[3]/mat-expansion-panel-header")
    def Qc_add_Prefix(self, profilename, prifix):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        time.sleep(5)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withextantion(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        # self.do_click(self.SAVEBUTTON)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withcheckvideo_true(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE_TRUE))
        time.sleep(2)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withcheckvideo(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withvideofreez(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE_TRUE))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withvideofreez_deco(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withvideodecoder(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withresolution(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withaspactratio(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO_VALUE))
        time.sleep(2)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withframrate(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE_VALUE))
        # time.sleep(2)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withpixelformet(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PIXEL_FORMAT))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PIXEL_FORMAT_VALUE))
        # time.sleep(2)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def Qc_add_Prefix_Withpalntsc(self, profilename, prifix, invalidskipid):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        self.do_click(self.NEWADDBUTTON)
        self.do_send_keys(self.PROFILENAME, profilename)
        self.do_send_keys(self.PRIFIX, prifix)
        self.do_click(self.EXSTANTION)
        self.do_click(self.EXSTANTIONVALUE)
        self.do_send_keys(self.INVALID_ID_SKIP, invalidskipid)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", TABONE))
        # self.do_click(self.TABONE)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_FREZZ_VIDEO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_BLACK_VIDEO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", CHECK_VIDEO_DECODER))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", CHECK_VIDEO_DECODER_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", REGULATION_MAIN_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", ASPECT_RATIO_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", FRAMERATE_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PIXEL_FORMAT))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PIXEL_FORMAT_VALUE))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PAL_NTSC))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element("xpath", PAL_NTSC_VALUE))
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element("xpath", SAVEBUTTON_one))
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)

    def QC_profile_update(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        if self.get_element_text(self.DTAT_TABLE) == 'testing_automation':
            self.do_click(self.DTAT_TABLE)
            self.do_click(self.UPDATE_BUTTON)
            time.sleep(4)
            if self.is_visible(self.ALERT_MESSAGE):
                return self.get_element_text(self.ALERT_MESSAGE)

    DTAT_TABLE_dete = (By.XPATH,
                       '//mat-tab-body[3]/div/qcprofile/div/div/div[2]/mat-tree/mat-tree-node[1]/button[2]')
    DELETE_BUTTON = (By.XPATH, '/html/body/div[3]/div[2]/div/mat-dialog-container/dialog-qcprofile/div[2]/button[2]')

    def QC_profile_delete(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.QCTABBUTTON)
        if self.get_element_text(self.DTAT_TABLE) == 'testing_automation':
            self.do_click(self.DTAT_TABLE_dete)
            self.do_click(self.DELETE_BUTTON)
            time.sleep(4)
            if self.is_visible(self.ALERT_MESSAGE):
                return self.get_element_text(self.ALERT_MESSAGE)
