from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Transferprofile(BaseTest):
    
    def test_Transferprofile_without_profilename_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withoutprofilename('')
        assert message == Testdata.TRANSFER_PRFILE_VALIDATION
        
    def test_Transferprofile_without_overwrite_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withprofilename('automationtesting')
        assert message == Testdata.TRANSFER_PRFILE_OVERWRITE_VALIDATION
        
    def test_Transferprofile_without_checksumverifcation_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withoutchecksumverfiy('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation')
        assert message == Testdata.TRANSFER_PRFILE_CHECKSUMVERIFY_VALIDATION
                
    def test_Transferprofile_without_checksum_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withchecksumverfiy('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation')
        assert message == Testdata.TRANSFER_PRFILE_CHECKSUM_VALIDATION
    
    def test_Transferprofile_without_checksumverifcation_disable_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withchecksumverfiy_disable('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_VALIDATION_VALIDATION
            
    def test_Transferprofile_without_tranferfail_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withchecksum('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_VALIDATION_VALIDATION
            
    def test_Transferprofile_without_tranferfail_value_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withtranferfail('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_VALUE_VALIDATION_VALIDATION    
           
    def test_Transferprofile_without_retry_waittime_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withtranferfailvalue('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation','50')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_RETURN_TIME_VALIDATION_VALIDATION
        
    def test_Transferprofile_without_transfer_protocol_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withretrywaittime('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation','50','50')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_PROTOCOL_VALIDATION_VALIDATION
        
    def test_Transferprofile_without_opration_type_check_validation(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_withtransferprotocolr('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation','50','50')
        assert message == Testdata.TRANSFER_PRFILE_TRANSFER_OPRATION_VALIDATION_VALIDATION
        
    def test_Transferprofile_save(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].add_tranferprofile_save('automationtesting','automationtesting','validprfix','mxf|mov|Mmp4','autionmation','50','50','100')
        assert message == Testdata.TRANSFER_PRFILE_SAVE
    
    def test_Transferprofile_update(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].update_data('update')
        # print(message)
        assert message == Testdata.TRANSFER_PRFILE_UPDATE
    
    def test_Transferprofile_delete(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[4].delete_data()
        # print(message)
        assert message == Testdata.TRANSFER_PRFILE_DELETE
    