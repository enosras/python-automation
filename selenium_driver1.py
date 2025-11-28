from selenium import webdriver
import time

#driver = webdriver.Safari('./safaridriver')


driver = webdriver.Firefox()
url = "http://127.0.0.1:8080"
x = driver.get(url)

print(x)
#help(driver)

#print(driver.get.__doc__)
#driver.get("http://Users/enos/phptest/phpmysql.html")

'''
print("testing")
time.sleep(10)
driver.quit()
#sleep(10)

'''
