from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")

driver.find_element(By.ID, "password").send_keys("Password123")

driver.find_element(By.ID, "submit").click()
time.sleep(2)


if "Logged In Successfully" in driver.page_source:
    print("TC01 Passed: Valid login successful")
else:
    print("TC01 Failed: Valid login unsuccessful")


driver.quit()