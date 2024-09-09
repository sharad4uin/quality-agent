
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
driver.implicitly_wait(0.5)

# Test Case 1: Create a new tenant with valid data
def test_case_1():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter valid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is created successfully
        if driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr//td[text()='John']").is_displayed():
            print("Test Case 1: Passed")
            passed_tests += 1
        else:
            print("Test Case 1: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_1.png")
    except Exception as e:
        print(f"Test Case 1: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_1.png")
        print(f"Error: {e}")

# Test Case 2: Create a new tenant with invalid data - empty first name
def test_case_2():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'First Name is required')]").is_displayed():
            print("Test Case 2: Passed")
            passed_tests += 1
        else:
            print("Test Case 2: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_2.png")
    except Exception as e:
        print(f"Test Case 2: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_2.png")
        print(f"Error: {e}")

# Test Case 3: Create a new tenant with invalid data - invalid email address
def test_case_3():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Invalid email address')]").is_displayed():
            print("Test Case 3: Passed")
            passed_tests += 1
        else:
            print("Test Case 3: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_3.png")
    except Exception as e:
        print(f"Test Case 3: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_3.png")
        print(f"Error: {e}")

# Test Case 4: Create a new tenant with invalid data - special characters in first name
def test_case_4():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John!")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Invalid first name')]").is_displayed():
            print("Test Case 4: Passed")
            passed_tests += 1
        else:
            print("Test Case 4: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_4.png")
    except Exception as e:
        print(f"Test Case 4: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_4.png")
        print(f"Error: {e}")

# Test Case 5: Create a new tenant with invalid data - special characters in last name
def test_case_5():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe!")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Invalid last name')]").is_displayed():
            print("Test Case 5: Passed")
            passed_tests += 1
        else:
            print("Test Case 5: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_5.png")
    except Exception as e:
        print(f"Test Case 5: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_5.png")
        print(f"Error: {e}")

# Test Case 6: Create a new tenant with invalid data - invalid contact number
def test_case_6():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("123456789")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Invalid contact number')]").is_displayed():
            print("Test Case 6: Passed")
            passed_tests += 1
        else:
            print("Test Case 6: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_6.png")
    except Exception as e:
        print(f"Test Case 6: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_6.png")
        print(f"Error: {e}")

# Test Case 7: Cancel tenant creation
def test_case_7():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter valid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Verify Add New Tenant screen is closed
        if driver.current_url == base_url:
            print("Test Case 7: Passed")
            passed_tests += 1
        else:
            print("Test Case 7: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_7.png")
    except Exception as e:
        print(f"Test Case 7: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_7.png")
        print(f"Error: {e}")

# Test Case 8: Create a new tenant with existing email address
def test_case_8():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Email address already exists')]").is_displayed():
            print("Test Case 8: Passed")
            passed_tests += 1
        else:
            print("Test Case 8: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_8.png")
    except Exception as e:
        print(f"Test Case 8: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_8.png")
        print(f"Error: {e}")

# Test Case 9: Create a new tenant with existing contact number
def test_case_9():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe1@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Contact number already exists')]").is_displayed():
            print("Test Case 9: Passed")
            passed_tests += 1
        else:
            print("Test Case 9: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_9.png")
    except Exception as e:
        print(f"Test Case 9: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_9.png")
        print(f"Error: {e}")

# Test Case 10: Create a new tenant with empty last name
def test_case_10():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe2@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify error message is displayed
        if driver.find_element(By.XPATH, "//div[@class='form-group']//div[contains(text(), 'Last Name is required')]").is_displayed():
            print("Test Case 10: Passed")
            passed_tests += 1
        else:
            print("Test Case 10: Failed")
            failed_tests += 1
            driver.save_screenshot("error_screenshot_test_case_10.png")
    except Exception as e:
        print(f"Test Case 10: Failed")
        failed_tests += 1
        driver.save_screenshot("error_screenshot_test_case_10.png")
        print(f"Error: {e}")

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