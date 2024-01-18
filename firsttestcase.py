#from selenium import webdriver
import time

# Set the path to your ChromeDriver executable
#chrome_driver_path = "C:\Drivers\chromedriver-win64\chromedriver.exe"

# Create a Chrome WebDriver instance using the specified path
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://demoqa.com/text-box")
browser.find_element(By.ID, "userName").send_keys("Muhammad Uzair")
time.sleep(10)
browser.find_element(By.ID,"userEmail").send_keys("uzair.baig@maqsoodlabs.com")
time.sleep(10)
#browser.find_element(By.CLASS_NAME,"mr-sm-2.form-control").send_keys("uzair.baig@maqsoodlabs.com")
browser.find_element(By.XPATH, "//*[@placeholder='Current Address']").send_keys("145A maqsoodlabs")
time.sleep(10)
#browser.find_element(By.ID, "currentAddress").send_keys("145A Maqsoodlabs")
browser.find_element(By.CSS_SELECTOR, "textarea[id='permanentAddress']").send_keys("Same address")

#browser.find_element(By.ID, "submit").click()
time.sleep(20)
#browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/button").click()
browser.find_element(By.CLASS_NAME,"btn-primary").click()

time.sleep(20)
browser.quit()




