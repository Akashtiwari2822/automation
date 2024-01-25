from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Playlist(BaseTest):
    pass

    # def test_playlist_page_title(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Playlistpage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     title = Playlistpage[1].get_home_page_title(Testdata.TITLE)
    #     assert title == Testdata.TITLE

    # def test_playlist_page_header(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Playlistpage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     header = Playlistpage[1].get_header_value()
    #     assert header == Testdata.HOMEPAGE_HEADER

    # def test_url_page(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Playlistpage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     url = Playlistpage.get_currenturl(Testdata.PLAYLIST_PAGE_URL)
    #     assert url == Testdata.PLAYLIST_PAGE_URL

    # def test_playlist_upload(self):
    #     self.loginPage = LoginPage(self.driver)
    #     Playlistpage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
    #     sucess = Playlistpage[1].upload_paly_list(Testdata.PLAYLIST)
    #     assert sucess == Testdata.PLAYLIST_SUCESS_MESSAGE
