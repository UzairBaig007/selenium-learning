from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get('https://demoqa.com/frames')

def first_iframe():
    browser.switch_to.frame(browser.find_element(By.ID, 'frame1'))
    msg = browser.find_element(By.ID, 'sampleHeading')
    print(msg.text)
    if msg.text == "This is a sample page":
        print("first ifrmae is passed")
    else:
        print("fail")


def scnd_iframe():
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element(By.ID, 'frame2'))
    msg = browser.find_element(By.ID, 'sampleHeading')
    print(msg.text)
    if msg.text == "This is a sample page":
        print("second ifrmae is passed")
    else:
        print("fail")






first_iframe()
scnd_iframe()
time.sleep(5)