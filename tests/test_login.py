import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.login_using_email_password('seleniumremote@gmail.com', 'tester')
        self.login_page.check_if_logged_in()

    def test_wrong_password(self):
        self.login_page.login_using_email_password('seleniumremote@gmail.com', 'tester1')
        self.login_page.check_error_message()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
