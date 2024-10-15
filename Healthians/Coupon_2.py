from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(), options=chrome_options)

# Navigate to the URL
driver.get("https://devcrm020.echl.co.in/")

# Wait for the username input to be present and log in
try:
    # Login to Healthians
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    username_input.send_keys("atul.tiwari@healthians.com")

    # Wait for the password input and enter password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password_input.send_keys("Atul@123")

    # Click on Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='login_submit']"))
    )
    login_button.click()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Optionally close the driver after a delay
    # driver.quit()
    pass
