import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#url_global = "http://[::]:8000/enos_dynamic.html"
#url_global = "http://127.0.0.1:8080"
url_global = "https://www.google.com"
text_title = "Delayed remove of an object"



class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get(url_global)

    def test_page_title(self):
        expected_title = text_title
        self.assertEqual(self.driver.title, expected_title, "Page title mismatch")

    def test_heading_text(self):
        #self.driver.implicitly_wait(2)
        heading_element = self.driver.find_element(By.TAG_NAME, "div")
        #heading_element = self.driver.find_element
        self.assertEqual(heading_element.text, "SIU HEALTH CENTR", "Heading text mismatch")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    y = By.__doc__
    print(y)
    #x= scrape_tool.test_page_title()
    #print(f'TEST RESULTS : {x}')
    unittest.main()
    

    
