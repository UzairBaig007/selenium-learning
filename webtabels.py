from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()
browser.get("https://demoqa.com/webtables")
time.sleep(5)

def add():
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/button").click()
    time.sleep(6)
    # browser.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/form/div[1]/div[2]/input").send_keys("Uzair")
    browser.find_element(By.ID, "firstName").send_keys("Uzair")
    browser.find_element(By.ID, "lastName").send_keys("Baig")
    browser.find_element(By.ID, "userEmail").send_keys("uzair.baig@maqsoodlabs.com")
    browser.find_element(By.ID, "age").send_keys("25")
    browser.find_element(By.ID, "salary").send_keys("50000")
    browser.find_element(By.ID, "department").send_keys("QA")
    browser.find_element(By.ID, "submit").click()

def edit():
    time.sleep(5)
    browser.find_element(By.ID, "edit-record-4").click()
    time.sleep(3)
    browser.find_element(By.ID, "department").clear()
    browser.find_element(By.ID, "department").send_keys("Quality Assurance")
    browser.find_element(By.ID, "submit").click()

def search_delete():
    time.sleep(10)
    browser.find_element(By.ID, "searchBox").send_keys("uzair")
    time.sleep(5)
    browser.find_element(By.ID, "delete-record-4").click()
    time.sleep(10)



add()
edit()
search_delete()