import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from src.PageObject.Pages.HomePage import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup

class Test_course_pack(WebDriverSetup):
    def test_add_item_to_course_pack(self):
        driver = self.driver
        self.driver.get(HomePage.get_url_base())
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.sign_up("John", "john@gmail.com", "9432344321", "Canada", "423 John Smith 04324, Ontario")
        home_page.click_sign_up()
