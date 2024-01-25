from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        title = HomePage[0].get_home_page_title(Testdata.TITLE)
        assert title == Testdata.TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        header = HomePage[0].get_header_value()
        assert header == Testdata.HOMEPAGE_HEADER

    def test_home_page_account_name(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        acount = HomePage[0].get_account_name_value()
        assert acount == Testdata.ACCOUNT_NAME

    def test_color_icon(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        assert HomePage[0].is_color_icon_exits()

    def test_caching_missing_value(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        getvalue = HomePage[0].get_caching_missing_value()
        assert getvalue == Testdata.CACHING_MISSING

    def test_caching_missing_pri_value(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        getvalue = HomePage[0].get_caching_missing__pri_value()
        assert getvalue == Testdata.CACHING_MISSING_PRI

    def test_caching_missing_sec_value(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        getvalue = HomePage[0].get_caching_missing__sec_value()
        assert getvalue == Testdata.CACHING_MISSING_SEC

