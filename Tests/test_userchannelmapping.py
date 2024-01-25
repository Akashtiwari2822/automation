from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_userchannelmapping(BaseTest):

    # def test_userchannel_mapping_add(self):
    #     self.loginPage = LoginPage(self.driver)
    #     userchannelmapping = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = userchannelmapping[9].userchannel_mapping_add()
    #     assert message == Testdata.USERNOTGIVEN

    # def test_userchannel_mapping_add_user(self):
    #     self.loginPage = LoginPage(self.driver)
    #     userchannelmapping = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = userchannelmapping[9].userchannel_mapping_add_user()
    #     assert message == Testdata.CHANNELNOTGIVEN

    # def test_userchannel_mapping_add_channel(self):
    #     self.loginPage = LoginPage(self.driver)
    #     userchannelmapping = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = userchannelmapping[9].userchannel_mapping_add_channel()
    #     assert message == Testdata.STATUS_NOTGIVEN

    def test_userchannel_mapping_add_status(self):
        self.loginPage = LoginPage(self.driver)
        userchannelmapping = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = userchannelmapping[11].userchannel_mapping_add_status()
        assert message == Testdata.DEVICE_SAVED