# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()

# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# driver.switch_to.default_content() # goes back to main page

# driver.switch_to.frame("packageFrame")
# driver.find_element(By.XPATH,"//span[normalize-space()='Alert']").click()
# driver.switch_to.default_content()

# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/ul[1]/li[8]/a[1]").click()
# time.sleep(20)

# multiple iframes
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

