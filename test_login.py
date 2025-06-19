from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and go to login page
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# VALID LOGIN TEST
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("✅ Valid login passed")
else:
    print("❌ Valid login failed")

# INVALID LOGIN TEST
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Your username is invalid!" in driver.page_source or "Your password is invalid!" in driver.page_source:
    print("✅ Invalid login passed")
else:
    print("❌ Invalid login failed")

driver.quit()
