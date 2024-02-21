from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://demoqa.com/nestedframes')

def outside_frame():
    msg = browser.find_element(By.CSS_SELECTOR,'div[id="framesWrapper"]')
    print(msg.text)


def parent_iframe():
    browser.switch_to.frame(browser.find_element(By.ID,'frame1'))
    print("inside parent frame")
    msg = browser.find_element(By.XPATH,'/html/body')
    print(msg.text)
    assert msg.text in "Parent frame"
    if msg.text == "Parent frame":
        print("parent test case pass")
    else:
        print("parent test case fail")

def child_frame():
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element(By.ID, 'frame1'))
    browser.switch_to.frame(browser.find_element(By.XPATH, '/html/body/iframe'))
    # print("inside child frame")
    msg = browser.find_element(By.XPATH,'/html/body')
    newmsg = msg.text
    print(newmsg)
    assert msg.text in "Child Iframe"
    if msg.text == "Child Iframe":
        print("Child test case is passed")
    else:
        print("Child test case is failed")


outside_frame()
parent_iframe()
child_frame()