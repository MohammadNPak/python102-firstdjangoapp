from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/accounts/profile/abc")

user_full_name = driver.find_element(By.ID,"full_name").text
print(user_full_name)
driver.quit()