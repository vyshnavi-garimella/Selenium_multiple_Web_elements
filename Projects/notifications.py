# disabling notifications like location notifications(allow ..block)
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ser_obj=Service("C:\Users\ngarimella2\sel_py\chromedriver.exe")

driver=webdriver.Chrome(service=ser_obj,options=ops)
driver.get("https://www.gps-coordinates.net/my-location")
driver.maximize_window()
