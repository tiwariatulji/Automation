# ***CSS Selector Locator
# FROM                                SYNTAX
# Class, Attribute & Value           tagname.classvalue[attribute = ‘value’]
# Attribute & Value                  tagname[attribute = ‘value’]
# ID                                 tagname#IDvalue
# Class                              tagname.classvalue
#                                 Note: Tagname is optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(options=Options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
driver.find_element(By.CSS_SELECTOR, "input.inputs[placeholder='Enter Your Name']").send_keys("Har Har Mahadev")

# *** XPath Locator
# driver.find_element(By.XPATH, "//input[@value='radio2']").click()
