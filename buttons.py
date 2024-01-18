import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get("https://demoqa.com/buttons")
browser.maximize_window()
time.sleep(4)

def doubleclick():
    element = browser.find_element(By.ID, "doubleClickBtn")
    actions = ActionChains(browser)
    actions.double_click(element).perform()
    time.sleep(2)
    actual_rslt = browser.find_element(By.ID, "doubleClickMessage")
    rslt = actual_rslt.text
    print(rslt)
    expected_result = "You have done a double click"
    if expected_result == rslt:
        print("Double Click test case is passed")
    else:
        print("Double Click test case is fail")

def rightclick():
    element2 = browser.find_element(By.ID, "rightClickBtn")
    actions = ActionChains(browser)
    actions.context_click(element2).perform()
    time.sleep(2)
    actual_rslt = browser.find_element(By.ID, "rightClickMessage")
    rslt = actual_rslt.text
    print(rslt)
    expected_result = "You have done a right click"
    if expected_result == rslt:
        print("Right Click test case is passed")
    else:
        print("Right Click test case is fail")

def click():
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button").click()
    time.sleep(5)
    actual_rslt = browser. find_element(By.ID,"dynamicClickMessage")
    rslt = actual_rslt.text
    print(rslt)
    expected_result = "You have done a dynamic click"
    if expected_result == rslt:
        print("Click test case is passed")
    else:
        print("Click test case is fail")


doubleclick()
rightclick()
click()




