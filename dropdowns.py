import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



browser = webdriver.Chrome()

browser.get('https://practice.cydeo.com/dropdown')
browser.maximize_window()

dropdown = Select(browser.find_element(By.ID, 'dropdown'))
dropdown.select_by_value('2')

year = Select(browser.find_element(By.ID, 'year'))
year.select_by_index(26)

month = Select(browser.find_element(By.ID,'month'))
month.select_by_visible_text('December')

date = Select(browser.find_element(By.ID,'day'))
date.select_by_value('11')

state = Select(browser.find_element(By.ID, 'state'))
state.select_by_visible_text("Arizona")

Language = Select(browser.find_element(By.CSS_SELECTOR,'Select[name="Languages"]'))
Language.select_by_visible_text('Python')
# Language.select_by_value('Python')
# time.sleep(5)

website = browser.find_element(By.ID, 'dropdownMenuLink')
website.click()

time.sleep(5)
browser.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/a[4]').click()

time.sleep(10)

