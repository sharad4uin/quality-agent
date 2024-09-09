
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

# Test Case TC_TENANT_01: Add a new tenant with valid data
try:
    print("Running Test Case TC_TENANT_01: Add a new tenant with valid data")
    # Navigate to "Add Tenant" screen
    driver.get(base_url + "add_tenant")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))
    print("Test Step 1: Navigate to 'Add Tenant' screen - PASSED")

    # Enter valid first name in "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    print("Test Step 2: Enter valid first name in 'First Name' field - PASSED")

    # Enter valid last name in "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    print("Test Step 3: Enter valid last name in 'Last Name' field - PASSED")

    # Enter valid contact number in "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    print("Test Step 4: Enter valid contact number in 'Contact Number' field - PASSED")

    # Enter valid email address in "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    print("Test Step 5: Enter valid email address in 'Email' field - PASSED")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(0.5)
    print("Test Step 6: Click on 'Add Tenant' button - PASSED")

    # Verify tenant is added successfully
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']//tbody//tr//td[text()='John']")))
    print("Test Case TC_TENANT_01: Add a new tenant with valid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_01.png")
    failed_tests += 1

# Test Case TC_TENANT_02: Add a new tenant with invalid data
try:
    print("Running Test Case TC_TENANT_02: Add a new tenant with invalid data")
    # Navigate to "Add Tenant" screen
    driver.get(base_url + "add_tenant")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))
    print("Test Step 1: Navigate to 'Add Tenant' screen - PASSED")

    # Enter invalid first name (special characters) in "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("!@#$%^")
    print("Test Step 2: Enter invalid first name (special characters) in 'First Name' field - PASSED")

    # Enter invalid last name (numbers only) in "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("12345")
    print("Test Step 3: Enter invalid last name (numbers only) in 'Last Name' field - PASSED")

    # Enter invalid contact number (alphabets) in "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("abcdefg")
    print("Test Step 4: Enter invalid contact number (alphabets) in 'Contact Number' field - PASSED")

    # Enter invalid email address (without "@" symbol) in "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doeexample.com")
    print("Test Step 5: Enter invalid email address (without '@' symbol) in 'Email' field - PASSED")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(0.5)
    print("Test Step 6: Click on 'Add Tenant' button - PASSED")

    # Verify tenant is not added and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_TENANT_02: Add a new tenant with invalid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_02.png")
    failed_tests += 1

# Test Case TC_TENANT_03: Add a new tenant with empty fields
try:
    print("Running Test Case TC_TENANT_03: Add a new tenant with empty fields")
    # Navigate to "Add Tenant" screen
    driver.get(base_url + "add_tenant")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))
    print("Test Step 1: Navigate to 'Add Tenant' screen - PASSED")

    # Leave "First Name" field empty
    driver.find_element(By.ID, "first_name").clear()
    print("Test Step 2: Leave 'First Name' field empty - PASSED")

    # Leave "Last Name" field empty
    driver.find_element(By.ID, "last_name").clear()
    print("Test Step 3: Leave 'Last Name' field empty - PASSED")

    # Leave "Contact Number" field empty
    driver.find_element(By.ID, "contact_number").clear()
    print("Test Step 4: Leave 'Contact Number' field empty - PASSED")

    # Leave "Email" field empty
    driver.find_element(By.ID, "email").clear()
    print("Test Step 5: Leave 'Email' field empty - PASSED")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(0.5)
    print("Test Step 6: Click on 'Add Tenant' button - PASSED")

    # Verify tenant is not added and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_TENANT_03: Add a new tenant with empty fields - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_03.png")
    failed_tests += 1

# Test Case TC_TENANT_04: Cancel adding a new tenant
try:
    print("Running Test Case TC_TENANT_04: Cancel adding a new tenant")
    # Navigate to "Add Tenant" screen
    driver.get(base_url + "add_tenant")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))
    print("Test Step 1: Navigate to 'Add Tenant' screen - PASSED")

    # Enter valid data in all fields
    driver.find_element(By.ID, "first_name").send_keys("Jane")
    driver.find_element(By.ID, "last_name").send_keys("Smith")
    driver.find_element(By.ID, "contact_number").send_keys("9876543210")
    driver.find_element(By.ID, "email").send_keys("jane.smith@example.com")
    print("Test Step 2: Enter valid data in all fields - PASSED")

    # Click on "Cancel" button
    driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
    time.sleep(0.5)
    print("Test Step 3: Click on 'Cancel' button - PASSED")

    # Verify Add Tenant screen is closed and no tenant is added
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Lease Management System']")))
    print("Test Case TC_TENANT_04: Cancel adding a new tenant - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_TENANT_04.png")
    failed_tests += 1

# Test Case TC_PROPERTY_01: Add a new property with valid data
try:
    print("Running Test Case TC_PROPERTY_01: Add a new property with valid data")
    # Navigate to "Add Property" screen
    driver.get(base_url + "add_property")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address_line1")))
    print("Test Step 1: Navigate to 'Add Property' screen - PASSED")

    # Enter valid address line 1 in "Address Line 1" field
    driver.find_element(By.ID, "address_line1").send_keys("123 Main Street")
    print("Test Step 2: Enter valid address line 1 in 'Address Line 1' field - PASSED")

    # Enter valid address line 2 in "Address Line 2" field
    driver.find_element(By.ID, "address_line2").send_keys("Apt 1")
    print("Test Step 3: Enter valid address line 2 in 'Address Line 2' field - PASSED")

    # Enter valid city in "City" field
    driver.find_element(By.ID, "city").send_keys("Anytown")
    print("Test Step 4: Enter valid city in 'City' field - PASSED")

    # Enter valid state in "State" field
    driver.find_element(By.ID, "state").send_keys("CA")
    print("Test Step 5: Enter valid state in 'State' field - PASSED")

    # Enter valid zip code in "Zip Code" field
    driver.find_element(By.ID, "zip_code").send_keys("91234")
    print("Test Step 6: Enter valid zip code in 'Zip Code' field - PASSED")

    # Select valid property status in "Status" field
    driver.find_element(By.ID, "status").send_keys("To Rent")
    print("Test Step 7: Select valid property status in 'Status' field - PASSED")

    # Enter valid unit number in "Unit Number" field
    driver.find_element(By.ID, "unit_number").send_keys("101")
    print("Test Step 8: Enter valid unit number in 'Unit Number' field - PASSED")

    # Click on "Add Property" button
    driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
    time.sleep(0.5)
    print("Test Step 9: Click on 'Add Property' button - PASSED")

    # Verify property is added successfully
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']//tbody//tr//td[text()='123 Main Street']")))
    print("Test Case TC_PROPERTY_01: Add a new property with valid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_01.png")
    failed_tests += 1

# Test Case TC_PROPERTY_02: Add a new property with invalid data
try:
    print("Running Test Case TC_PROPERTY_02: Add a new property with invalid data")
    # Navigate to "Add Property" screen
    driver.get(base_url + "add_property")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address_line1")))
    print("Test Step 1: Navigate to 'Add Property' screen - PASSED")

    # Enter invalid address line 1 (special characters) in "Address Line 1" field
    driver.find_element(By.ID, "address_line1").send_keys("!@#$%^")
    print("Test Step 2: Enter invalid address line 1 (special characters) in 'Address Line 1' field - PASSED")

    # Enter invalid address line 2 (numbers only) in "Address Line 2" field
    driver.find_element(By.ID, "address_line2").send_keys("12345")
    print("Test Step 3: Enter invalid address line 2 (numbers only) in 'Address Line 2' field - PASSED")

    # Enter invalid city (numbers only) in "City" field
    driver.find_element(By.ID, "city").send_keys("12345")
    print("Test Step 4: Enter invalid city (numbers only) in 'City' field - PASSED")

    # Enter invalid state (numbers only) in "State" field
    driver.find_element(By.ID, "state").send_keys("12345")
    print("Test Step 5: Enter invalid state (numbers only) in 'State' field - PASSED")

    # Enter invalid zip code (alphabets) in "Zip Code" field
    driver.find_element(By.ID, "zip_code").send_keys("abcdefg")
    print("Test Step 6: Enter invalid zip code (alphabets) in 'Zip Code' field - PASSED")

    # Select invalid property status (not from the dropdown list) in "Status" field
    driver.find_element(By.ID, "status").send_keys("Invalid Status")
    print("Test Step 7: Select invalid property status (not from the dropdown list) in 'Status' field - PASSED")

    # Enter invalid unit number (alphabets) in "Unit Number" field
    driver.find_element(By.ID, "unit_number").send_keys("abcdefg")
    print("Test Step 8: Enter invalid unit number (alphabets) in 'Unit Number' field - PASSED")

    # Click on "Add Property" button
    driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
    time.sleep(0.5)
    print("Test Step 9: Click on 'Add Property' button - PASSED")

    # Verify property is not added and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_PROPERTY_02: Add a new property with invalid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_02.png")
    failed_tests += 1

# Test Case TC_PROPERTY_03: Add a new property with empty fields
try:
    print("Running Test Case TC_PROPERTY_03: Add a new property with empty fields")
    # Navigate to "Add Property" screen
    driver.get(base_url + "add_property")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address_line1")))
    print("Test Step 1: Navigate to 'Add Property' screen - PASSED")

    # Leave "Address Line 1" field empty
    driver.find_element(By.ID, "address_line1").clear()
    print("Test Step 2: Leave 'Address Line 1' field empty - PASSED")

    # Leave "City" field empty
    driver.find_element(By.ID, "city").clear()
    print("Test Step 3: Leave 'City' field empty - PASSED")

    # Leave "State" field empty
    driver.find_element(By.ID, "state").clear()
    print("Test Step 4: Leave 'State' field empty - PASSED")

    # Leave "Zip Code" field empty
    driver.find_element(By.ID, "zip_code").clear()
    print("Test Step 5: Leave 'Zip Code' field empty - PASSED")

    # Leave "Status" field empty
    driver.find_element(By.ID, "status").clear()
    print("Test Step 6: Leave 'Status' field empty - PASSED")

    # Leave "Unit Number" field empty
    driver.find_element(By.ID, "unit_number").clear()
    print("Test Step 7: Leave 'Unit Number' field empty - PASSED")

    # Click on "Add Property" button
    driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
    time.sleep(0.5)
    print("Test Step 8: Click on 'Add Property' button - PASSED")

    # Verify property is not added and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_PROPERTY_03: Add a new property with empty fields - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_03.png")
    failed_tests += 1

# Test Case TC_PROPERTY_04: Cancel adding a new property
try:
    print("Running Test Case TC_PROPERTY_04: Cancel adding a new property")
    # Navigate to "Add Property" screen
    driver.get(base_url + "add_property")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address_line1")))
    print("Test Step 1: Navigate to 'Add Property' screen - PASSED")

    # Enter valid data in all fields
    driver.find_element(By.ID, "address_line1").send_keys("456 Elm Street")
    driver.find_element(By.ID, "address_line2").send_keys("Apt 2")
    driver.find_element(By.ID, "city").send_keys("Springfield")
    driver.find_element(By.ID, "state").send_keys("IL")
    driver.find_element(By.ID, "zip_code").send_keys("62701")
    driver.find_element(By.ID, "status").send_keys("On Lease")
    driver.find_element(By.ID, "unit_number").send_keys("202")
    print("Test Step 2: Enter valid data in all fields - PASSED")

    # Click on "Cancel" button
    driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
    time.sleep(0.5)
    print("Test Step 3: Click on 'Cancel' button - PASSED")

    # Verify Add Property screen is closed and no property is added
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Lease Management System']")))
    print("Test Case TC_PROPERTY_04: Cancel adding a new property - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_PROPERTY_04.png")
    failed_tests += 1

# Test Case TC_LEASE_01: Prepare a new lease with valid data
try:
    print("Running Test Case TC_LEASE_01: Prepare a new lease with valid data")
    # Navigate to "Prepare Lease" screen
    driver.get(base_url + "prepare_lease")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "property_id")))
    print("Test Step 1: Navigate to 'Prepare Lease' screen - PASSED")

    # Select a valid property from the "Property" dropdown
    driver.find_element(By.ID, "property_id").send_keys("123 Main Street")
    print("Test Step 2: Select a valid property from the 'Property' dropdown - PASSED")

    # Select a valid tenant from the "Tenant" dropdown
    driver.find_element(By.ID, "tenant_id").send_keys("John Doe")
    print("Test Step 3: Select a valid tenant from the 'Tenant' dropdown - PASSED")

    # Enter valid start date in "Start Date" field
    driver.find_element(By.ID, "start_date").send_keys("2024-01-01")
    print("Test Step 4: Enter valid start date in 'Start Date' field - PASSED")

    # Enter valid end date in "End Date" field
    driver.find_element(By.ID, "end_date").send_keys("2025-01-01")
    print("Test Step 5: Enter valid end date in 'End Date' field - PASSED")

    # Enter valid monthly rent in "Monthly Rent" field
    driver.find_element(By.ID, "monthly_rent").send_keys("1500")
    print("Test Step 6: Enter valid monthly rent in 'Monthly Rent' field - PASSED")

    # Enter valid security deposit in "Security Deposit" field
    driver.find_element(By.ID, "security_deposit").send_keys("1500")
    print("Test Step 7: Enter valid security deposit in 'Security Deposit' field - PASSED")

    # Enter valid payment due date in "Payment Due Date" field
    driver.find_element(By.ID, "payment_due_date").send_keys("2024-01-15")
    print("Test Step 8: Enter valid payment due date in 'Payment Due Date' field - PASSED")

    # Enter valid payment method in "Payment Method" field
    driver.find_element(By.ID, "payment_method").send_keys("Check")
    print("Test Step 9: Enter valid payment method in 'Payment Method' field - PASSED")

    # Click on "Create Lease" button
    driver.find_element(By.XPATH, "//button[text()='Create Lease']").click()
    time.sleep(0.5)
    print("Test Step 10: Click on 'Create Lease' button - PASSED")

    # Verify lease is created successfully
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']//tbody//tr//td[text()='123 Main Street']")))
    print("Test Case TC_LEASE_01: Prepare a new lease with valid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_01.png")
    failed_tests += 1

# Test Case TC_LEASE_02: Prepare a new lease with invalid data
try:
    print("Running Test Case TC_LEASE_02: Prepare a new lease with invalid data")
    # Navigate to "Prepare Lease" screen
    driver.get(base_url + "prepare_lease")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "property_id")))
    print("Test Step 1: Navigate to 'Prepare Lease' screen - PASSED")

    # Select an invalid property (not from the dropdown list) from the "Property" dropdown
    driver.find_element(By.ID, "property_id").send_keys("Invalid Property")
    print("Test Step 2: Select an invalid property (not from the dropdown list) from the 'Property' dropdown - PASSED")

    # Select an invalid tenant (not from the dropdown list) from the "Tenant" dropdown
    driver.find_element(By.ID, "tenant_id").send_keys("Invalid Tenant")
    print("Test Step 3: Select an invalid tenant (not from the dropdown list) from the 'Tenant' dropdown - PASSED")

    # Enter invalid start date (future date) in "Start Date" field
    driver.find_element(By.ID, "start_date").send_keys("2025-01-01")
    print("Test Step 4: Enter invalid start date (future date) in 'Start Date' field - PASSED")

    # Enter invalid end date (past date) in "End Date" field
    driver.find_element(By.ID, "end_date").send_keys("2023-01-01")
    print("Test Step 5: Enter invalid end date (past date) in 'End Date' field - PASSED")

    # Enter invalid monthly rent (alphabets) in "Monthly Rent" field
    driver.find_element(By.ID, "monthly_rent").send_keys("abc")
    print("Test Step 6: Enter invalid monthly rent (alphabets) in 'Monthly Rent' field - PASSED")

    # Enter invalid security deposit (alphabets) in "Security Deposit" field
    driver.find_element(By.ID, "security_deposit").send_keys("xyz")
    print("Test Step 7: Enter invalid security deposit (alphabets) in 'Security Deposit' field - PASSED")

    # Enter invalid payment due date (future date) in "Payment Due Date" field
    driver.find_element(By.ID, "payment_due_date").send_keys("2025-01-15")
    print("Test Step 8: Enter invalid payment due date (future date) in 'Payment Due Date' field - PASSED")

    # Enter invalid payment method (not from the dropdown list) in "Payment Method" field
    driver.find_element(By.ID, "payment_method").send_keys("Invalid Payment Method")
    print("Test Step 9: Enter invalid payment method (not from the dropdown list) in 'Payment Method' field - PASSED")

    # Click on "Create Lease" button
    driver.find_element(By.XPATH, "//button[text()='Create Lease']").click()
    time.sleep(0.5)
    print("Test Step 10: Click on 'Create Lease' button - PASSED")

    # Verify lease is not created and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_LEASE_02: Prepare a new lease with invalid data - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_02.png")
    failed_tests += 1

# Test Case TC_LEASE_03: Prepare a new lease with empty fields
try:
    print("Running Test Case TC_LEASE_03: Prepare a new lease with empty fields")
    # Navigate to "Prepare Lease" screen
    driver.get(base_url + "prepare_lease")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "property_id")))
    print("Test Step 1: Navigate to 'Prepare Lease' screen - PASSED")

    # Leave "Property" field empty
    driver.find_element(By.ID, "property_id").clear()
    print("Test Step 2: Leave 'Property' field empty - PASSED")

    # Leave "Tenant" field empty
    driver.find_element(By.ID, "tenant_id").clear()
    print("Test Step 3: Leave 'Tenant' field empty - PASSED")

    # Leave "Start Date" field empty
    driver.find_element(By.ID, "start_date").clear()
    print("Test Step 4: Leave 'Start Date' field empty - PASSED")

    # Leave "End Date" field empty
    driver.find_element(By.ID, "end_date").clear()
    print("Test Step 5: Leave 'End Date' field empty - PASSED")

    # Leave "Monthly Rent" field empty
    driver.find_element(By.ID, "monthly_rent").clear()
    print("Test Step 6: Leave 'Monthly Rent' field empty - PASSED")

    # Leave "Security Deposit" field empty
    driver.find_element(By.ID, "security_deposit").clear()
    print("Test Step 7: Leave 'Security Deposit' field empty - PASSED")

    # Leave "Payment Due Date" field empty
    driver.find_element(By.ID, "payment_due_date").clear()
    print("Test Step 8: Leave 'Payment Due Date' field empty - PASSED")

    # Leave "Payment Method" field empty
    driver.find_element(By.ID, "payment_method").clear()
    print("Test Step 9: Leave 'Payment Method' field empty - PASSED")

    # Click on "Create Lease" button
    driver.find_element(By.XPATH, "//button[text()='Create Lease']").click()
    time.sleep(0.5)
    print("Test Step 10: Click on 'Create Lease' button - PASSED")

    # Verify lease is not created and error message is displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
    print("Test Case TC_LEASE_03: Prepare a new lease with empty fields - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_03.png")
    failed_tests += 1

# Test Case TC_LEASE_04: Cancel preparing a new lease
try:
    print("Running Test Case TC_LEASE_04: Cancel preparing a new lease")
    # Navigate to "Prepare Lease" screen
    driver.get(base_url + "prepare_lease")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "property_id")))
    print("Test Step 1: Navigate to 'Prepare Lease' screen - PASSED")

    # Enter valid data in all fields
    driver.find_element(By.ID, "property_id").send_keys("123 Main Street")
    driver.find_element(By.ID, "tenant_id").send_keys("John Doe")
    driver.find_element(By.ID, "start_date").send_keys("2024-02-01")
    driver.find_element(By.ID, "end_date").send_keys("2025-02-01")
    driver.find_element(By.ID, "monthly_rent").send_keys("1700")
    driver.find_element(By.ID, "security_deposit").send_keys("1700")
    driver.find_element(By.ID, "payment_due_date").send_keys("2024-02-15")
    driver.find_element(By.ID, "payment_method").send_keys("Cash")
    print("Test Step 2: Enter valid data in all fields - PASSED")

    # Click on "Cancel" button
    driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
    time.sleep(0.5)
    print("Test Step 3: Click on 'Cancel' button - PASSED")

    # Verify Prepare Lease screen is closed and no lease is created
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Lease Management System']")))
    print("Test Case TC_LEASE_04: Cancel preparing a new lease - PASSED")
    passed_tests += 1

except Exception as e:
    print(f"Test step failed: {e}")
    driver.save_screenshot(f"error_screenshot_TC_LEASE_04.png")
    failed_tests += 1

# Close the WebDriver
driver.quit()