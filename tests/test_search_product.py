import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.products import ProductsPage


class TestSearchProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")

        self.products_page = ProductsPage(self.driver)

    def test_search_product_unicorn(self):
        self.products_page.search_product('unicorn')
        self.assertGreaterEqual(len(self.products_page.get_visible_products()), 2)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
