from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage


class LoginPage(BasePage):
    login_tab_selector = (By.CSS_SELECTOR, "[href='/login']")
    email_field_selector = (By.XPATH, "//*[@data-qa='login-email']")
    password_field_selector = (By.XPATH, "//*[@data-qa='login-password']")
    login_button_selector = (By.XPATH, "//*[@data-qa='login-button']")
    user_tab_selector = (By.CLASS_NAME, "fa-user")
    login_error_message_selector = (By.CSS_SELECTOR, ".login-form p")

    def login_using_email_password(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.login_button_selector).click()

    def check_if_logged_in(self):
        # self.assertTrue(self.driver.find_element(*self.user_tab_selector).is_displayed())
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_tab_selector))

    def check_error_message(self):
        self.driver.find_element(*self.login_error_message_selector)