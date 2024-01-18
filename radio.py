import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://demoqa.com/radio-button")

browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/label").click()
time.sleep(5)
#browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/label").click()
act_rslt = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p/span")
text_content = act_rslt.text
print(text_content)

expected_rslt = "Yes"

#time.sleep(10)

if text_content==expected_rslt:
    print("test is passed")
else:
    print("test is failed")