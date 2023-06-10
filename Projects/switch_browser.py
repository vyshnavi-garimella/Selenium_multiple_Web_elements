from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(3)
windows=driver.window_handles

for i in windows:
    driver.switch_to.window(i)
    print("title of the page is", driver.title)
