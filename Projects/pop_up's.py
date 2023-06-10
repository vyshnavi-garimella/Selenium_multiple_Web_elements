from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(20)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("welcome")

alertwindow.accept() # means OK
#alertwindow.dismiss()# means cancel
time.sleep(10)


# driver.get("https://mypage.rediff.com/login")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@id='remember']").click()
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
# alertwindow=driver.switch_to.alert
# print(alertwindow.text)
# alertwindow.accept()
# time.sleep(10)