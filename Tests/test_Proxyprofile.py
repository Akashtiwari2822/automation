from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Proxyprofile(BaseTest):

    def test_profile_name(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_profilename('', Testdata.PROXY_PRIFIX)
        assert message == Testdata.PROFILE_NAME_PROXY_ALERT

    def test_prifix_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_profilename(Testdata.PROFILE_NAME_PROXY, '')
        assert message == Testdata.PRIFIX_MESSAGE

    def test_extantion_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_profilename(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX)
        assert message == Testdata.PROXY_EXSTANTION_ALERT

    def test_timecode_overlay_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_extantion(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX)
        assert message == Testdata.PROXY_TIMECODE

    def test_timecode_overlay_position_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_timedode(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX)
        assert message == Testdata.PROXY_TIMECODE_POSITION

    def test_timecode_size_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_timedodeposition(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX)
        assert message == Testdata.PROXY_TIME_CODE_SIZE

    def test_watermark_overlay_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_timecodesize(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX,
                                                          Testdata.PROXY_TIME_CODE_SIZE_VALUE)
        assert message == Testdata.PROXY_WATERMARK_ALERT

    def test_watermark_overlay_char_value_validation(self):
        self.loginPage = LoginPage(self.driver)
        Proxyprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Proxyprofile[3].validation_timecodesize(Testdata.PROFILE_NAME_PROXY, Testdata.PROXY_PRIFIX,
                                                          Testdata.PROXY_TIME_CODE_SIZE_CHAR_VALUE)
        assert message == Testdata.PROXY_TIME_CODE_SIZE

    def test_proxy_profile_update(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[3].Proxy_profile_update()
        assert message == Testdata.QC_SUCESS_MESSAGE_UPDATE

    def test_proxy_profile_delete(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[3].Proxy_profile_delete()
        assert message == Testdata.QC_SUCESS_MESSAGE_DELETE


