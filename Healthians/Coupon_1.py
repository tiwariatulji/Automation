import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # ब्राउज़र सेटअप
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # ब्राउज़र बंद करना
    driver.quit()

def test_create_coupon(driver):
    # वेबसाइट पर जाएं
    driver.get("https://www.healthians.com")
    
    # एलिमेंट्स के लिए प्रतीक्षा सेट करें
    wait = WebDriverWait(driver, 10)
    
    # कैम्पेन चुनें
    campaign_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='Select Campaign']")))
    Select(campaign_dropdown).select_by_visible_text("Your Desired Campaign")

    # कूपन शुरू होने की तारीख
    start_date = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Coupon Start Date']")))
    start_date.send_keys("2023-12-20")

    # कूपन समाप्ति तारीख
    end_date = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Coupon End Date']")))
    end_date.send_keys("2023-12-30")

    # सैंपल कलेक्शन शुरू होने की तारीख
    sample_start = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Sample Collection Start Date']")))
    sample_start.send_keys("2023-12-21")

    # सैंपल कलेक्शन समाप्ति तारीख
    sample_end = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Sample Collection End Date']")))
    sample_end.send_keys("2023-12-31")

    # छूट का प्रकार
    discount_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Fixed']")))
    discount_type.click()

    # क्या आप मल्टीपल स्लैब चाहते हैं?
    multiple_slab = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Do You Want For Multiple Slab' and @value='Yes']")))
    multiple_slab.click()

    # छूट की राशि
    discount_amount = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Discount Amount']")))
    discount_amount.send_keys("100")

    # न्यूनतम बुकिंग मूल्य
    min_booking = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Min Booking Value']")))
    min_booking.send_keys("500")

    # किस प्लेटफॉर्म पर इस कूपन का उपयोग करें?
    platform_checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@name='Which Platform use this Coupon']")))
    for checkbox in platform_checkboxes:
        checkbox.click()

    # कूपन जोड़ें बटन
    add_coupon_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Coupon']")))
    add_coupon_button.click()

    # कूपन सफलतापूर्वक बनाया गया है या नहीं, इसकी जांच करें
    # उदाहरण के लिए:
    # assert "Coupon created successfully" in driver.page_source