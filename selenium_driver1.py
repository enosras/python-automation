from selenium import webdriver
import time
import requests
#from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions


#cookies_dict = {}
#used this link for testing cookies retrieval and other selenium functions
#chose this url because it is my alma mater site and I am familiar with it, however i was blocked by the fire wall eventually

url = "https://www.starbucks.com/"

timer = 2
#url = "http://localhost:8080"
driver = webdriver.Safari('./safaridriver')

print("still alive")
#driver = webdriver.Firefox()

#x = driver.get(url)

#y = driver.get_network_conditions()
#print(y)

#print(x)
#help(driver)

#print(driver.get.__doc__)
driver.get(url)
driver.set_window_size(800, 600)
#driver.maximize_window()
time.sleep(timer)

#help(driver.get_cookies()) 
#response = requests.get(url, cookies=cookies_dict)
cookies_dict = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
print("Cookies Dict:", cookies_dict)
print("Cookies:", driver.get_cookies())

with open('cookies.txt', 'a') as f:
    for cookie in driver.get_cookies():
        f.write(f"{cookie}\n")

#capturing only specific cookie
with open('specific_cookie.txt', 'a') as f:
        session_data = driver.session_id
        
        f.write(f"{session_data}\n")
        x = 1
        for i, k in cookies_dict.items():
            f.write(f"{x} - {i}: {k}\n")
            x += 1


# Testing page refresh
driver.refresh()

# Taking a screenshot
driver.save_screenshot('homepage.png')

#options  VirtualAuthenticatorOptions(protocol="u2f", transport="usb")
#driver.add_virtual_authenticator(options)

print(driver.session_id)
time.sleep(timer)
driver.quit()

'''
print("testing")
time.sleep(10)
driver.quit()
#sleep(10)

'''
