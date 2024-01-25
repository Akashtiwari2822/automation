from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Qcprofile(BaseTest):

    def test_user_add(self):
        self.loginPage = LoginPage(self.driver)
        Users = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Users[9].user_add(Testdata.NAME_USERS)
        assert message == Testdata.NAME_GIVEN

    def test_user_add_with_username(self):
        self.loginPage = LoginPage(self.driver)
        Users = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Users[9].user_add_with_username(Testdata.NAME_USERS, Testdata.USERNAME)
        assert message == Testdata.USERNAME_GIVEN

    def test_user_add_with_password(self):
        self.loginPage = LoginPage(self.driver)
        Users = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Users[9].user_add_with_password(Testdata.NAME_USERS, Testdata.USERNAME ,'qwert')
        assert message == Testdata.PASSWORD_GIVEN

    def test_user_add_with_roles(self):
        self.loginPage = LoginPage(self.driver)
        Users = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Users[9].user_add_with_roles(Testdata.NAME_USERS, Testdata.USERNAME ,'qwert')
        assert message == Testdata.ROLES_GIVEN

    def test_user_add_with_status(self):
        self.loginPage = LoginPage(self.driver)
        Users = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Users[9].user_add_with_status(Testdata.NAME_USERS, Testdata.USERNAME ,'qwert')
        assert message == Testdata.STATUS_GIVEN