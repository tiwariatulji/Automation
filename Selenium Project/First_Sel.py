# from selenium import webdriver

# driver = webdriver.Chrome() # Launch Chrome browser
# # webdriver.Chrome() is a method which launch chrome browser
# driver.get("www.youtube.com")
# # get() method is used to open the URL in the browser
# # driver.implicitly_wait(10) # Wait for 10 seconds to load the page
# # driver.maximize_window() # Maximize the browser window

# ------------- No need chrome driver for python if python version is above 4.5 -----------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
# from selenium_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service("chromeDriverManager().install()"))

# webdriver = webdriver.Chrome(service=Service("C:\chromedriver-win64\chromedriver-win64\chromedriver.exe") )

webdriver = webdriver.Chrome()
# Access the website
webdriver.get("https://www.healthians.com/")
webdriver.implicitly_wait(30)