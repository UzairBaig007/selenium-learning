import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://www.daraz.pk/')
browser.maximize_window()
time.sleep(3)
browser.find_element(By.ID,'q').send_keys("Mobile")
time.sleep(2)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[2]/button').click()
time.sleep(5)

dropdown = browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div')
dropdown.click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, "[data-spm-click='gostr=/lzdse.result.sort;locaid=d4']").click()
time.sleep(5)
browser.find_element(By.ID, 'id-title').click()
time.sleep(10)
browser.find_element(By.CSS_SELECTOR,"a[class='next-number-picker-handler next-number-picker-handler-up ']").click()
actual_price = browser.find_element(By.CSS_SELECTOR,'span[class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]')
print(actual_price.text)
expected_price = "Rs. 399"
if actual_price.text == expected_price:
    print("passed")
else:
    print("fail")

browser.find_element(By.CSS_SELECTOR, 'button[class="add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl"]').click()
time.sleep(10)

