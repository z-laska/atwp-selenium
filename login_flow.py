from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://automationexercise.com/login")

driver.find_element(By.CSS_SELECTOR, "[data-qa='login-email']").send_keys('seleniumremote@gmail.com')
driver.find_element(By.CSS_SELECTOR, "[data-qa='login-password']").send_keys('tester')
driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()

# wait
# try finding element
driver.find_element(By.CLASS_NAME, "fa-user")
# assert if exists
