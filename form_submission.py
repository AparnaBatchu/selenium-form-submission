from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Fill form
driver.find_element(By.NAME, "firstname").send_keys("Satya")
driver.find_element(By.NAME, "lastname").send_keys("Kruthi")

driver.find_element(By.ID, "sex-1").click()
driver.find_element(By.ID, "exp-2").click()

driver.find_element(By.ID, "datepicker").send_keys("05-12-2025")
driver.find_element(By.ID, "profession-1").click()

driver.find_element(By.ID, "tool-2").click()

# Submit form
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()

time.sleep(3)
print("Form submitted successfully")

driver.quit()
