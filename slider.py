import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://demoqa.com/slider')
browser.maximize_window()

slider = browser.find_element(By.CSS_SELECTOR, 'input[type="range"]')

move = ActionChains(browser)
# move.click_and_hold(slider).move_by_offset(3, 0).release().perform()
# time.sleep(5)
# move.click_and_hold(slider).move_by_offset(180, 0).release().perform()
# time.sleep(5)
# move.click_and_hold(slider).move_by_offset(500, 0).release().perform()
# time.sleep(10)
move.click_and_hold(slider).move_by_offset(87, 0).release().perform()
time.sleep(5)