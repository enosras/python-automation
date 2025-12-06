from selenium import webdriver
import time
import requests


#cookies_dict = {}
#used this link for testing cookies retrieval and other selenium functions
#chose this url because it is my alma mater site and I am familiar with it

url = "https://www.usiu.ac.ke"
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
cookies_dict = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
print("Cookies Dict:", cookies_dict)
print("Cookies:", driver.get_cookies())

with open('cookies.txt', 'w') as f:
    for cookie in driver.get_cookies():
        f.write(f"{cookie}\n")

#capturing only specific cookie
with open('specific_cookie.txt', 'w') as f:
    
        x = 0
        for i in cookies_dict:
            f.write(f"item {x} {i}\n")
            x += 1



# Testing page refresh
driver.refresh()


time.sleep(5)
driver.quit()

'''
print("testing")
time.sleep(10)
driver.quit()
#sleep(10)

'''
