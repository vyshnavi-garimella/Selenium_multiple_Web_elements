from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()
time.sleep(10)
text1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
text2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
text1.send_keys("I'm happy")
time.sleep(5)
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(5)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
time.sleep(4)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
