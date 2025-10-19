import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get("http://127.0.0.1:8080")

    def test_page_title(self):
        expected_title = "usiu"
        self.assertEqual(self.driver.title, expected_title, "Page title mismatch")

    def test_heading_text(self):
        heading_element = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(heading_element.text, "Example Domain", "Heading text mismatch")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
