from selenium.webdriver.common.by import By


class BasePage:
    products_tab_selector = (By.CSS_SELECTOR, "[href='/products']")

    def __init__(self, driver):
        self.driver = driver

    def close_ad(self):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.refresh()