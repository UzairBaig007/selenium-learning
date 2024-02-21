import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://demoqa.com/date-picker')

# date_pick.clear()
#
# time.sleep(4)
#
# dob_date = "11/12/1998"
# date_pick.send_keys(dob_date)

desired_date = "December 1998"

def date():
    date_pick = browser.find_element(By.ID, 'datePickerMonthYearInput')
    date_pick.click()
    while True:
        month = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]')
        print(month.text)
        if desired_date == month.text:
            break
        else:
            browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/button[1]').click()

    browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]').click()

def date_time():
    browser.find_element(By.ID, 'dateAndTimePickerInput').click()
    while True:
        months = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]')
        # print(months.text)
        if desired_date == months.text:
            break
        else:
            # print("something")
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/button[1]').click()


    browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]').click()
    browser.find_element(By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[5]').click()



date()
date_time()

time.sleep(10)