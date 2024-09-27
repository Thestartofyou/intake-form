from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace 'your_chrome_driver_path' with the actual path to your ChromeDriver
driver = webdriver.Chrome(executable_path="your_chrome_driver_path")

# Open the doctor's intake form webpage
driver.get("https://www.example.com/intake-form")  # Replace with the actual URL of the form

# Add a wait to ensure the page is fully loaded
time.sleep(2)  # Adjust this based on the website's loading time

# Example fields to autofill (adjust these selectors according to the form)
patient_name = driver.find_element(By.ID, "patient_name")  # Replace 'ID' with the actual form element ID or use By.NAME, By.CLASS_NAME, etc.
patient_name.send_keys("John Doe")

dob_field = driver.find_element(By.ID, "dob")  # Date of Birth field
dob_field.send_keys("01/01/1990")

address_field = driver.find_element(By.ID, "address")
address_field.send_keys("123 Main St, Springfield")

phone_field = driver.find_element(By.ID, "phone_number")
phone_field.send_keys("555-123-4567")

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("johndoe@example.com")

# Example of a dropdown field
insurance_dropdown = driver.find_element(By.ID, "insurance_provider")
insurance_dropdown.send_keys(Keys.ARROW_DOWN)  # Adjust this depending on the dropdown options
insurance_dropdown.send_keys(Keys.RETURN)

# Checkboxes or radio buttons (if applicable)
agree_checkbox = driver.find_element(By.ID, "agree_terms")
agree_checkbox.click()

# Submit the form
submit_button = driver.find_element(By.ID, "submit_button")
submit_button.click()

# Wait to see the result before closing the browser
time.sleep(5)  # Adjust if necessary

# Close the browser
driver.quit()
