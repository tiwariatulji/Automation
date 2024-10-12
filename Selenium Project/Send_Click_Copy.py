# Common Actions:
# .send_keys() = to enter input value in a blank
# .click()           = to give click command
# .clear()          = to clear the input field
# .text              = to copy the text

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(options=Options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

input_field = driver.find_element(By.XPATH,'//input[@id="name"]')
input_field.send_keys("Atul Tiwari")
input_field.clear()
input_field.send_keys("Har Har Mahadev")

alert_expample = driver.find_element(By.XPATH, '//legend[text()="Switch To Alert Example"]')
alert_expample.text
alert_example_text = alert_expample.text
print(alert_example_text)

# driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("Atul Tiwari ") # send_keys() = to enter input value in a blank
# driver.find_element(By.XPATH,'//input[@id="name"]').clear()  # send_keys() = to enter input value in a blank
# driver.find_element(By.XPATH, '//input[@id="name"]').send_keys("Har Har mahadev")
driver.find_element(By.XPATH,'//input[@id="alertbtn"]').click() # click() = to give click command
# alert = driver.switch_to.alert0 # switch_to.alert = to switch to alert window
# print(alert.text)
# alert.dismiss()
# driver.find_element(By.XPATH, '//input[@id="confirmbtn"]').click() # click() = to give click command
# print(alert.text)
# alert.accept()
# driver.find_element(By.XPATH, '//input[@id="name"]').clear() # clear() = to clear the input field
