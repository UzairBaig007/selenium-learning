from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

browser = webdriver.Chrome()

browser.get('https://demoqa.com/alerts')
browser.maximize_window()
popup = Alert(browser)

# browser.find_element(By.CSS_SELECTOR, 'button[id="alertButton"]').click()
# time.sleep(3)
# alert = Alert(browser)
# alert.accept()
# time.sleep(5)


def first():
    browser.find_element(By.CSS_SELECTOR, 'button[id="alertButton"]').click()
    # popup = Alert(browser)
    popup.accept()
    time.sleep(5)

def scndalert():
    browser.find_element(By.CSS_SELECTOR, 'button[id="timerAlertButton"]').click()
    time.sleep(10)
    # popup = Alert(browser)
    popup.accept()
    time.sleep(10)

def third_ok():
    browser.find_element(By.CSS_SELECTOR, 'button[id="confirmButton"]').click()
    # popup = Alert(browser)
    popup.accept()
    time.sleep(5)
    msg = browser.find_element(By.CSS_SELECTOR,'span[id="confirmResult"]')

    assert msg.text in "You selected Ok"
    if msg.text == "You selected Ok":
        print("You selected Ok is passed")
    else:
        print("fail")



def third_cancel():
    browser.find_element(By.CSS_SELECTOR, 'button[id="confirmButton"]').click()
    # popup = Alert(browser)
    popup.dismiss()
    time.sleep(5)
    msg = browser.find_element(By.CSS_SELECTOR, 'span[id="confirmResult"]')
    assert msg.text in "You selected Cancel"
    if msg.text == "You selected Cancel":
        print("You selected cancel is passed")
    else:
        print("fail")


def forth():
    browser.find_element(By.CSS_SELECTOR, 'button[id="promtButton"]').click()
    # popup = Alert(browser)
    popup.send_keys('Uzair Baig')
    popup.accept()
    time.sleep(5)
    # browser.find_element(By.CSS_SELECTOR, 'button[id="promtButton"]').click()
    # popup.dismiss()

    msg = browser.find_element(By.CSS_SELECTOR, 'span[id="promptResult"]')
    assert msg.text in "You entered Uzair Baig"
    if msg.text == "You entered Uzair Baig":
        print("Name validation pass")
    else:
        print("fail")





first()
scndalert()
third_ok()
third_cancel()
forth()
