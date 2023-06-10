from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(20)
driver.maximize_window()

drop_downs=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#selecting option using built in method
#drop_downs.select_by_visible_text("India")
#drop_downs.select_by_index(13)
#drop_downs.select_by_value("10")

time.sleep(20)

alloptions=drop_downs.options
print(len(alloptions)) # 244
for i in alloptions:
    print(i.text)

# selectiong using logic without built in function/methods
drop_downs=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
alloptions=drop_downs.options
for i in alloptions:
    if i.text=="India":
        i.click()
        break


drop_downs=Select(driver.find_element(By.XPATH,"//*[@id='input-country']/option"))
print(len(drop_downs))
