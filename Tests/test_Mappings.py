from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Mappings(BaseTest):

    # def test_mappings_add(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Mappings = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = Mappings[8].mappings_add()
    #     assert message == Testdata.DEVICENOTGIVEN

    # def test_mappings_add_device(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Mappings = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = Mappings[8].mappings_add_device()
    #     assert message == Testdata.CHANNELNOTGIVEN

    # def test_mappings_add_channel(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Mappings = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     message = Mappings[8].mappings_add_channel()
    #     assert message == Testdata.DEVICENOTGIVEN

    def test_mappings_add_status(self):
        self.loginPage = LoginPage(self.driver)
        Mappings = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Mappings[10].mappings_add_status()
        assert message == Testdata.DEVICE_SAVED