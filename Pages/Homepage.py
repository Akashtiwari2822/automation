from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.XPATH, "//static-dashboard/mat-toolbar/div[1]/mat-select/div/div[1]/span/span")
    PROFILE_BUTTON = (By.XPATH, "//app-bar/mat-toolbar/div/button[7]")
    ACCOUNT_NAME = (By.XPATH, "//div[3]/div[2]/div/div/div/button[1]")
    COLOR_ICON = (By.XPATH, "//app-bar/mat-toolbar/div/button[3]")
    LOCK = (By.XPATH, "//static-dashboard/mat-toolbar/div[2]/mat-icon")
    SELECT_OPTION = (By.XPATH, "//static-dashboard/mat-toolbar/div[1]/mat-select")
    SELECT_VALUE = (By.XPATH, "//div[3]/div[2]/div/div/mat-option[2]")
    CHCING_MISSING = (By.XPATH, "//static-dashboard/div/div[1]/div/div[1]/mat-card/mat-card-header/div[2]/div["
                                "1]/mat-card-subtitle/b")
    SELECT_VALUE_TWO = (By.XPATH, "//div[3]/div[2]/div/div/mat-option[3]")
    CHCING_MISSING_PRI = (By.XPATH, "//static-dashboard/div/div[1]/div/div[1]/mat-card/mat-card-header/div[2]/div["
                                    "1]/mat-card-subtitle/b")
    SELECT_VALUE_THIRED = (By.XPATH, "//div[3]/div[2]/div/div/mat-option[4]")
    CHCING_MISSING_SEC = (By.XPATH, "//static-dashboard/div/div[1]/div/div[3]/mat-card/mat-card-header/div[2]/div[1]/mat-card-subtitle/b")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_color_icon_exits(self):
        return self.is_visible(self.COLOR_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        self.do_click(self.PROFILE_BUTTON)
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def get_caching_missing_value(self):
        self.do_click(self.LOCK)
        self.do_click(self.SELECT_OPTION)
        self.do_click(self.SELECT_VALUE)
        if self.is_visible(self.CHCING_MISSING):
            return self.get_element_text(self.CHCING_MISSING)

    def get_caching_missing__pri_value(self):
        self.do_click(self.LOCK)
        self.do_click(self.SELECT_OPTION)
        self.do_click(self.SELECT_VALUE_TWO)
        if self.is_visible(self.CHCING_MISSING_PRI):
            return self.get_element_text(self.CHCING_MISSING_PRI)

    def get_caching_missing__sec_value(self):
        self.do_click(self.LOCK)
        self.do_click(self.SELECT_OPTION)
        self.do_click(self.SELECT_VALUE_THIRED)
        if self.is_visible(self.CHCING_MISSING_SEC):
            return self.get_element_text(self.CHCING_MISSING_SEC)
