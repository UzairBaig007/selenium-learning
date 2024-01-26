import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://demoqa.com/browser-windows')


def newtab():
    browser.find_element(By.ID, 'tabButton').click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])

    element = browser.find_element(By.ID, 'sampleHeading')
    assert element.text == 'This is a sample page'
    if element.text == 'This is a sample page':
        print("new tab is passed")
    else:
        print("fail")

def newwindow():
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.ID, 'windowButton').click()
    browser.switch_to.window(browser.window_handles[2])
    # browser.maximize_window()
    newwin = browser.find_element(By.ID, 'sampleHeading')
    assert newwin.text in "This is a sample page"
    if newwin.text == "This is a sample page":
        print("new window validation passed")
    else:
        print("fail")
    time.sleep(5)



def newwindowmessage():
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.ID, 'messageWindowButton').click()
    browser.switch_to.window(browser.window_handles[3])
    time.sleep(2)
    # msg = browser.find_element(By.XPATH,'/html/body')
    # time.sleep(2)
    # newmsg = msg.text
    # print(newmsg)
    # assert msg.text in "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."
    # if msg.text == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.":
    #     print("message is passed ")
    # else:
    #     print("message is failed")
    time.sleep(5)
    browser.close()

def frames():
    browser.find_element(By.ID, 'messageWindowButton').click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)




newtab()
newwindow()
newwindowmessage()

time.sleep(5)
