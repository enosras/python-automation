from selenium import webdriver
import time

driver = webdriver.Safari('./safaridriver')

driver.get("http://Users/enos/phptest/phpmysql.html")


print("testing")
time.sleep(10)
driver.quit()
#sleep(10)
