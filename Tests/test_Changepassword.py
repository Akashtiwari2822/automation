from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Password(BaseTest):

    def test_get_title_chapass(self):
        self.loginPage = LoginPage(self.driver)
        PasswordChange = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        title = PasswordChange.get_title_change_pass(Testdata.TITLE)
        assert title == Testdata.TITLE

    def test_old_pass_validation(self):
        self.loginPage = LoginPage(self.driver)
        PasswordChange = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        message = PasswordChange.old_pass_validation()
        assert message == Testdata.OLD_PASS

    def test_new_pass_validation(self):
        self.loginPage = LoginPage(self.driver)
        Newpass = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Newpass.new_pass_validation(Testdata.OLD_PASS_VALUE)
        assert message == Testdata.NEW_MESSAGE

    def test_con_pass_validation(self):
        self.loginPage = LoginPage(self.driver)
        Conpass = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Conpass.con_pass_validation(Testdata.OLD_PASS_VALUE, Testdata.NEW_PASS_VALUE)
        assert message == Testdata.CON_MESSAGE

    def test_con_new_pass_diff_validation(self):
        self.loginPage = LoginPage(self.driver)
        ConF = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        message = ConF.diff_new_conf_pass_validation(Testdata.OLD_PASS_VALUE, Testdata.NEW_PASS_VALUE, "abc")
        assert message == Testdata.CON_NEW_PASS

    def test_con_new_pass_diff_validation(self):
        self.loginPage = LoginPage(self.driver)
        ConF = self.loginPage.do_login_pass(Testdata.USER_NAME, Testdata.PASSWORD)
        message = ConF.diff_new_conf_pass_validation(Testdata.OLD_PASS_VALUE, Testdata.NEW_PASS_VALUE, Testdata.NEW_PASS_VALUE)
        assert message == Testdata.CHANGE_PASS_SUC
