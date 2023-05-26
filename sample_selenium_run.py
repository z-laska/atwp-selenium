from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://automationexercise.com/")

# Logo
# driver.find_element(By.CSS_SELECTOR, "img[alt='Website for automation practice']")
driver.find_element(By.CLASS_NAME, "logo")

# Cart
# driver.find_element(By.CSS_SELECTOR, "li>a[href='/view_cart']")
driver.find_element(By.XPATH, "//li/a[@href='/view_cart']")

# Email subscription
# driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")
driver.find_element(By.ID, "susbscribe_email")

# Banner switch (right)
# driver.find_element(By.CSS_SELECTOR, "#slider .fa-angle-right")
driver.find_element(By.CSS_SELECTOR, "#slider-carousel .fa-angle-right")

# Brands
driver.find_element(By.CSS_SELECTOR, ".brands_products>h2")

# Footer
# driver.find_element(By.CSS_SELECTOR, "#footer")
driver.find_element(By.XPATH, "//footer")
