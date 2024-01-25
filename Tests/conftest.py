from selenium import webdriver
import pytest
# from selenium.webdriver.common.devtools.v107.cache_storage import delete_cache

from Config.config import Testdata
from Pages.checkstatus import CheckPageaction
from Pages.dbcommancomand import DBHelper
from clear_cache import clear as clear_cache

print('ak test')


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    clear_cache(dir=".")
    print("======================================= setup ========================================")
    # db = DBHelper()
    print(request)

    if request.param == "chrome":
        #        web_driver = webdriver.Chrome(executable_path=Testdata.CHROME_EXECUTABLE_PATH)
        print('akas')
        # print(db.select())

        print(CheckPageaction.checkruningfunction())
        # break
        web_driver = webdriver.Chrome()
        print(CheckPageaction.checkruningfunction())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=Testdata.FIREFOX_EXECUTABLE_PATH)
    web_driver.maximize_window()
    # delete_cache(web_driver)
    request.cls.driver = web_driver
    # request.cls.driver = web_driver

    yield
    print("======================================= close setup ========================================")
    web_driver.close()
