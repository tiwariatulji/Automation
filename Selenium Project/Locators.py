# 2.Navigate and Locators (https://rahulshettyacademy.com/AutomationPractice/)
#    ** Navigation:
#     driver.get("{website_url}")
#    **Locators (to locate the web element):
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
# **Common Actions:
# .send_keys()       = to enter input value in a blank
# .click()           = to give click command
# .clear()           = to clear the input field
# .text              = to copy the text



from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Create an instance of the Options class
options = Options()
# Add an experimental option to keep the browser open after the code execution
options.add_experimental_option("detach", True) 

from selenium import webdriver 
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"checkBoxOption1").click()
# driver.find_element(By.NAME,"checkBoxOption2").click()
# driver.find_element(By.CLASS_NAME,"radioButton").click()
# driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"InterviewQues/ResumeAssistance").click()