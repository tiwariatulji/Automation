from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

# # @pytest.fixture
# # def driver():
#     options = Options()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     # driver.quit()

def test_login(driver):
    driver.get("https://devcrm020.echl.co.in/")
    
    element = driver.find_element(By.XPATH, "//input[@name='username']")
    element.send_keys("atul.tiwari@healthians.com")
    driver.implicitly_wait(10)
    
    element_2 = driver.find_element(By.XPATH, "//input[@name='password']")
    element_2.send_keys("Atul@123")
    driver.implicitly_wait(10)
    
    element_3 = driver.find_element(By.XPATH, "//button[@id='login_submit']")
    element_3.click()
    driver.implicitly_wait(70)

    driver.quit()

    
    