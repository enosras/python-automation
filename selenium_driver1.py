from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("http://Users/enos/phptest/phpmysql.html")


print("testing")
time.sleep(10)
driver.quit()
#sleep(10)
