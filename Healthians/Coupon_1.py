from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Replace with the actual path to your ChromeDriver executable
driver = webdriver.Chrome()

# Navigate to the URL of the page
driver.get("")

# Select Campaign
campaign_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='Select Campaign']"))
campaign_dropdown.select_by_visible_text("Your Desired Campaign")

# No Of Frequency (if applicable)
# frequency_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='No Of Frequency']"))
# frequency_dropdown.select_by_visible_text("Your Desired Frequency")

# Coupon Start Date
driver.find_element(By.XPATH, "//input[@name='Coupon Start Date']").send_keys("2023-12-20")

# Coupon End Date
driver.find_element(By.XPATH, "//input[@name='Coupon End Date']").send_keys("2023-12-30")

# Sample Collection Start Date
driver.find_element(By.XPATH, "//input[@name='Sample Collection Start Date']").send_keys("2023-12-21")

# Sample Collection End Date
driver.find_element(By.XPATH, "//input[@name='Sample Collection End Date']").send_keys("2023-12-31")

# Unique Coupon Code (if applicable)
# unique_coupon_code_checkbox = driver.find_element(By.XPATH, "//input[@name='Unique Coupon Code']")
# unique_coupon_code_checkbox.click()

# Discount Type
discount_type_radio = driver.find_element(By.XPATH, "//input[@value='Fixed']")
discount_type_radio.click()

# Do You Want For Multiple Slab?
multiple_slab_checkbox = driver.find_element(By.XPATH, "//input[@name='Do You Want For Multiple Slab' and @value='Yes']")
multiple_slab_checkbox.click()

# Discount Amount
driver.find_element(By.XPATH, "//input[@name='Discount Amount']").send_keys("100")

# Min Booking Value
driver.find_element(By.XPATH, "//input[@name='Min Booking Value']").send_keys("500")

# Which Platform use this Coupon?
platform_checkboxes = driver.find_elements(By.XPATH, "//input[@name='Which Platform use this Coupon']")
for checkbox in platform_checkboxes:
    checkbox.click()

# Agent of which role can apply this coupon? (if applicable)
# role_checkboxes = driver.find_elements(By.XPATH, "//input[@name='Agent of which role can apply this coupon']")
# for checkbox in role_checkboxes:
#     checkbox.click()

# For what kind of users. This coupon is meant for? (if applicable)
# user_checkboxes = driver.find_elements(By.XPATH, "//input[@name='For what kind of users. This coupon is meant for?']")
# for checkbox in user_checkboxes:
#     checkbox.click()

# Add Coupon button (replace with actual button locator)
add_coupon_button = driver.find_element(By.XPATH, "//button[text()='Add Coupon']")
add_coupon_button.click()

# Close the browser
driver.quit()