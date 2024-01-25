from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata

class Test_Oprations(BaseTest):
    
    def test_qc(self):
        self.loginpage=LoginPage(self.driver)
        Oprations=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message = Oprations[7].Qc_Check()
        assert message == 'Ok'    
        
    def test_move(self):
        self.loginpage=LoginPage(self.driver)
        Oprations=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message = Oprations[7].Move_Check()
        assert message == 'Ok'
        
    def test_proxy(self):
        self.loginpage=LoginPage(self.driver)
        Oprations=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message = Oprations[7].Proxy_Check()
        assert message == 'Ok'