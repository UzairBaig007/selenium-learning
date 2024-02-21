from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome()
browser.get('https://demoqa.com/automation-practice-form')
browser.maximize_window()
#browser.execute_script("document.body.style.zoom='50%'")
time.sleep(5)
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/input").send_keys("Uzair")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[4]/input").send_keys("Baig")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").send_keys("uzair.baig@maqsoodlabs.com")

browser.implicitly_wait(10)
browser.execute_script("document.querySelector('input[id=gender-radio-1]').click()")
# time.sleep(20)
#browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/label").click()
browser.find_element(By.ID, "userNumber").send_keys("3364399157")
#Date of birth
time.sleep(1)
browser.find_element(By.ID, 'dateOfBirthInput').click()
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[99]').click()
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[12]').click()
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]').click()
# #Date of birth

element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subjects-auto-complete__input>input[id="subjectsInput"][type="text"]')))
element.send_keys("Math")
element.send_keys(Keys.ENTER)



time.sleep(10)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[1]').click()
s=browser.find_element(By.ID,'uploadPicture')
s.send_keys("C:/test/sampleFile.jpeg")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[9]/div[2]/textarea").send_keys("145A Maqsoodlabs Airline society")


dropdown = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='react-select-3-input']")))
dropdown.send_keys("NCR")
dropdown.send_keys(Keys.ENTER)
time.sleep(10)

dropdown2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='react-select-4-input']")))
dropdown2.send_keys("Delhi")
dropdown2.send_keys(Keys.ENTER)

time.sleep(10)
element.submit()
# submitbtn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='submit']")))
# submitbtn.click()

#browser.find_element(By.CSS_SELECTOR,"button[id='submit']").click()
time.sleep(5)
