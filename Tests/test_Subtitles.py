from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Subtitles(BaseTest):
    def test_subtitle_profilename_validation(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('profilename',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_PROFILE_NAME
        
    def test_subtitle_prefix_validation(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('prefix','automationtesting',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_PREFIX
        
    def test_subtitle_postfix_validation(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('postfix','automationtesting','mxf',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_POSTFIX
    
    def test_subtitle_input_sub_type_validation(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('inputsub','automationtesting','ab','mxf',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_INPUT_SUB_TYPE
        
    def test_subtitle_input_sub_path_validation(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('inputsubpath','automationtesting','ab','mxf',' ',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_INPUT_SUB_PATH
    
    def test_subtitle_validation_output_sub_type(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('outputsubtype','automationtesting','ab','mxf','inputsubpath',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_OUT_SUB_TYPE
        
    def test_subtitle_validation_dvb_profile_type(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('debprofile','automationtesting','ab','mxf','inputsubpath',' ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_DVB_PROFILE
        
    def test_subtitle_validation_dvb_profile_output_type(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('debprofileout','automationtesting','ab','mxf','inputsubpath','devprofilepath ',' ',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_DVB_OUT_PATH
        
    def test_subtitle_validation_ts_input_type(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('tsinput','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath',' ',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_TC_INPUT_PATH
        
    def test_subtitle_validation_ts_output(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('tsoutput','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath',' ',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_TC_OUT_PATH
        
    def test_subtitle_validation_srt_path(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('srtpath','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath','tsoutputpath',' ',' ',' ',' ')
        assert message==Testdata.SUBTITLE_SRT_PATH
        
    def test_subtitle_validation_srt_profile_path(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('srtprofilepath','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath','tsoutputpath','srtpath',' ',' ',' ')
        assert message==Testdata.SUBTITLE_SRTPROFILE_PATH
                
    def test_subtitle_validation_language_code(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('languagecode','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath','tsoutputpath','srtpath','srtprofilepath',' ',' ')
        assert message==Testdata.SUBTITLE_LANGUAGE_CODE
                
    def test_subtitle_validation_clip_length(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('cliplenth','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath','tsoutputpath','srtpath','srtprofilepath','cliplenth',' ')
        assert message==Testdata.SUBTITLE_CLIP_LENTH
    
    def test_subtitle_save(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].check_validation_subtitles('save','automationtesting','ab','mxf','inputsubpath','devprofilepath','dvboutputpath','tspath','tsoutputpath','srtpath','srtprofilepath','cliplenth','12')
        assert message==Testdata.VOD_SAVE
    def test_subtitle_update(self):
        self.loginpage=LoginPage(self.driver)
        subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=subtitle[6].update_data('update')
        # print(message)
        assert message == Testdata.VOD_UPDATE
    # def test_vod_delete(self):
    #     self.loginpage=LoginPage(self.driver)
    #     subtitle=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
    #     message=subtitle[6].delete_data()
    #     # print(message)
    #     assert message == Testdata.VOD_DELETE