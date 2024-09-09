
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your actual browser driver path
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Navigate to the Lease Management System landing page
driver.get("https://lease-management-service-729496874389.us-central1.run.app/")
time.sleep(2)

# Test Case ID: TC_TENANT_01
# Test Case Description: Create a new tenant with valid data
def test_create_tenant_valid_data():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_02
# Test Case Description: Create a new tenant with invalid data - empty first name
def test_create_tenant_invalid_data_empty_first_name():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Leave the "First Name" field empty
    # No action needed, field is already empty

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_03
# Test Case Description: Create a new tenant with invalid data - invalid email address
def test_create_tenant_invalid_data_invalid_email():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter an invalid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("invalid_email")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_04
# Test Case Description: Create a new tenant with invalid data - special characters in first name
def test_create_tenant_invalid_data_special_chars_first_name():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a first name with special characters in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John!")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_05
# Test Case Description: Create a new tenant with invalid data - special characters in last name
def test_create_tenant_invalid_data_special_chars_last_name():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a last name with special characters in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe!")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_06
# Test Case Description: Create a new tenant with invalid data - invalid contact number
def test_create_tenant_invalid_data_invalid_contact_number():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter an invalid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("123456789")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_07
# Test Case Description: Cancel tenant creation
def test_cancel_tenant_creation():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Cancel" button
    driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_08
# Test Case Description: Create a new tenant with existing email address
def test_create_tenant_existing_email():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter an existing email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("existing@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_09
# Test Case Description: Create a new tenant with existing contact number
def test_create_tenant_existing_contact_number():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Enter an existing contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")
    time.sleep(2)

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Test Case ID: TC_TENANT_10
# Test Case Description: Create a new tenant with empty contact number
def test_create_tenant_empty_contact_number():
    # Test Step ID: 1
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()
    time.sleep(2)

    # Test Step ID: 2
    # Test Step Description: Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")
    time.sleep(2)

    # Test Step ID: 3
    # Test Step Description: Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    time.sleep(2)

    # Test Step ID: 4
    # Test Step Description: Leave the "Contact Number" field empty
    # No action needed, field is already empty

    # Test Step ID: 5
    # Test Step Description: Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(2)

    # Test Step ID: 6
    # Test Step Description: Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
    time.sleep(2)

# Run all test cases
test_create_tenant_valid_data()
test_create_tenant_invalid_data_empty_first_name()
test_create_tenant_invalid_data_invalid_email()
test_create_tenant_invalid_data_special_chars_first_name()
test_create_tenant_invalid_data_special_chars_last_name()
test_create_tenant_invalid_data_invalid_contact_number()
test_cancel_tenant_creation()
test_create_tenant_existing_email()
test_create_tenant_existing_contact_number()
test_create_tenant_empty_contact_number()

# Close the browser
driver.quit()