from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get('https://web.fiatcs.com/web/landing/login')
    driver.implicitly_wait(50)

    # Enter email
    input_field = driver.find_element(By.XPATH, '//input[@name="email"]')
    input_field.send_keys("atul.tiwari@healthians.com")

    # Enter password
    input_field = driver.find_element(By.XPATH, '//input[@type="password"]')
    input_field.send_keys("Atul@123")
    input_field.send_keys(Keys.ENTER)

    # Check for login success or failure
    try:
        # Assuming there's an element that only appears on successful login
        success_element = driver.find_element(By.XPATH, '//div[@class="success-message"]')
        print("Login successful!")
    except NoSuchElementException:
        # Assuming there's an element that appears on login failure
        error_element = driver.find_element(By.XPATH, '//div[@class="error-message"]')
        print("Login failed: Incorrect email or password.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
