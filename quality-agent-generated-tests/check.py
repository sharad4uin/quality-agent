
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
driver.implicitly_wait(5)
driver.maximize_window()

# Define test cases
test_cases = [
    {
        "id": "TC_TENANT_01",
        "description": "Create a new tenant with valid data",
        "steps": [
            {"id": 1, "description": "Click on 'Add Tenant' button", "expected_result": "Add New Tenant screen is displayed"},
            {"id": 2, "description": "Enter valid first name in 'First Name' field", "expected_result": "First name is entered successfully"},
            {"id": 3, "description": "Enter valid last name in 'Last Name' field", "expected_result": "Last name is entered successfully"},
            {"id": 4, "description": "Enter valid contact number in 'Contact Number' field", "expected_result": "Contact number is entered successfully"},
            {"id": 5, "description": "Enter valid email address in 'Email' field", "expected_result": "Email address is entered successfully"},
            {"id": 6, "description": "Click on 'Add Tenant' button", "expected_result": "New tenant is created successfully and displayed in the Tenants table"}
        ]
    },
    {
        "id": "TC_TENANT_02",
        "description": "Create a new tenant with invalid data - empty first name",
        "steps": [
            {"id": 1, "description": "Click on 'Add Tenant' button", "expected_result": "Add New Tenant screen is displayed"},
            {"id": 2, "description": "Leave 'First Name' field empty", "expected_result": "Error message is displayed for empty first name field"},
            {"id": 3, "description": "Enter valid last name in 'Last Name' field", "expected_result": "Last name is entered successfully"},
            {"id": 4, "description": "Enter valid contact number in 'Contact Number' field", "expected_result": "Contact number is entered successfully"},
            {"id": 5, "description": "Enter valid email address in 'Email' field", "expected_result": "Email address is entered successfully"},
            {"id": 6, "description": "Click on 'Add Tenant' button", "expected_result": "Tenant is not created and error message is displayed"}
        ]
    },
    {
        "id": "TC_TENANT_03",
        "description": "Create a new tenant with invalid data - invalid email address",
        "steps": [
            {"id": 1, "description": "Click on 'Add Tenant' button", "expected_result": "Add New Tenant screen is displayed"},
            {"id": 2, "description": "Enter valid first name in 'First Name' field", "expected_result": "First name is entered successfully"},
            {"id": 3, "description": "Enter valid last name in 'Last Name' field", "expected_result": "Last name is entered successfully"},
            {"id": 4, "description": "Enter valid contact number in 'Contact Number' field", "expected_result": "Contact number is entered successfully"},
            {"id": 5, "description": "Enter invalid email address in 'Email' field", "expected_result": "Error message is displayed for invalid email address"},
            {"id": 6, "description": "Click on 'Add Tenant' button", "expected_result": "Tenant is not created and error message is displayed"}
        ]
    },
    {
        "id": "TC_TENANT_04",
        "description": "Create a new tenant with invalid data - invalid contact number",
        "steps": [
            {"id": 1, "description": "Click on 'Add Tenant' button", "expected_result": "Add New Tenant screen is displayed"},
            {"id": 2, "description": "Enter valid first name in 'First Name' field", "expected_result": "First name is entered successfully"},
            {"id": 3, "description": "Enter valid last name in 'Last Name' field", "expected_result": "Last name is entered successfully"},
            {"id": 4, "description": "Enter invalid contact number in 'Contact Number' field", "expected_result": "Error message is displayed for invalid contact number"},
            {"id": 5, "description": "Enter valid email address in 'Email' field", "expected_result": "Email address is entered successfully"},
            {"id": 6, "description": "Click on 'Add Tenant' button", "expected_result": "Tenant is not created and error message is displayed"}
        ]
    },
    {
        "id": "TC_TENANT_05",
        "description": "Cancel tenant creation",
        "steps": [
            {"id": 1, "description": "Click on 'Add Tenant' button", "expected_result": "Add New Tenant screen is displayed"},
            {"id": 2, "description": "Enter valid first name in 'First Name' field", "expected_result": "First name is entered successfully"},
            {"id": 3, "description": "Enter valid last name in 'Last Name' field", "expected_result": "Last name is entered successfully"},
            {"id": 4, "description": "Click on 'Cancel' button", "expected_result": "Add New Tenant screen is closed and user is redirected to the main screen"}
        ]
    }
]

# Run test cases
for test_case in test_cases:
    print(f"Running test case: {test_case['id']} - {test_case['description']}")
    driver.get("https://lease-management-service-729496874389.us-central1.run.app/")
    
    for step in test_case['steps']:
        try:
            # Execute test step
            if step['description'] == "Click on 'Add Tenant' button":
                add_tenant_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
                )
                add_tenant_button.click()
                time.sleep(0.5)
            elif step['description'] == "Enter valid first name in 'First Name' field":
                first_name_field = driver.find_element(By.ID, "first_name")
                first_name_field.send_keys("John")
                time.sleep(0.5)
            elif step['description'] == "Enter valid last name in 'Last Name' field":
                last_name_field = driver.find_element(By.ID, "last_name")
                last_name_field.send_keys("Doe")
                time.sleep(0.5)
            elif step['description'] == "Enter valid contact number in 'Contact Number' field":
                contact_number_field = driver.find_element(By.ID, "contact_number")
                contact_number_field.send_keys("1234567890")
                time.sleep(0.5)
            elif step['description'] == "Enter valid email address in 'Email' field":
                email_field = driver.find_element(By.ID, "email")
                email_field.send_keys("john.doe@example.com")
                time.sleep(0.5)
            elif step['description'] == "Leave 'First Name' field empty":
                first_name_field = driver.find_element(By.ID, "first_name")
                first_name_field.clear()
                time.sleep(0.5)
            elif step['description'] == "Enter invalid email address in 'Email' field":
                email_field = driver.find_element(By.ID, "email")
                email_field.send_keys("invalid_email")
                time.sleep(0.5)
            elif step['description'] == "Enter invalid contact number in 'Contact Number' field":
                contact_number_field = driver.find_element(By.ID, "contact_number")
                contact_number_field.send_keys("invalid_number")
                time.sleep(0.5)
            elif step['description'] == "Click on 'Add Tenant' button":
                add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
                add_tenant_button.click()
                time.sleep(0.5)
            elif step['description'] == "Click on 'Cancel' button":
                cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                time.sleep(0.5)

            # Verify expected result
            if step['description'] == "Add New Tenant screen is displayed":
                assert "Add New Tenant" in driver.title, f"Test step {step['id']} failed: Add New Tenant screen is not displayed"
            elif step['description'] == "First name is entered successfully":
                assert first_name_field.get_attribute("value") == "John", f"Test step {step['id']} failed: First name is not entered successfully"
            elif step['description'] == "Last name is entered successfully":
                assert last_name_field.get_attribute("value") == "Doe", f"Test step {step['id']} failed: Last name is not entered successfully"
            elif step['description'] == "Contact number is entered successfully":
                assert contact_number_field.get_attribute("value") == "1234567890", f"Test step {step['id']} failed: Contact number is not entered successfully"
            elif step['description'] == "Email address is entered successfully":
                assert email_field.get_attribute("value") == "john.doe@example.com", f"Test step {step['id']} failed: Email address is not entered successfully"
            elif step['description'] == "Error message is displayed for empty first name field":
                error_message = driver.find_element(By.XPATH, "//div[@class='form-group'][1]/div").text
                assert "First Name is required" in error_message, f"Test step {step['id']} failed: Error message for empty first name field is not displayed"
            elif step['description'] == "Error message is displayed for invalid email address":
                error_message = driver.find_element(By.XPATH, "//div[@class='form-group'][4]/div").text
                assert "Invalid email address" in error_message, f"Test step {step['id']} failed: Error message for invalid email address is not displayed"
            elif step['description'] == "Error message is displayed for invalid contact number":
                error_message = driver.find_element(By.XPATH, "//div[@class='form-group'][3]/div").text
                assert "Invalid contact number" in error_message, f"Test step {step['id']} failed: Error message for invalid contact number is not displayed"
            elif step['description'] == "New tenant is created successfully and displayed in the Tenants table":
                # Add assertion logic to verify tenant creation
                # Example: Check if the tenant's name is displayed in the table
                pass
            elif step['description'] == "Tenant is not created and error message is displayed":
                # Add assertion logic to verify tenant creation failure
                # Example: Check if an error message is displayed
                pass
            elif step['description'] == "Add New Tenant screen is closed and user is redirected to the main screen":
                assert "Lease Management" in driver.title, f"Test step {step['id']} failed: Add New Tenant screen is not closed"

            print(f"Test step {step['id']} passed")
            passed_tests += 1

        except Exception as e:
            print(f"Test step {step['id']} failed")
            failed_tests += 1
            # Take screenshot
            screenshot_name = f"error_screenshot_{test_case['id']}_{step['id']}.png"
            driver.save_screenshot(screenshot_name)
            # Log error message
            error_message = getattr(e, 'msg', repr(e))
            print(f"Error: {error_message}")

# Generate test report
print("\nTest Report:")
print(f"Passed tests: {passed_tests}")
print(f"Failed tests: {failed_tests}")

# Close WebDriver
driver.quit()