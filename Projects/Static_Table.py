from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(10)
#count number of rows
no_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th"))
print(no_of_rows)
print(no_of_columns)

#read sepcific element
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[1]").text
time.sleep(10)
print(data)

#read all table data
for i in range(2,no_of_rows): #range starts from 1
    for j in range(1,no_of_columns):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(data,end=" ")
    print()

#getting speciic data match
for i in range(2,no_of_rows+1): #range starts from 1
    for j in range(1,no_of_columns+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        if data=="Mukesh":
            bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j-1)+"]").text
            print(bookname)