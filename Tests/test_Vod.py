from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Vod(BaseTest):
    
    def test_tc_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withouttc()
        assert message==Testdata.VOD_TC
    
    def test_profilename_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withtc()
        assert message==Testdata.VOD_PROFILE_NAME

    def test_outputextention_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withprofile('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_OUTPUT_EXTENTION
    
    def test_vprofile_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withoutputextention('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_VPROFILE
         
    def test_level_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withvprofile('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_LEVEL         
        
    def test_scaleg_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withlevel('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_SCALE_G
        
    def test_muxrate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withscale('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_MUX_RATE
        
    def test_subtitle_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withmuxrate('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_SUBTITLE
        
    def test_subtitlepath_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withsubtitle('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_SUBTITLE_PATH 
    
    def test_subtitlepath_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withsubtitle('automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_SUBTITLE_PATH
        
    def test_subtitlelanguage_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withsubtitlepath('automationtesting','automationtesting','automationtesting','automationtesting')
        assert message==Testdata.VOD_SUBTITLE_LANGUAGE
        
    def test_pixelformat_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withsubtitlelanguage('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark')
        assert message==Testdata.VOD_PIXEL_FORMAT
        
    def test_simplerate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withpixelformet('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark')
        assert message==Testdata.VOD_SIMPLE_RATE  
            
    def test_audiocodec_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withsimplerate('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark')
        assert message==Testdata.VOD_AUDIO_CODEC     
        
    def test_audiobitrate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withaudiocodec('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark')
        assert message==Testdata.VOD_AUDIO_BITRATE
    
    def test_fremerate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withaudiobitrate('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate')
        assert message==Testdata.VOD_FRAME_RATE
        
    def test_fremerate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withfreamrate('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate')
        assert message==Testdata.VOD_VIDEO_CODEC
        
    def test_resolution_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withvideocodec('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate')
        assert message==Testdata.VOD_RESOLUTION
        
    def test_videobiteate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withresolution('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate','concatvideocodec')
        assert message==Testdata.VOD_VIDEO_BITRATE
        
    def test_minbitrate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withvideobitrate('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate','concatvideocodec','bitrate')
        assert message==Testdata.VOD_MIN_BITRATE
    
    def test_maxbitrate_validation(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_withminbitrate('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate','concatvideocodec','videobitrate','minbitrate')
        assert message==Testdata.VOD_MAX_BITRATE
        
    def test_save(self):
        self.loginpage=LoginPage(self.driver)
        Vod=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Vod[5].Add_vod_save('automationtesting','automationtesting','automationtesting','automationtesting','subtilelanguage','remark','audiobitrate','concatvideocodec','videobitrate','minbitrate','maxbitrate','extraparameter')
        assert message==Testdata.VOD_SAVE
        
    def test_vod_update(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[5].update_data('update')
        # print(message)
        assert message == Testdata.VOD_UPDATE
    
    def test_vod_delete(self):
        self.loginpage=LoginPage(self.driver)
        Tranferprofile=self.loginpage.do_login(Testdata.USER_NAME,Testdata.PASSWORD)
        message=Tranferprofile[5].delete_data()
        # print(message)
        assert message == Testdata.VOD_DELETE
        