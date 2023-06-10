from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.chrome.service import Service
# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable-notifications")
# ser_obj=Service("C:\\Users\\ngarimella2\\sel_py\\chromedriver.exe")
date="23"
# driver=webdriver.Chrome(service=ser_obj,options=ops)
driver=webdriver.Chrome()
driver.get("https://www.ixigo.com/flights?utm_source=Google_Search&utm_medium=paid_search_google&utm_campaign=Generic_Search_Feb23_NewUserGGL&gclid=Cj0KCQjw4NujBhC5ARIsAF4Iv6fDXt2wsv7IbvlSZMFAklDa-MZzxBwx69tjfXFTeuAZt-VpuEr0QA0aArKtEALw_wcB")
driver.maximize_window()
# alertwindow=driver.switch_to.alert
# alertwindow.dismiss()# means cancel
time.sleep(10)
driver.find_element(By.XPATH,"(//input[@placeholder='Enter city or airport'])[1]").send_keys("HYD-Hyderabad")
time.sleep(4)
driver.find_element(By.XPATH,"(//input[@placeholder='Enter city or airport'])[2]").send_keys("DEL-NEW DELHI")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Depart']").click()
time.sleep(3)
mon=driver.find_element(By.XPATH,"(//div[@class='rd-month-label'])[1]").text
time.sleep(5)
#driver.find_element(By.XPATH,"(//*[@class='rd-day-body trip-date'])[1]").text
print(mon)
date_to_select = driver.find_element(By.XPATH, "//div[@class='date-picker']//td[text()='25']")
date_to_select.click()
# Dates=driver.find_element(By.XPATH,"//*[@class='rd-days']//tr/td")
# Dates.click()
    
