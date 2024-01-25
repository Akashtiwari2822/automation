import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class PasswordChange(BasePage):
    PROFILE_BUTTON = (By.XPATH, "//app-bar/mat-toolbar/div/button[3]")
    CHANGEPASSWORDBUT = (By.XPATH, "//body/div[3]/div[2]/div/div/div/button[4]")
    # CHANGEPASSWORDBUT = (By.XPATH, "//body/div[4]/div[2]/div/div/div/button[4]")
    OLDPASSWORDF = (By.XPATH, "//*[@Placeholder='Old Password']")
    NEWPASSWORD = (By.XPATH, "//*[@Placeholder='New Password']")
    CONNEWPASSWORD = (By.XPATH, "//*[@Placeholder='Confirm New Password']")
    SUBMITBUTTON = (By.XPATH, "//change-password/div/div/div/mat-dialog-actions/button[1]")
    ERRORMESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")

    def __int__(self, driver):
        super().__init__(driver)

    def get_title_change_pass(self, title):
        return self.get_title(title)

    def old_pass_validation(self):
        self.do_click(self.PROFILE_BUTTON)
        # time.sleep(15)
        self.do_click_force(self.CHANGEPASSWORDBUT)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.ERRORMESSAGE):
            return self.get_element_text(self.ERRORMESSAGE)

    def new_pass_validation(self, oldpassword):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.CHANGEPASSWORDBUT)
        self.do_send_keys(self.OLDPASSWORDF, oldpassword)
        time.sleep(2)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.ERRORMESSAGE):
            return self.get_element_text(self.ERRORMESSAGE)

    def con_pass_validation(self, oldpass, newpass):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.CHANGEPASSWORDBUT)
        self.do_send_keys(self.OLDPASSWORDF, oldpass)
        self.do_send_keys(self.NEWPASSWORD, newpass)
        time.sleep(5)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.ERRORMESSAGE):
            return self.get_element_text(self.ERRORMESSAGE)

    def diff_new_conf_pass_validation(self, oldpass, newpass, conpass):
        self.do_click(self.PROFILE_BUTTON)
        self.do_click(self.CHANGEPASSWORDBUT)
        self.do_send_keys(self.OLDPASSWORDF, oldpass)
        self.do_send_keys(self.NEWPASSWORD, newpass)
        self.do_send_keys(self.CONNEWPASSWORD, conpass)
        self.do_click(self.SUBMITBUTTON)
        if self.is_visible(self.ERRORMESSAGE):
            return self.get_element_text(self.ERRORMESSAGE)
