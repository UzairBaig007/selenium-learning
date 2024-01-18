from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://demoqa.com/links")
browser.maximize_window()
time.sleep(4)

def created():
    browser.find_element(By.ID, 'created').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '//*[@id="linkResponse"]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "201"
    if actual_rslt == expected_rslt:
        print("Test case is passed for created status code 201")
    else:
        print("Test case is fail")

def nocontent():
    browser.find_element(By.ID, 'no-content').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "204"
    if actual_rslt == expected_rslt:
        print("Test case is passed for no content status code 204")
    else:
        print("Test case is fail")


def Moved():
    browser.find_element(By.ID, 'moved').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "301"
    if actual_rslt == expected_rslt:
        print("Test case is passed for moved status code 301")
    else:
        print("Test case is fail")

def badrequest():
        browser.find_element(By.ID, 'bad-request').click()
        time.sleep(4)
        response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
        # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
        actual_rslt = response.text
        print(actual_rslt)
        expected_rslt = "400"
        if actual_rslt == expected_rslt:
            print("Test case is passed for the bad-request status code 400")
        else:
            print("Test case is fail")


def Unauthorized():
    browser.find_element(By.ID, 'unauthorized').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "401"
    if actual_rslt == expected_rslt:
        print("Test case is passed for the unauthorized status code 401")
    else:
        print("Test case is fail")
def Forbidden():
    browser.find_element(By.ID, 'forbidden').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "403"
    if actual_rslt == expected_rslt:
        print("Test case is passed for the forbidden status code 403")
    else:
        print("Test case is fail")

def Not_Found():
    browser.find_element(By.ID, 'invalid-url').click()
    time.sleep(4)
    response = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]/b[1]')
    # response =browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[10]')
    actual_rslt = response.text
    print(actual_rslt)
    expected_rslt = "404"
    if actual_rslt == expected_rslt:
        print("Test case is passed for the not found status code 404")
    else:
        print("Test case is fail")
def links():
    browser.find_element(By.LINK_TEXT, 'Home').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    browser.find_element(By.ID, 'dynamicLink').click()
    time.sleep(8)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(7)
    browser.close()
    time.sleep(10)
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(10)


links()
time.sleep(3)
created()
time.sleep(3)
nocontent()
time.sleep(3)
Moved()
time.sleep(3)
badrequest()
time.sleep(3)
Unauthorized()
time.sleep(3)
Forbidden()
time.sleep(3)
Not_Found()

browser.quit()