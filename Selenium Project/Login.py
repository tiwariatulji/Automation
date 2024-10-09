from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://web.fiatcs.com/')

# browser.close()  # Close the current window
browser.quit()  # Close the browser and all associated windows

# ==================================================================================================

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get('https://web.fiatcs.com/web/landing/login')
assert 'fiatcs' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('fiatcs' + Keys.RETURN)


browser.quit()