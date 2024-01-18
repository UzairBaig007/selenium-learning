from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()
browser.get('https://demoqa.com/automation-practice-form')
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/input").send_keys("Uzair")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[4]/input").send_keys("Baig")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").send_keys("uzair.baig@maqsoodlabs.com")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").send_keys("uzair.baig@maqsoodlabs.com")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").send_keys("uzair.baig@maqsoodlabs.com")


