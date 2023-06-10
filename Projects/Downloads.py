from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd
def chrome_class():
    # from selenium.webdriver.chrome.service import Service
    # ser_obj=Service()
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(options=ops)
    # driver=webdriver.Chrome(service=ser_obj,options=ops)
    return driver

driver=chrome_class()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[3]/a").click()
