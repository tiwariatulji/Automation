from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Options)
driver.get("https://devcrm020.echl.co.in/")

# Login to Healthians
Username = driver.find_element(By.XPATH, "//input[@name='username']")
Username.send_keys("atul.tiwari@healthians.com")
driver.implicitly_wait(10)
password  = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("Atul@1234")
driver.implicitly_wait(100)



# Click on Login
Login = driver.find_element(By.XPATH, "//button[@id='login_submit']")
Login.click()
driver.implicitly_wait(1000)

# Coupon Managemnt

coupon_task = driver.find_element(By.XPATH, "//*[@id=\"searchSidebarAction\"]")
coupon_task.send_keys("Coupon")
driver.implicitly_wait(1000)

marketing = driver.find_element(By.XPATH, "//span[normalize-space()='Marketing']")
marketing.click()
# webdriver = driver.find_element(By.XPATH, "//p[normalize-space()='Coupon Management']").click() 
# driver.implicitly_wait(1000)

# create coupon
coupon_create = driver.find_element(By.XPATH, "//p[normalize-space()='Campaign Coupon Management']")
coupon_create.click()

# Add campain
add_campaign = driver.find_element(By.XPATH, "//a[@title='New Campaign']//i[@class='fa fa-plus']")
add_campaign.click()
driver.implicitly_wait(1000)

# Fill the details
campaign_name = driver.find_element(By.XPATH, "//input[@id='campaign']")   
campaign_name.send_keys("Healthians")

firquency = driver.find_element(By.XPATH, "//input[@id='frequency']")
firquency.send_keys(100)
driver.implicitly_wait(1000)



# def test_current_date_picker(driver):
#     current_date = datetime.date.today().strftime("%m/%d/%Y")
#     date_picker_input = driver.find_element(By.XPATH, "//input[@id='datepicker1']").click()
#     driver.execute_script("arguments[0].value = '{}';".format(current_date), date_picker_input)

# date picker for start date
start_date = driver.find_element(By.XPATH, "//input[@id='datepicker1']")
start_date.send_keys("30/12/2024")
driver.implicitly_wait(1000)

# date picker for end date
end_date = driver.find_element(By.XPATH, "//input[@id='datepicker2']")
end_date.send_keys("10/01/2025")
driver.implicitly_wait(1000)