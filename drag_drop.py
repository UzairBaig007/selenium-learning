import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get('https://demoqa.com/droppable')
browser.maximize_window()
time.sleep(10)
def simple():
    drag_from = browser.find_element(By.ID, 'draggable')
    drag_to = browser.find_element(By.ID, 'droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(drag_from, drag_to).perform()
    # message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]')
    # print(message.text)
    # assert message.text in "Dropped!"
    # if message.text == "Dropped!":
    #     print("pass")
    # else:
    #     print("fail")

def Accept():
    browser.find_element(By.ID, 'droppableExample-tab-accept').click()

    time.sleep(3)
    # drag_from = WebDriverWait(browser,15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]")))
    # drag_to = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]")))
    drag_from = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]')
    drag_to = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]')
    drag_notacceptable = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]')
    actions = ActionChains(browser)
    actions.drag_and_drop(drag_notacceptable, drag_to).perform()
    time.sleep(3)
    actions.drag_and_drop(drag_from, drag_to).perform()
    drop_message = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]')
    print(drop_message.text)
    assert drop_message.text in "Dropped!"
    if drop_message.text == "Dropped!":
        print("pass")
    else:
        print("fail")

def prevent():
    browser.find_element(By.ID,'droppableExample-tab-preventPropogation').click()
    # browser.execute_script("document.body.style.zoom='75%'")
    time.sleep(5)
    drag_from = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[1]')
    drag_to = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/p')
    drag_to_inner = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]')
    drag_to_inner_dropable = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/p')
    drag_to_outer_dropable = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/p')

    actions = ActionChains(browser)
    actions.drag_and_drop(drag_from, drag_to).perform()
    time.sleep(4)
    dropto_message = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/p')
    print(dropto_message.text)
    assert dropto_message.text in "Dropped!"
    if dropto_message.text == "Dropped!":
        print("outer droppable text message passed ")
    else:
        print("outer dropplable text message failed")

    actions.drag_and_drop(drag_from, drag_to_inner).perform()
    time.sleep(4)
    droptoinner_message = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/p')
    print(droptoinner_message.text)
    assert droptoinner_message.text in "Dropped!"
    if droptoinner_message.text == "Dropped!":
        print("inner droppable text message passed ")
    else:
        print("inner dropplable text message failed")

    actions.drag_and_drop(drag_from, drag_to_inner_dropable).perform()
    time.sleep(4)
    droptoinnerdropable_message = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/p')
    print(droptoinnerdropable_message.text)
    assert droptoinnerdropable_message.text in "Dropped!"
    if droptoinnerdropable_message.text == "Dropped!":
        print("inner greedy droppable text message passed ")
    else:
        print("inner greedy  dropplable text message failed")

    actions.drag_and_drop(drag_from, drag_to_outer_dropable).perform()
    time.sleep(3)
    droptoouterdropable_message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/p')
    print(droptoouterdropable_message.text)
    assert droptoouterdropable_message.text in "Dropped!"
    if droptoouterdropable_message.text == "Dropped!":
        print("outer greedy droppable text message passed ")
    else:
        print("outer greedy  dropplable text message failed")

def revert():
    browser.find_element(By.ID,'droppableExample-tab-revertable').click()
    time.sleep(3)
    drag_from = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/div[1]')
    drag_to = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]')

    actions = ActionChains(browser)
    actions.drag_and_drop(drag_from, drag_to).perform()
    time.sleep(3)
    browser.refresh()
    time.sleep(7)
    browser.find_element(By.ID, 'droppableExample-tab-revertable').click()
    drag_notrevertable = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/div[2]')
    destination = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/div[2]')

    actions.drag_and_drop(drag_notrevertable, destination).perform()
    time.sleep(5)




# simple()
# time.sleep(5)
# Accept()
# time.sleep(5)
# prevent()
# time.sleep(5)
revert()
time.sleep(3)
