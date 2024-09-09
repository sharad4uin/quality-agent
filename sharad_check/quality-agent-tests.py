
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the Lease Management System landing page
driver.get("https://lease-management-service-729496874389.us-central1.run.app/")

# Test Case TC_TENANT_01: Create a new tenant with valid data
def test_create_tenant_valid_data():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is created successfully and displayed in the Tenants table
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_02: Create a new tenant with invalid data - empty first name
def test_create_tenant_invalid_data_empty_first_name():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Leave the "First Name" field empty

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_03: Create a new tenant with invalid data - invalid email address
def test_create_tenant_invalid_data_invalid_email():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter an invalid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("invalid_email")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_04: Create a new tenant with invalid data - special characters in first name
def test_create_tenant_invalid_data_special_chars_first_name():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a first name with special characters in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John!")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_05: Create a new tenant with invalid data - special characters in last name
def test_create_tenant_invalid_data_special_chars_last_name():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a last name with special characters in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe!")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_06: Create a new tenant with invalid data - invalid contact number
def test_create_tenant_invalid_data_invalid_contact_number():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter an invalid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("123456789")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_07: Cancel tenant creation
def test_cancel_tenant_creation():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Cancel" button
    driver.find_element(By.XPATH, "//button[text()='Cancel']").click()

    # Verify that the Add New Tenant screen is closed and no tenant is created
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_08: Create a new tenant with existing email address
def test_create_tenant_existing_email():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter an existing email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("existing@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_09: Create a new tenant with existing contact number
def test_create_tenant_existing_contact_number():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter an existing contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is not created and an error message is displayed
    # (Add assertions here to verify the expected result)

# Test Case TC_TENANT_10: Create a new tenant with empty contact number
def test_create_tenant_empty_contact_number():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Leave the "Contact Number" field empty

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Verify that the tenant is created successfully and displayed in the Tenants table
    # (Add assertions here to verify the expected result)

# Run the test cases
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