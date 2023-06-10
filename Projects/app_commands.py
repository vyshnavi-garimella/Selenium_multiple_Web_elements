from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
#APPLICATION COMMANDS
# driver.get("https://www.facebook.com/")
# driver.maximize_window
# print("Title is ", driver.title)
# print(driver.current_url)
# #print(driver.page_source)
# driver.close()  #close current window
# driver.quit() # closed the browser shutdown chrome driver

#CONDITIONAL COMMANDS
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
displayed=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(displayed.is_displayed())         # it will see whether the element isdisplayed or not

enabled=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(enabled.is_enabled()) 
enableed=driver.find_element(By.XPATH,"//input[@id='Email']")
print(enableed.is_enabled())# it will be used to check whether it is enabled to make modications like typing in the search box

selected=driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(selected.is_selected())       # used to check wheter radio button is selected or not

#BROWSER COMMANDS
