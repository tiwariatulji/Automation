from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
Options = Options()
Options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
