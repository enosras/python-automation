#I have this for practice. Using generative AI to master some automation principles

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import configparser

# Initialize the Chrome WebDriver
# Using ChromeDriverManager to automatically handle driver installation
service = Service(SafariDriverManager().install())
driver = webdriver.Safari(service=service)


try:
    # Navigate to a website
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Assert the title of the page
    assert "Web form" in driver.title

    # Find the text input element by its name
    text_box = driver.find_element(By.NAME, "my-text")

    # Find the submit button by its tag name
    submit_button = driver.find_element(By.TAG_NAME, "button")

    # Type text into the input field
    text_box.send_keys("Selenium is awesome!")

    # Click the submit button
    submit_button.click()

    # Find the message element after submission
    message_element = driver.find_element(By.ID, "message")

    # Assert that the message confirms submission
    assert "Received!" in message_element.text

    print("Test passed: Form submitted successfully.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()
