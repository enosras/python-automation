from selenium import webdriver
import time
import requests


cookies_dict = {}
url = "https://www.google.com"
#url = "http://localhost:8080"
driver = webdriver.Safari('./safaridriver')


#driver = webdriver.Firefox()

#x = driver.get(url)

#y = driver.get_network_conditions()
#print(y)

#print(x)
#help(driver)

#print(driver.get.__doc__)
driver.get(url)
driver.set_window_size(800, 800)
#driver.maximize_window()
time.sleep(5)

#help(driver.get_cookies()) 
#response = requests.get(url, cookies=cookies_dict)
print("Cookies:", driver.get_cookies())

driver.refresh()
time.sleep(5)
driver.quit()

'''
print("testing")
time.sleep(10)
driver.quit()
#sleep(10)

'''
