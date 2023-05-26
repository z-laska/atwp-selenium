from selenium.webdriver.common.by import By
from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, "[href='/products']")
    search_field_selector = (By.ID, "search_product")
    search_button_selector = (By.ID, "submit_search")
    products_selector = (By.CLASS_NAME, "single-products")

    def search_product(self, product_name):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.find_element(*self.search_field_selector).send_keys(product_name)
        self.driver.find_element(*self.search_button_selector).click()

    def get_visible_products(self):
        return self.driver.find_elements(*self.products_selector)
