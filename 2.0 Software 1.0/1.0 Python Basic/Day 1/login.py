from selenium import webdriver
from selenium.webdriver.common.by import By
import time

while True:
    driver = webdriver.Chrome()
    driver.get('https://www.ubastudent.online/')
    time.sleep(2)  # Wait for page to load

    # Close the popup if present
    try:
        close_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-danger')
        close_btn.click()
        print("Popup closed.")
        time.sleep(1)
    except Exception as e:
        print("No popup to close:", e)

    # Find all elements with class 'form-control'
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input.input-lg.form-control.fg-input')

    # Find username and password fields by ID or NAME
    try:
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('UBa23PB033')
        password.send_keys('Junior07')
    except Exception as e:
        print("Could not find username or password field:", e)

    # Find and click the submit button
    try:
        submit_btn = driver.find_element(By.TAG_NAME, 'button')
        submit_btn.click()
    except Exception as e:
        print("Submit button not found:", e)

    input("Press Enter to close the browser...")

    driver.quit()

    # Ask if user wants to run again
    again = input("Run again? (y/n): ")
    if again.lower() != 'y':
        break