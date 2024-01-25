import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage


class Playlistpage(BasePage):
    PLAYLISTBUTTON = (By.XPATH, '//a[@href="/playlist"]')
    PLAYLISTICON = (By.XPATH, "//mat-grid-list/div/mat-grid-tile/figure/button[1]")
    FILETYPE = (By.XPATH, '//*[@name="playlistType"]')
    FILETYPEVALUE = (By.XPATH, '//*[@value="Playlist"]')
    SELECTCHANNEL = (By.XPATH, '//*[@name="playlistChannel"]')
    SELECTCHANNELVALUE = (By.XPATH, "//mat-option//span[normalize-space()='TESTING_MAM']")
    PLAYLISTDATE = (By.XPATH, '//input[@name="playlistDate"]')
    PLAYLISTDATEVALUE = (By.XPATH, "//td[@aria-label='" + Testdata.PLAYLISTDATE + "']")
    FILEPATH = (By.NAME, "file")

    SUBMITBUTTON = (By.XPATH,"//button[@class='mat-raised-button mat-primary']")
    UPLOAD_SUCESS_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")

    def __init__(self, driver):
        super().__init__(driver)

    def get_playlist_page_title(self, title):
        return self.get_title(title)

    # def get_current_url(self, currenturl):
    #     return self.get_currenturl(currenturl)

    def upload_paly_list(self, playlist):
        self.do_click(self.PLAYLISTBUTTON)
        self.do_click(self.PLAYLISTICON)
        self.do_click(self.FILETYPE)
        self.do_click(self.FILETYPEVALUE)
        self.do_click(self.SELECTCHANNEL)
        self.do_click(self.SELECTCHANNELVALUE)
        self.do_click(self.PLAYLISTDATE)
        self.do_click(self.PLAYLISTDATEVALUE)
        print('1')

        self.do_upload(self.FILEPATH, playlist)
        print('done')
        self.do_click(self.SUBMITBUTTON)
        time.sleep(20)
        if self.is_visible(self.UPLOAD_SUCESS_MESSAGE):
            return self.get_element_text(self.UPLOAD_SUCESS_MESSAGE)
