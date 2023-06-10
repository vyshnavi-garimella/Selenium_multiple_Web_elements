#broken links
import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

links=driver.find_elements(By.TAG_NAME,'a')
count=0

for i in links:
    url=i.get_attribute('href')
    res=requests.head(url)
    if res.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url, " is valid link")