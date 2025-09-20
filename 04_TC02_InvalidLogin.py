from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("pedini jayashree")

driver.find_element(By.ID, "password").send_keys("wrong password")

driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("TC02 Passed: Correct error message displayed")
else:
    print("TC02 Failed: Error message missing or incorrect")

driver.quit()
