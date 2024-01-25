import pytest
import time
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import Testdata
import configparser

filename = "/Config/config.ini"
print(filename)
config = configparser.ConfigParser()
config.read(filename)
try:
    config.add_section("LOGIN")
except configparser.DuplicateSectionError:
    print('error')
stored_exception = None


class Test_Login(BaseTest):
    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_signup_link_exits()
        assert flag

    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        titledata = self.loginpage.get_title(Testdata.TITLE)
        assert titledata == Testdata.TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)

    def test_login_check(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_check(Testdata.USER_NAME, Testdata.PASSWORD)
        assert message == Testdata.LOGIN_SUCESS_MESSAGE

    def test_login_wrong_username(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username('abc1', Testdata.PASSWORD)
        assert message == Testdata.LOGIN_WRONG_USERNAME_PASSWORD_MESSAGE

    def test_login_wrong_password(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username(Testdata.USER_NAME, 'abc')
        assert message == Testdata.LOGIN_WRONG_PASSWORD_MESSAGE

    def test_login_wrong_blank(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username_blank('', '')
        assert message == Testdata.LOGIN_BLANK_ALL_MESSAGE

    def test_login_username_blank(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username_blank('', Testdata.PASSWORD)
        assert message == Testdata.LOGIN_BLANK_USERNAME_MESSAGE

    def test_login_password_blank(self):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username_blank(Testdata.USER_NAME, '')
        assert message == Testdata.LOGIN_BLANK_PASSWORD_MESSAGE
