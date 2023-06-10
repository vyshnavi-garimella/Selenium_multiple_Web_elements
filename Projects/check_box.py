from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
#driver.find_element(By.XPATH,"//input[@id='monday']").click()
time.sleep(3)

# checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# print(len(checkboxs))

#checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# for i in range(len(checkboxs)):
#     checkboxs[i].click()

# checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# for i in checkboxs:
#     i.click()
#time.sleep(3)

#selecting checboxes bases on id's
# checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# for i in checkboxs:
#     weekname=i.get_attribute('id')
#     if weekname=='monday' or weekname=='friday':
#         i.click()
#time.sleep(3)        

#selecting required checkboxes
# checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# for i in range(len(checkboxs)):
#     if i>len(checkboxs)-3:
#         checkboxs[i].click()
#time.sleep(3)

# checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
# for i in range(len(checkboxs)):
#     if i>2:
#         checkboxs[i].click()
# time.sleep(3)

#clearing checkboxes if selected
checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id ,'day')]")
for i in checkboxs:
    i.click()
for i in checkboxs:
    if i.is_selected():
        i.click()

time.sleep(7)