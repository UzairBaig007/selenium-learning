import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://demoqa.com/progress-bar')
browser.maximize_window()

def simple():
    browser.find_element(By.ID, 'startStopButton').click()
    time.sleep(4)
    browser.find_element(By.ID, 'startStopButton').click()
    time.sleep(4)
    browser.find_element(By.ID, 'startStopButton').click()
    time.sleep(4)
    browser.find_element(By.ID, 'startStopButton').click()
    time.sleep(10)

def second():
    browser.find_element(By.ID, 'startStopButton').click()
    time.sleep(6)
    browser.find_element(By.ID, 'startStopButton').click()
    bar = browser.find_element(By.ID, 'progressBar')
    print(bar.text)
    time.sleep(5)

def third():
    time.sleep(5)
    start = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "startStopButton")))
    start.click()
    print("hello")
    while True:
        bar = browser.find_element(By.ID, 'progressBar')
        progress = bar.text
        if progress == '50%':
            browser.find_element(By.ID, 'startStopButton').click()
            print(progress)
            time.sleep(3)
            # browser.find_element(By.ID, 'startStopButton').click()
            start = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "startStopButton")))
            start.click()
            while True:
                bar = browser.find_element(By.ID, 'progressBar')
                progress = bar.text
                if progress == '80%':
                    browser.find_element(By.ID, 'startStopButton').click()
                    print(progress)
                    time.sleep(3)
                    browser.find_element(By.ID,'startStopButton').click()
                    time.sleep(3)
                    browser.find_element(By.ID, 'resetButton').click()
                    browser.quit()
                    break


def forth():
    start = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "startStopButton")))
    start.click()
    while True:
        bar = browser.find_element(By.ID, 'progressBar')
        progress = bar.text
        if progress == '50%':
            browser.find_element(By.ID, 'startStopButton').click()
            print(progress)
            time.sleep(3)
            break

def fifth():
    start = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "startStopButton")))
    start.click()
    while True:
        bar = browser.find_element(By.ID, 'progressBar')
        progress = bar.text
        if progress == '80%':
            browser.find_element(By.ID, 'startStopButton').click()
            print(progress)
            time.sleep(3)
            break







# simple()
# second()
# third()
forth()
fifth()