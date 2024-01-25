from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata

class Test_Category(BaseTest):
    
    def test_category_add_channelname(self):
        self.loginPage = LoginPage(self.driver)
        Category = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Category[8].category_add_channelname()
        assert message == Testdata.CHANNELNAME_GIVEN
    
    def test_category_add_category(self):
        self.loginPage = LoginPage(self.driver)
        Category = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Category[8].category_add_category(Testdata.CATEGORY_NAME)
        assert message == Testdata.CATEGORY_GIVEN
 
    def test_category_add_category_prefix(self):
        self.loginPage = LoginPage(self.driver)
        Category = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Category[8].category_add_category_prefix(Testdata.CATEGORY_NAME , 'zxc')
        assert message == Testdata.CATEGORY_PREFIX_GIVEN

    def test_category_add_colorcode(self):
        self.loginPage = LoginPage(self.driver)
        Category = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Category[8].category_add_colorcode(Testdata.CATEGORY_NAME , 'zxc', 'lkj')
        assert message == Testdata.COLORCODE_GIVEN

    def test_category_update(self):
        self.loginPage = LoginPage(self.driver)
        Category = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Category[8].category_update(Testdata.CATEGORY_NAME , 'zxc', 'lkj', 'mnjk')
        assert message == Testdata.UPDATEDONE
    