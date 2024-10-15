# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://web.fiatcs.com/')

# # browser.close()  # Close the current window
# browser.quit()  # Close the browser and all associated windows

# ==================================================================================================

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=Options)

driver.get('https://web.fiatcs.com/web/landing/login')
driver.implicitly_wait(50)
input_field = driver.find_element(By.XPATH, '//input[@name="email"]')
input_field.send_keys("atul.tiwari@healthians.com")
input_field = driver.find_element(By.XPATH, '//input[@type="password"]')
input_field.send_keys("Atul@123")
input_field.send_keys(Keys.ENTER)


# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('fiatcs' + Keys.RETURN)


# ---------------------------------Login ----------------