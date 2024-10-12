from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(options=Options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

check_boxs = driver.find_elements(By.XPATH, '//input[starts-with(@name,"checkBoxOption")]')
# check_boxs = driver.find_elements(By.XPATH, "(//input[starts-with(@name,'checkBoxOption')])[position()<3]")

print(check_boxs)
print(len(check_boxs))
for check_box in check_boxs:
  if check_boxs.index(check_box)+1 <3:
    check_box.click()
    print(check_box.is_selected())  # to check whether the checkbox is selected or not
    print(check_box.get_attribute("value"))
    print(check_box.text)

    
# print(check_box.is_selected())
# print(check_box.get_attribute("value")) # get_attribute() = to get the value of any attribute
# print(check_box.text) # text = to get the text of the element   that is selected