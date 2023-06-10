from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://www.facebook.com/")
driver.maximize_window()
# using name
driver.find_element(By.NAME,"email").send_keys("123@email")
driver.find_element(By.NAME,"pass").send_keys("123")

#using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()

#using tag name 
anchor_tags=driver.find_elements(By.TAG_NAME,"a")
print(len(anchor_tags))

#CSS SELECTORS
#using tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("123@email")
#                        (OR) tag is optional...only with id 
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("123@email")

# using tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("123@email")
#                         (OR) tag is optional...only with class
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("123@email")  

#using tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("123@email")    
#                         (OR) tag is optional...only with attribute           
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("123@email") 

# using tag class attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("123@email") 
#                         (OR) tag is optional...only with class & attribute 
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("123@email") 
time.sleep(3)