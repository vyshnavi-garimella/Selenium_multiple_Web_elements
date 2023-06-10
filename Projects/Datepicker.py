from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
year="2023"
month="July"
date="20"
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
time.sleep(10)

Dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for i in Dates:
    if i.text==date:
        i.click()
        break
time.sleep(10)