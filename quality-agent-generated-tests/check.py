
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize test report variables
passed_tests = 0
failed_tests = 0

# Configure WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.maximize_window()

# Base URL
base_url = "https://lease-management-service-729496874389.us-central1.run.app/"

def take_screenshot(test_step_description):
    """Takes a screenshot and saves it with the test step description."""
    try:
        driver.save_screenshot(f'error_screenshot_{test_step_description}.png')
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def test_case_tc_tenant_01():
    """Test Case ID: TC_TENANT_01
    Test Case Description: Create a new tenant with valid data
    """
    global passed_tests, failed_tests
    try:
        # Step 1: Click on "Add Tenant" button
        driver.get(base_url)
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
        )
        add_tenant_button.click()
        time.sleep(0.5)

        # Step 2: Enter valid first name in "First Name" field
        first_name_field = driver.find_element(By.ID, "first_name")
        first_name_field.send_keys("John")
        time.sleep(0.5)

        # Step 3: Enter valid last name in "Last Name" field
        last_name_field = driver.find_element(By.ID, "last_name")
        last_name_field.send_keys("Doe")
        time.sleep(0.5)

        # Step 4: Enter valid contact number in "Contact Number" field
        contact_number_field = driver.find_element(By.ID, "contact_number")
        contact_number_field.send_keys("1234567890")
        time.sleep(0.5)

        # Step 5: Enter valid email address in "Email" field
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Step 6: Click on "Add Tenant" button
        add_tenant_button = driver.find_element(By.XPATH, "//button[text()='Add Tenant']")
        add_tenant_button.click()
        time.sleep(0.5)

        # Assertion: Verify tenant is created and displayed in the Tenants table
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]/tbody"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        assert len(tenant_rows) > 0, "Tenant not created or not displayed in the table"

        passed_tests += 1
        print(f"Test Case TC_TENANT_01 - Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_01 - Failed: {e}")
        take_screenshot("TC_TENANT_01_Step_6")

def test_case_tc_tenant_02():
    """Test Case ID: TC_TENANT_02
    Test Case Description: Create a new tenant with invalid data - empty first name
    """
    global passed_tests, failed_tests
    try:
        # Step 1: Click on "Add Tenant" button
        driver.get(base_url)
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
        )
        add_tenant_button.click()
        time.sleep(0.5)

        # Step 2: Leave "First Name" field empty
        # (No action needed, field is already empty)

        # Step 3: Enter valid last name in "Last Name" field
        last_name_field = driver.find_element(By.ID, "last_name")
        last_name_field.send_keys("Doe")
        time.sleep(0.5)

        # Step 4: Enter valid contact number in "Contact Number" field
        contact_number_field = driver.find_element(By.ID, "contact_number")
        contact_number_field.send_keys("1234567890")
        time.sleep(0.5)

        # Step 5: Enter valid email address in "Email" field
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Step 6: Click on "Add Tenant" button
        add_tenant_button = driver.find_element(By.XPATH, "//button[text()='Add Tenant']")
        add_tenant_button.click()
        time.sleep(0.5)

        # Assertion: Verify error message is displayed for empty first name field
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'form-group')]//div[contains(@class, 'invalid-feedback')]"))
        )
        assert error_message.text == "First Name is required", "Error message not displayed or incorrect"

        passed_tests += 1
        print(f"Test Case TC_TENANT_02 - Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_02 - Failed: {e}")
        take_screenshot("TC_TENANT_02_Step_6")

def test_case_tc_tenant_03():
    """Test Case ID: TC_TENANT_03
    Test Case Description: Create a new tenant with invalid data - invalid email address
    """
    global passed_tests, failed_tests
    try:
        # Step 1: Click on "Add Tenant" button
        driver.get(base_url)
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
        )
        add_tenant_button.click()
        time.sleep(0.5)

        # Step 2: Enter valid first name in "First Name" field
        first_name_field = driver.find_element(By.ID, "first_name")
        first_name_field.send_keys("John")
        time.sleep(0.5)

        # Step 3: Enter valid last name in "Last Name" field
        last_name_field = driver.find_element(By.ID, "last_name")
        last_name_field.send_keys("Doe")
        time.sleep(0.5)

        # Step 4: Enter valid contact number in "Contact Number" field
        contact_number_field = driver.find_element(By.ID, "contact_number")
        contact_number_field.send_keys("1234567890")
        time.sleep(0.5)

        # Step 5: Enter invalid email address in "Email" field
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("john.doe.example.com")
        time.sleep(0.5)

        # Step 6: Click on "Add Tenant" button
        add_tenant_button = driver.find_element(By.XPATH, "//button[text()='Add Tenant']")
        add_tenant_button.click()
        time.sleep(0.5)

        # Assertion: Verify error message is displayed for invalid email address
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'form-group')]//div[contains(@class, 'invalid-feedback')]"))
        )
        assert error_message.text == "Please enter a valid email address", "Error message not displayed or incorrect"

        passed_tests += 1
        print(f"Test Case TC_TENANT_03 - Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_03 - Failed: {e}")
        take_screenshot("TC_TENANT_03_Step_6")

def test_case_tc_tenant_04():
    """Test Case ID: TC_TENANT_04
    Test Case Description: Create a new tenant with invalid data - invalid contact number
    """
    global passed_tests, failed_tests
    try:
        # Step 1: Click on "Add Tenant" button
        driver.get(base_url)
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
        )
        add_tenant_button.click()
        time.sleep(0.5)

        # Step 2: Enter valid first name in "First Name" field
        first_name_field = driver.find_element(By.ID, "first_name")
        first_name_field.send_keys("John")
        time.sleep(0.5)

        # Step 3: Enter valid last name in "Last Name" field
        last_name_field = driver.find_element(By.ID, "last_name")
        last_name_field.send_keys("Doe")
        time.sleep(0.5)

        # Step 4: Enter invalid contact number in "Contact Number" field
        contact_number_field = driver.find_element(By.ID, "contact_number")
        contact_number_field.send_keys("123456789")
        time.sleep(0.5)

        # Step 5: Enter valid email address in "Email" field
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Step 6: Click on "Add Tenant" button
        add_tenant_button = driver.find_element(By.XPATH, "//button[text()='Add Tenant']")
        add_tenant_button.click()
        time.sleep(0.5)

        # Assertion: Verify error message is displayed for invalid contact number
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'form-group')]//div[contains(@class, 'invalid-feedback')]"))
        )
        assert error_message.text == "Please enter a valid contact number", "Error message not displayed or incorrect"

        passed_tests += 1
        print(f"Test Case TC_TENANT_04 - Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_04 - Failed: {e}")
        take_screenshot("TC_TENANT_04_Step_6")

def test_case_tc_tenant_05():
    """Test Case ID: TC_TENANT_05
    Test Case Description: Cancel tenant creation
    """
    global passed_tests, failed_tests
    try:
        # Step 1: Click on "Add Tenant" button
        driver.get(base_url)
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
        )
        add_tenant_button.click()
        time.sleep(0.5)

        # Step 2: Enter valid first name in "First Name" field
        first_name_field = driver.find_element(By.ID, "first_name")
        first_name_field.send_keys("John")
        time.sleep(0.5)

        # Step 3: Enter valid last name in "Last Name" field
        last_name_field = driver.find_element(By.ID, "last_name")
        last_name_field.send_keys("Doe")
        time.sleep(0.5)

        # Step 4: Click on "Cancel" button
        cancel_button = driver.find_element(By.XPATH, "//button[text()='Cancel']")
        cancel_button.click()
        time.sleep(0.5)

        # Assertion: Verify Add New Tenant screen is closed and user is redirected to the main screen
        assert driver.current_url == base_url, "User not redirected to the main screen"

        passed_tests += 1
        print(f"Test Case TC_TENANT_05 - Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_05 - Failed: {e}")
        take_screenshot("TC_TENANT_05_Step_4")

# Run test cases
test_case_tc_tenant_01()
test_case_tc_tenant_02()
test_case_tc_tenant_03()
test_case_tc_tenant_04()
test_case_tc_tenant_05()

# Generate test report
print(f"\nTest Report:")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

# Close the browser
driver.quit()