from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Qcprofile(BaseTest):

    def test_Qc_profile_add_prifix(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix(Testdata.QC_PROFILE_NAME, '')
        assert message == Testdata.PRIFIX_BLANK_MESSAGE

    def test_Qc_profile_add_profile(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix('', Testdata.QC_PROFILE_NAME)
        assert message == Testdata.PROFILE_BLANK_MESSAGE

    def test_Qc_profile_add_extantion(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX)
        assert message == Testdata.EXTANTION_BLANK_MESSAGE

    def test_Qc_profile_add_Invalid_id_skip(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withextantion(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '')
        assert message == Testdata.INVALID_ID_SKIP

    def test_Qc_profile_add_video_black(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withextantion(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '1')
        assert message == Testdata.CHECK_BLACK_VIDEO

    def test_Qc_profile_add_video_black_ignor(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withcheckvideo_true(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '1')
        assert message == Testdata.IGONAOR_BLACK_TIME

    def test_Qc_profile_add_video_freez(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withcheckvideo(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '1')
        assert message == Testdata.CHECK_VIDEO_FREZZ

    def test_Qc_profile_add_video_freez_sec(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withvideofreez(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '1')
        assert message == Testdata.CHECK_VIDEO_FREEZ_SEC

    def test_Qc_profile_add_video_decod(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withvideofreez_deco(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, '1')
        assert message == Testdata.CHECK_VIDEO_DECODER

    def test_Qc_profile_add_video_resolution(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withvideodecoder(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.REDULATION_BLANK_MESSAGE

    def test_Qc_profile_add_video_aspect_ratio(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withresolution(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.ASPECT_RATIO

    def test_Qc_profile_add_video_framerate(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withaspactratio(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.FRAME_RATE

    def test_Qc_profile_add_video_pixel_formet(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withframrate(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.PIXEL_FORMET

    def test_Qc_profile_add_video_pal_ntsc(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withpixelformet(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.PAL_NTSC

    def test_Qc_profile_add_video_save(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].Qc_add_Prefix_Withpalntsc(Testdata.QC_PROFILE_NAME, Testdata.PRIFIX, "1")
        assert message == Testdata.QC_SUCESS_MESSAGE

    def test_Qc_profile_update(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].QC_profile_update()
        assert message == Testdata.QC_SUCESS_MESSAGE_UPDATE

    def test_Qc_profile_delete(self):
        self.loginPage = LoginPage(self.driver)
        Qcprofile = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        message = Qcprofile[2].QC_profile_delete()
        assert message == Testdata.QC_SUCESS_MESSAGE_DELETE
