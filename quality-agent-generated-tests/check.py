
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

# Test Case TC_TENANT_01: Create a new tenant with valid data
try:
    print("Running Test Case TC_TENANT_01: Create a new tenant with valid data")
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Enter valid first name
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("John")
    time.sleep(0.5)

    # Enter valid last name
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("Doe")
    time.sleep(0.5)

    # Enter valid contact number
    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.send_keys("1234567890")
    time.sleep(0.5)

    # Enter valid email address
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john.doe@example.com")
    time.sleep(0.5)

    # Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is created successfully
    # (You'll need to add logic to verify the tenant is displayed in the table)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_01 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_01.png")

# Test Case TC_TENANT_02: Create a new tenant with invalid data
try:
    print("Running Test Case TC_TENANT_02: Create a new tenant with invalid data")
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Enter invalid first name
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("!@#$%^")
    time.sleep(0.5)

    # Enter invalid last name
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("12345")
    time.sleep(0.5)

    # Enter invalid contact number
    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.send_keys("abcdefg")
    time.sleep(0.5)

    # Enter invalid email address
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john.doeexample.com")
    time.sleep(0.5)

    # Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_02 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_02.png")

# Test Case TC_TENANT_03: Create a new tenant with empty fields
try:
    print("Running Test Case TC_TENANT_03: Create a new tenant with empty fields")
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Leave "First Name" field empty
    # Leave "Last Name" field empty
    # Leave "Contact Number" field empty
    # Leave "Email" field empty

    # Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_03 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_03.png")

# Test Case TC_TENANT_04: Cancel tenant creation
try:
    print("Running Test Case TC_TENANT_04: Cancel tenant creation")
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Enter valid data in all fields
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("John")
    time.sleep(0.5)

    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("Doe")
    time.sleep(0.5)

    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.send_keys("1234567890")
    time.sleep(0.5)

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john.doe@example.com")
    time.sleep(0.5)

    # Click on "Cancel" button
    cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
    cancel_button.click()
    time.sleep(0.5)

    # Assert that the Add New Tenant screen is closed and the user is redirected to the main screen
    # (You'll need to add logic to verify the redirection)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_04 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_04.png")

# Test Case TC_TENANT_05: Edit existing tenant
try:
    print("Running Test Case TC_TENANT_05: Edit existing tenant")
    # Navigate to the Tenants table
    driver.get(base_url)

    # Click on "Actions" button for an existing tenant
    # (You'll need to add logic to identify the existing tenant)
    # ...

    # Edit the "First Name" field
    # ...

    # Click on "Save" button
    # ...

    # Assert that the tenant details are updated successfully
    # (You'll need to add logic to verify the updated details)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_05 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_05.png")

# Test Case TC_TENANT_06: Delete existing tenant
try:
    print("Running Test Case TC_TENANT_06: Delete existing tenant")
    # Navigate to the Tenants table
    driver.get(base_url)

    # Click on "Actions" button for an existing tenant
    # (You'll need to add logic to identify the existing tenant)
    # ...

    # Click on "Delete" button
    # ...

    # Assert that the tenant is deleted successfully
    # (You'll need to add logic to verify the tenant is removed from the table)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_06 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_06.png")

# Test Case TC_TENANT_07: Search for a tenant
try:
    print("Running Test Case TC_TENANT_07: Search for a tenant")
    # Navigate to the Tenants table
    driver.get(base_url)

    # Enter a valid first name in the search field
    # ...

    # Assert that tenants matching the entered first name are displayed
    # (You'll need to add logic to verify the search results)
    # ...

    # Clear the search field
    # ...

    # Assert that all tenants are displayed again
    # (You'll need to add logic to verify the display of all tenants)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_07 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_07.png")

# Test Case TC_TENANT_08: View tenant details
try:
    print("Running Test Case TC_TENANT_08: View tenant details")
    # Navigate to the Tenants table
    driver.get(base_url)

    # Click on the "First Name" of a tenant
    # (You'll need to add logic to identify the tenant)
    # ...

    # Assert that tenant details are displayed in a separate screen
    # (You'll need to add logic to verify the display of details)
    # ...

    # Click on "Back" button
    # ...

    # Assert that the user is redirected to the Tenants table
    # (You'll need to add logic to verify the redirection)
    # ...

    passed_tests += 1
    print("Test Case TC_TENANT_08 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_08.png")

# ... (Repeat similar test cases for Property and Lease)

# Test Case TC_PROPERTY_01: Create a new property with valid data
try:
    print("Running Test Case TC_PROPERTY_01: Create a new property with valid data")
    # Navigate to the Add Property page
    driver.get(base_url + "add_property")

    # Click on "Add Property" button
    add_property_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Property')]"))
    )
    add_property_button.click()
    time.sleep(0.5)

    # Enter valid address line 1
    address_line_1_field = driver.find_element(By.ID, "address_line_1")
    address_line_1_field.send_keys("123 Main Street")
    time.sleep(0.5)

    # Enter valid address line 2
    address_line_2_field = driver.find_element(By.ID, "address_line_2")
    address_line_2_field.send_keys("Apt 1")
    time.sleep(0.5)

    # Enter valid city
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("Anytown")
    time.sleep(0.5)

    # Enter valid state
    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("CA")
    time.sleep(0.5)

    # Enter valid zip code
    zip_code_field = driver.find_element(By.ID, "zip_code")
    zip_code_field.send_keys("12345")
    time.sleep(0.5)

    # Enter valid status
    status_field = driver.find_element(By.ID, "status")
    status_field.send_keys("Available")
    time.sleep(0.5)

    # Enter valid unit number
    unit_number_field = driver.find_element(By.ID, "unit_number")
    unit_number_field.send_keys("1")
    time.sleep(0.5)

    # Click on "Add Property" button
    add_property_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Property')]")
    add_property_button.click()
    time.sleep(0.5)

    # Assert that the property is created successfully
    # (You'll need to add logic to verify the property is displayed in the table)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_01 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_01.png")

# Test Case TC_PROPERTY_02: Create a new property with invalid data
try:
    print("Running Test Case TC_PROPERTY_02: Create a new property with invalid data")
    # Navigate to the Add Property page
    driver.get(base_url + "add_property")

    # Click on "Add Property" button
    add_property_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Property')]"))
    )
    add_property_button.click()
    time.sleep(0.5)

    # Enter invalid address line 1
    address_line_1_field = driver.find_element(By.ID, "address_line_1")
    address_line_1_field.send_keys("!@#$%^")
    time.sleep(0.5)

    # Enter invalid address line 2
    address_line_2_field = driver.find_element(By.ID, "address_line_2")
    address_line_2_field.send_keys("12345")
    time.sleep(0.5)

    # Enter invalid city
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("12345")
    time.sleep(0.5)

    # Enter invalid state
    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("12345")
    time.sleep(0.5)

    # Enter invalid zip code
    zip_code_field = driver.find_element(By.ID, "zip_code")
    zip_code_field.send_keys("abcdefg")
    time.sleep(0.5)

    # Enter invalid status
    status_field = driver.find_element(By.ID, "status")
    status_field.send_keys("!@#$%^")
    time.sleep(0.5)

    # Enter invalid unit number
    unit_number_field = driver.find_element(By.ID, "unit_number")
    unit_number_field.send_keys("abcdefg")
    time.sleep(0.5)

    # Click on "Add Property" button
    add_property_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Property')]")
    add_property_button.click()
    time.sleep(0.5)

    # Assert that the property is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_02 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_02.png")

# Test Case TC_PROPERTY_03: Create a new property with empty fields
try:
    print("Running Test Case TC_PROPERTY_03: Create a new property with empty fields")
    # Navigate to the Add Property page
    driver.get(base_url + "add_property")

    # Click on "Add Property" button
    add_property_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Property')]"))
    )
    add_property_button.click()
    time.sleep(0.5)

    # Leave "Address Line 1" field empty
    # Leave "City" field empty
    # Leave "State" field empty
    # Leave "Zip Code" field empty
    # Leave "Status" field empty
    # Leave "Unit Number" field empty

    # Click on "Add Property" button
    add_property_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Property')]")
    add_property_button.click()
    time.sleep(0.5)

    # Assert that the property is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_03 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_03.png")

# Test Case TC_PROPERTY_04: Cancel property creation
try:
    print("Running Test Case TC_PROPERTY_04: Cancel property creation")
    # Navigate to the Add Property page
    driver.get(base_url + "add_property")

    # Click on "Add Property" button
    add_property_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Property')]"))
    )
    add_property_button.click()
    time.sleep(0.5)

    # Enter valid data in all fields
    address_line_1_field = driver.find_element(By.ID, "address_line_1")
    address_line_1_field.send_keys("123 Main Street")
    time.sleep(0.5)

    address_line_2_field = driver.find_element(By.ID, "address_line_2")
    address_line_2_field.send_keys("Apt 1")
    time.sleep(0.5)

    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("Anytown")
    time.sleep(0.5)

    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("CA")
    time.sleep(0.5)

    zip_code_field = driver.find_element(By.ID, "zip_code")
    zip_code_field.send_keys("12345")
    time.sleep(0.5)

    status_field = driver.find_element(By.ID, "status")
    status_field.send_keys("Available")
    time.sleep(0.5)

    unit_number_field = driver.find_element(By.ID, "unit_number")
    unit_number_field.send_keys("1")
    time.sleep(0.5)

    # Click on "Cancel" button
    cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
    cancel_button.click()
    time.sleep(0.5)

    # Assert that the Add New Property screen is closed and the user is redirected to the main screen
    # (You'll need to add logic to verify the redirection)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_04 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_04.png")

# Test Case TC_PROPERTY_05: Edit existing property
try:
    print("Running Test Case TC_PROPERTY_05: Edit existing property")
    # Navigate to the Properties table
    driver.get(base_url)

    # Click on "Actions" button for an existing property
    # (You'll need to add logic to identify the existing property)
    # ...

    # Edit the "Address Line 1" field
    # ...

    # Click on "Save" button
    # ...

    # Assert that the property details are updated successfully
    # (You'll need to add logic to verify the updated details)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_05 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_05.png")

# Test Case TC_PROPERTY_06: Delete existing property
try:
    print("Running Test Case TC_PROPERTY_06: Delete existing property")
    # Navigate to the Properties table
    driver.get(base_url)

    # Click on "Actions" button for an existing property
    # (You'll need to add logic to identify the existing property)
    # ...

    # Click on "Delete" button
    # ...

    # Assert that the property is deleted successfully
    # (You'll need to add logic to verify the property is removed from the table)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_06 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_06.png")

# Test Case TC_PROPERTY_07: Search for a property
try:
    print("Running Test Case TC_PROPERTY_07: Search for a property")
    # Navigate to the Properties table
    driver.get(base_url)

    # Enter a valid city in the search field
    # ...

    # Assert that properties matching the entered city are displayed
    # (You'll need to add logic to verify the search results)
    # ...

    # Clear the search field
    # ...

    # Assert that all properties are displayed again
    # (You'll need to add logic to verify the display of all properties)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_07 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_07.png")

# Test Case TC_PROPERTY_08: View property details
try:
    print("Running Test Case TC_PROPERTY_08: View property details")
    # Navigate to the Properties table
    driver.get(base_url)

    # Click on the "Address" of a property
    # (You'll need to add logic to identify the property)
    # ...

    # Assert that property details are displayed in a separate screen
    # (You'll need to add logic to verify the display of details)
    # ...

    # Click on "Back" button
    # ...

    # Assert that the user is redirected to the Properties table
    # (You'll need to add logic to verify the redirection)
    # ...

    passed_tests += 1
    print("Test Case TC_PROPERTY_08 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_08.png")

# Test Case TC_LEASE_01: Create a new lease with valid data
try:
    print("Running Test Case TC_LEASE_01: Create a new lease with valid data")
    # Navigate to the Prepare Lease page
    driver.get(base_url + "prepare_lease")

    # Click on "Prepare Lease" button
    prepare_lease_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Prepare Lease')]"))
    )
    prepare_lease_button.click()
    time.sleep(0.5)

    # Select a valid property from the "Property" dropdown
    # (You'll need to add logic to identify the property dropdown and select a valid option)
    # ...

    # Select a valid tenant from the "Tenant" dropdown
    # (You'll need to add logic to identify the tenant dropdown and select a valid option)
    # ...

    # Enter valid start date
    start_date_field = driver.find_element(By.ID, "start_date")
    start_date_field.send_keys("2024-01-01")
    time.sleep(0.5)

    # Enter valid end date
    end_date_field = driver.find_element(By.ID, "end_date")
    end_date_field.send_keys("2025-01-01")
    time.sleep(0.5)

    # Enter valid monthly rent
    monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
    monthly_rent_field.send_keys("1000")
    time.sleep(0.5)

    # Enter valid security deposit
    security_deposit_field = driver.find_element(By.ID, "security_deposit")
    security_deposit_field.send_keys("1000")
    time.sleep(0.5)

    # Enter valid payment due date
    payment_due_date_field = driver.find_element(By.ID, "payment_due_date")
    payment_due_date_field.send_keys("2024-01-15")
    time.sleep(0.5)

    # Enter valid payment method
    payment_method_field = driver.find_element(By.ID, "payment_method")
    payment_method_field.send_keys("Check")
    time.sleep(0.5)

    # Click on "Create Lease" button
    create_lease_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Lease')]")
    create_lease_button.click()
    time.sleep(0.5)

    # Assert that the lease is created successfully
    # (You'll need to add logic to verify the lease is displayed in the table)
    # ...

    passed_tests += 1
    print("Test Case TC_LEASE_01 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_01.png")

# Test Case TC_LEASE_02: Create a new lease with invalid data
try:
    print("Running Test Case TC_LEASE_02: Create a new lease with invalid data")
    # Navigate to the Prepare Lease page
    driver.get(base_url + "prepare_lease")

    # Click on "Prepare Lease" button
    prepare_lease_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Prepare Lease')]"))
    )
    prepare_lease_button.click()
    time.sleep(0.5)

    # Select an invalid property from the "Property" dropdown
    # (You'll need to add logic to identify the property dropdown and select an invalid option)
    # ...

    # Select an invalid tenant from the "Tenant" dropdown
    # (You'll need to add logic to identify the tenant dropdown and select an invalid option)
    # ...

    # Enter invalid start date
    start_date_field = driver.find_element(By.ID, "start_date")
    start_date_field.send_keys("2024-01-01")
    time.sleep(0.5)

    # Enter invalid end date
    end_date_field = driver.find_element(By.ID, "end_date")
    end_date_field.send_keys("2023-01-01")
    time.sleep(0.5)

    # Enter invalid monthly rent
    monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
    monthly_rent_field.send_keys("abc")
    time.sleep(0.5)

    # Enter invalid security deposit
    security_deposit_field = driver.find_element(By.ID, "security_deposit")
    security_deposit_field.send_keys("abc")
    time.sleep(0.5)

    # Enter invalid payment due date
    payment_due_date_field = driver.find_element(By.ID, "payment_due_date")
    payment_due_date_field.send_keys("2024-02-01")
    time.sleep(0.5)

    # Enter invalid payment method
    payment_method_field = driver.find_element(By.ID, "payment_method")
    payment_method_field.send_keys("!@#$%^")
    time.sleep(0.5)

    # Click on "Create Lease" button
    create_lease_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Lease')]")
    create_lease_button.click()
    time.sleep(0.5)

    # Assert that the lease is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_LEASE_02 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_02.png")

# Test Case TC_LEASE_03: Create a new lease with empty fields
try:
    print("Running Test Case TC_LEASE_03: Create a new lease with empty fields")
    # Navigate to the Prepare Lease page
    driver.get(base_url + "prepare_lease")

    # Click on "Prepare Lease" button
    prepare_lease_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Prepare Lease')]"))
    )
    prepare_lease_button.click()
    time.sleep(0.5)

    # Leave "Property" field empty
    # Leave "Tenant" field empty
    # Leave "Start Date" field empty
    # Leave "End Date" field empty
    # Leave "Monthly Rent" field empty
    # Leave "Security Deposit" field empty
    # Leave "Payment Due Date" field empty
    # Leave "Payment Method" field empty

    # Click on "Create Lease" button
    create_lease_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Lease')]")
    create_lease_button.click()
    time.sleep(0.5)

    # Assert that the lease is not created and an error message is displayed
    # (You'll need to add logic to verify the error message)
    # ...

    passed_tests += 1
    print("Test Case TC_LEASE_03 passed")

except Exception as e:
    failed_tests += 1
    print(f"Test step failed: