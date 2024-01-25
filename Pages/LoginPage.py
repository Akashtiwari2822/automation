from Pages.BasePage import BasePage
from Config.config import Testdata
from Pages.Qcprofile import Qcprofile
from Pages.Transferprofile import Tranferprofile
from Pages.Vod import Vod
from Pages.Subtitles import Subtitles
from Pages.Oprations import Oprations
from Pages.Proxyprofile import Proxyprofile
from Pages.Playlistpage import Playlistpage
from Pages.Homepage import HomePage
from Pages.Users import Users
from Pages.Category import Category
from Pages.Chnagepassword import PasswordChange
from selenium.webdriver.common.by import By
from Pages.Mappings import Mappings
from Pages.userchannelmapping import userchannelmapping


class LoginPage(BasePage):
    """ This is my by locators it is showing of the all input and other data  """
    EMAIL = (By.ID, "UN")
    PASSWORD = (By.ID, "pwd")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='mat-raised-button mat-primary']")
    # LOGIN_BUTTON = (By.XPATH, "//mat-horizontal-stepper/div[2]/div[1]/form/div[4]/button")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    LOGIN_SUCESS_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/div/button/span")
    # LOGIN_SUCESS_MESSAGE = (By.XPATH, "//div/snack-bar-container/simple-snack-bar/span")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")

    """ This is my constructor of the page class  """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    # this is my page action

    # this is get the page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # this is use to the signup test show or not
    def is_signup_link_exits(self):
        return self.is_visible(self.SIGNUP_LINK)

    # this showing the login button exits or not
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver), Playlistpage(self.driver), Qcprofile(self.driver), Proxyprofile(self.driver), Tranferprofile(self.driver), Vod(self.driver), Subtitles(self.driver), Oprations(self.driver),Category(self.driver), Users(self.driver) , Mappings(self.driver), userchannelmapping(self.driver)

    def do_login_pass(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return PasswordChange(self.driver)

    def do_login_check(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_SUCESS_MESSAGE):
            return self.get_element_text(self.LOGIN_SUCESS_MESSAGE)

    def do_login_password_username(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_SUCESS_MESSAGE):
            return self.get_element_text(self.LOGIN_ERROR_MESSAGE)

    def do_login_password_username_blank(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_SUCESS_MESSAGE):
            return self.get_element_text(self.LOGIN_ERROR_MESSAGE)
