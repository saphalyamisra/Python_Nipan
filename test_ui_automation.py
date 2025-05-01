import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.google.com/"

search_bar_xpath = "//*[@name='q']"
search_text = "saphalya misra linkedin"
search_button_xpath = '(//*[@value="Google Search" and @name="btnK"])[2]'
linkedin_text = "//*[text()='Saphalya Misra - Linux System Administrator']"

@pytest.mark.ui_nipan
def test_ui_google():
    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(2)
    search_field = driver.find_element(By.XPATH, search_bar_xpath)
    search_field.send_keys(search_text)
    search_btn = driver.find_element(By.XPATH, search_button_xpath)
    time.sleep(2)
    search_btn.click()
    time.sleep(5)
    input("Solve the robot captcha and then press any key...")
    time.sleep(30)
    driver.find_element(By.XPATH, linkedin_text).click()
    driver.save_screenshot("profile.png")


