from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.innovatewithseed.com')

time.sleep(2)  # Wait for page to load

# Get page title
print("Title:", driver.title)

# Get first <h1>
try:
    h1 = driver.find_element(By.TAG_NAME, 'h1')
    print("First <h1>:", h1.text)
except Exception as e:
    print("No <h1> found:", e)

# Get first <p>
try:
    p = driver.find_element(By.TAG_NAME, 'p')
    print("First <p>:", p.text)
except Exception as e:
    print("No <p> found:", e)

driver.quit()