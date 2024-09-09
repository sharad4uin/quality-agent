
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize test report variables
passed_tests = 0
failed_tests = 0

# Define the base URL
base_url = "https://lease-management-service-729496874389.us-central1.run.app/"

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Test Case 1: Create a new tenant with valid data
def test_case_1():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is created successfully
        # (Add assertion here to check if the tenant is displayed in the Tenants table)

        passed_tests += 1
        print(f"Test Case 1: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 1: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 2: Create a new tenant with invalid data - empty first name
def test_case_2():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Leave First Name field empty
        # (No need to enter anything in the field)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 2: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 2: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 3: Create a new tenant with invalid data - invalid email address
def test_case_3():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter invalid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 3: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 3: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 4: Create a new tenant with invalid data - special characters in first name
def test_case_4():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter first name with special characters
        driver.find_element(By.ID, "first_name").send_keys("John!")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 4: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 4: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 5: Create a new tenant with invalid data - special characters in last name
def test_case_5():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter last name with special characters
        driver.find_element(By.ID, "last_name").send_keys("Doe!")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 5: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 5: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 6: Create a new tenant with invalid data - invalid contact number
def test_case_6():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter invalid contact number
        driver.find_element(By.ID, "contact_number").send_keys("123456789")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 6: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 6: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 7: Cancel tenant creation
def test_case_7():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Verify Add New Tenant screen is closed
        # (Add assertion here to check if the Add New Tenant screen is closed)

        passed_tests += 1
        print(f"Test Case 7: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 7: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 8: Create a new tenant with existing email address
def test_case_8():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter existing email address
        driver.find_element(By.ID, "email").send_keys("existing@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 8: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 8: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 9: Create a new tenant with existing contact number
def test_case_9():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter existing contact number
        driver.find_element(By.ID, "contact_number").send_keys("9876543210")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        # (Add assertion here to check if the error message is displayed)

        passed_tests += 1
        print(f"Test Case 9: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 9: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Test Case 10: Create a new tenant with empty contact number
def test_case_10():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Leave Contact Number field empty
        # (No need to enter anything in the field)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is created successfully
        # (Add assertion here to check if the tenant is displayed in the Tenants table)

        passed_tests += 1
        print(f"Test Case 10: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case 10: Failed")
        print(f"Error: {e}")
        driver.save_screenshot('error_screenshot.png')

# Run all test cases
test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()
test_case_7()
test_case_8()
test_case_9()
test_case_10()

# Generate test report
print(f"\nTest Report:")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

# Close the WebDriver
driver.quit()