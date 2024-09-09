
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

# Function to take a screenshot
def take_screenshot(test_step_description):
    try:
        driver.save_screenshot(f'error_screenshot_{test_step_description}.png')
    except Exception as e:
        print(f"Error taking screenshot: {e}")

# Function to handle test steps
def execute_test_step(test_step_id, test_step_description, expected_result, *args):
    global passed_tests, failed_tests
    try:
        # Execute the test step based on the provided arguments
        if len(args) == 1:
            # Click operation
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, args[0]))
            )
            element.click()
            time.sleep(0.5)
        elif len(args) == 2:
            # Input operation
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, args[0]))
            )
            element.send_keys(args[1])
            time.sleep(0.5)
        elif len(args) == 3:
            # Select operation
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, args[0]))
            )
            element.select_by_visible_text(args[1])
            time.sleep(0.5)
        else:
            print(f"Test step {test_step_id} not implemented.")
            return

        # Verify the expected result
        if expected_result in driver.page_source:
            print(f"Test step {test_step_id} passed: {test_step_description}")
            passed_tests += 1
        else:
            print(f"Test step {test_step_id} failed: {test_step_description}")
            failed_tests += 1
            take_screenshot(test_step_description)
    except Exception as e:
        print(f"Test step {test_step_id} failed: {test_step_description}")
        failed_tests += 1
        take_screenshot(test_step_description)
        print(f"Error: {e}")

# Test Case TC_TENANT_01
driver.get(base_url)
execute_test_step(1, "Click on 'Add Tenant' button", "Add New Tenant", "Add Tenant")
execute_test_step(2, "Enter valid first name in 'First Name' field", "First name is entered successfully", "first_name", "John")
execute_test_step(3, "Enter valid last name in 'Last Name' field", "Last name is entered successfully", "last_name", "Doe")
execute_test_step(4, "Enter valid contact number in 'Contact Number' field", "Contact number is entered successfully", "contact_number", "1234567890")
execute_test_step(5, "Enter valid email address in 'Email' field", "Email address is entered successfully", "email", "john.doe@example.com")
execute_test_step(6, "Click on 'Add Tenant' button", "Tenant is created successfully and displayed in the Tenants table", "Add Tenant")

# Test Case TC_TENANT_02
driver.get(base_url)
execute_test_step(1, "Click on 'Add Tenant' button", "Add New Tenant", "Add Tenant")
execute_test_step(2, "Enter invalid first name (special characters) in 'First Name' field", "Error message is displayed for invalid first name", "first_name", "John*")
execute_test_step(3, "Enter invalid last name (numbers only) in 'Last Name' field", "Error message is displayed for invalid last name", "last_name", "12345")
execute_test_step(4, "Enter invalid contact number (alphabets) in 'Contact Number' field", "Error message is displayed for invalid contact number", "contact_number", "abc123")
execute_test_step(5, "Enter invalid email address (without @ symbol) in 'Email' field", "Error message is displayed for invalid email address", "email", "john.doeexample.com")
execute_test_step(6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Add Tenant")

# Test Case TC_TENANT_03
driver.get(base_url)
execute_test_step(1, "Click on 'Add Tenant' button", "Add New Tenant", "Add Tenant")
execute_test_step(2, "Leave 'First Name' field empty", "Error message is displayed for empty first name", "first_name", "")
execute_test_step(3, "Leave 'Last Name' field empty", "Error message is displayed for empty last name", "last_name", "")
execute_test_step(4, "Leave 'Contact Number' field empty", "Contact number is accepted as optional", "contact_number", "")
execute_test_step(5, "Leave 'Email' field empty", "Error message is displayed for empty email address", "email", "")
execute_test_step(6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Add Tenant")

# Test Case TC_TENANT_04
driver.get(base_url)
execute_test_step(1, "Click on 'Add Tenant' button", "Add New Tenant", "Add Tenant")
execute_test_step(2, "Enter valid data in all fields", "Data is entered successfully", "first_name", "Jane", "last_name", "Doe", "contact_number", "9876543210", "email", "jane.doe@example.com")
execute_test_step(3, "Click on 'Cancel' button", "Add New Tenant screen is closed and user is redirected to the main screen", "Cancel")

# Test Case TC_TENANT_05
driver.get(base_url)
execute_test_step(1, "Navigate to the Tenants table", "Tenants table is displayed", "Tenants")
execute_test_step(2, "Click on 'Actions' button for an existing tenant", "Edit Tenant screen is displayed", "Actions")
execute_test_step(3, "Edit the 'First Name' field", "First name is updated successfully", "first_name", "Jane")
execute_test_step(4, "Click on 'Save' button", "Tenant details are updated successfully and displayed in the Tenants table", "Save")

# Test Case TC_TENANT_06
driver.get(base_url)
execute_test_step(1, "Navigate to the Tenants table", "Tenants table is displayed", "Tenants")
execute_test_step(2, "Click on 'Actions' button for an existing tenant", "Delete confirmation dialog is displayed", "Actions")
execute_test_step(3, "Click on 'Delete' button", "Tenant is deleted successfully and removed from the Tenants table", "Delete")

# Test Case TC_TENANT_07
driver.get(base_url)
execute_test_step(1, "Navigate to the Tenants table", "Tenants table is displayed", "Tenants")
execute_test_step(2, "Enter a valid first name in the search field", "Tenants matching the entered first name are displayed", "search_tenant", "John")
execute_test_step(3, "Clear the search field", "All tenants are displayed again", "search_tenant", "")

# Test Case TC_TENANT_08
driver.get(base_url)
execute_test_step(1, "Navigate to the Tenants table", "Tenants table is displayed", "Tenants")
execute_test_step(2, "Click on the 'First Name' of a tenant", "Tenant details are displayed in a separate screen", "First Name")
execute_test_step(3, "Click on 'Back' button", "User is redirected to the Tenants table", "Back")

# Test Case TC_PROPERTY_01
driver.get(base_url)
execute_test_step(1, "Click on 'Add Property' button", "Add New Property screen is displayed", "Add Property")
execute_test_step(2, "Enter valid address line 1 in 'Address Line 1' field", "Address line 1 is entered successfully", "address_line1", "123 Main St")
execute_test_step(3, "Enter valid address line 2 in 'Address Line 2' field", "Address line 2 is entered successfully", "address_line2", "Apt 1")
execute_test_step(4, "Enter valid city in 'City' field", "City is entered successfully", "city", "Anytown")
execute_test_step(5, "Enter valid state in 'State' field", "State is entered successfully", "state", "CA")
execute_test_step(6, "Enter valid zip code in 'Zip Code' field", "Zip code is entered successfully", "zip_code", "91234")
execute_test_step(7, "Enter valid status in 'Status' field", "Status is entered successfully", "status", "To Rent")
execute_test_step(8, "Enter valid unit number in 'Unit Number' field", "Unit number is entered successfully", "unit_number", "1")
execute_test_step(9, "Click on 'Add Property' button", "Property is created successfully and displayed in the Properties table", "Add Property")

# Test Case TC_PROPERTY_02
driver.get(base_url)
execute_test_step(1, "Click on 'Add Property' button", "Add New Property screen is displayed", "Add Property")
execute_test_step(2, "Enter invalid address line 1 (special characters) in 'Address Line 1' field", "Error message is displayed for invalid address line 1", "address_line1", "123 Main* St")
execute_test_step(3, "Enter invalid address line 2 (numbers only) in 'Address Line 2' field", "Error message is displayed for invalid address line 2", "address_line2", "12345")
execute_test_step(4, "Enter invalid city (numbers only) in 'City' field", "Error message is displayed for invalid city", "city", "12345")
execute_test_step(5, "Enter invalid state (numbers only) in 'State' field", "Error message is displayed for invalid state", "state", "12345")
execute_test_step(6, "Enter invalid zip code (alphabets) in 'Zip Code' field", "Error message is displayed for invalid zip code", "zip_code", "abc123")
execute_test_step(7, "Enter invalid status (special characters) in 'Status' field", "Error message is displayed for invalid status", "status", "To Rent*")
execute_test_step(8, "Enter invalid unit number (alphabets) in 'Unit Number' field", "Error message is displayed for invalid unit number", "unit_number", "abc")
execute_test_step(9, "Click on 'Add Property' button", "Property is not created and error message is displayed", "Add Property")

# Test Case TC_PROPERTY_03
driver.get(base_url)
execute_test_step(1, "Click on 'Add Property' button", "Add New Property screen is displayed", "Add Property")
execute_test_step(2, "Leave 'Address Line 1' field empty", "Error message is displayed for empty address line 1", "address_line1", "")
execute_test_step(3, "Leave 'City' field empty", "Error message is displayed for empty city", "city", "")
execute_test_step(4, "Leave 'State' field empty", "Error message is displayed for empty state", "state", "")
execute_test_step(5, "Leave 'Zip Code' field empty", "Error message is displayed for empty zip code", "zip_code", "")
execute_test_step(6, "Leave 'Status' field empty", "Status is accepted as optional", "status", "")
execute_test_step(7, "Leave 'Unit Number' field empty", "Unit number is accepted as optional", "unit_number", "")
execute_test_step(8, "Click on 'Add Property' button", "Property is not created and error message is displayed", "Add Property")

# Test Case TC_PROPERTY_04
driver.get(base_url)
execute_test_step(1, "Click on 'Add Property' button", "Add New Property screen is displayed", "Add Property")
execute_test_step(2, "Enter valid data in all fields", "Data is entered successfully", "address_line1", "456 Elm St", "address_line2", "Apt 2", "city", "Springfield", "state", "IL", "zip_code", "62701", "status", "To Rent", "unit_number", "2")
execute_test_step(3, "Click on 'Cancel' button", "Add New Property screen is closed and user is redirected to the main screen", "Cancel")

# Test Case TC_PROPERTY_05
driver.get(base_url)
execute_test_step(1, "Navigate to the Properties table", "Properties table is displayed", "Properties")
execute_test_step(2, "Click on 'Actions' button for an existing property", "Edit Property screen is displayed", "Actions")
execute_test_step(3, "Edit the 'Address Line 1' field", "Address line 1 is updated successfully", "address_line1", "789 Oak St")
execute_test_step(4, "Click on 'Save' button", "Property details are updated successfully and displayed in the Properties table", "Save")

# Test Case TC_PROPERTY_06
driver.get(base_url)
execute_test_step(1, "Navigate to the Properties table", "Properties table is displayed", "Properties")
execute_test_step(2, "Click on 'Actions' button for an existing property", "Delete confirmation dialog is displayed", "Actions")
execute_test_step(3, "Click on 'Delete' button", "Property is deleted successfully and removed from the Properties table", "Delete")

# Test Case TC_PROPERTY_07
driver.get(base_url)
execute_test_step(1, "Navigate to the Properties table", "Properties table is displayed", "Properties")
execute_test_step(2, "Enter a valid city in the search field", "Properties matching the entered city are displayed", "search_property", "Anytown")
execute_test_step(3, "Clear the search field", "All properties are displayed again", "search_property", "")

# Test Case TC_PROPERTY_08
driver.get(base_url)
execute_test_step(1, "Navigate to the Properties table", "Properties table is displayed", "Properties")
execute_test_step(2, "Click on the 'Address' of a property", "Property details are displayed in a separate screen", "Address")
execute_test_step(3, "Click on 'Back' button", "User is redirected to the Properties table", "Back")

# Test Case TC_LEASE_01
driver.get(base_url)
execute_test_step(1, "Click on 'Prepare Lease' button", "Prepare New Lease screen is displayed", "Prepare Lease")
execute_test_step(2, "Select a valid property from the 'Property' dropdown", "Property is selected successfully", "property_id", "123 Main St")
execute_test_step(3, "Select a valid tenant from the 'Tenant' dropdown", "Tenant is selected successfully", "tenant_id", "John Doe")
execute_test_step(4, "Enter valid start date in 'Start Date' field", "Start date is entered successfully", "start_date", "2024-01-01")
execute_test_step(5, "Enter valid end date in 'End Date' field", "End date is entered successfully", "end_date", "2025-01-01")
execute_test_step(6, "Enter valid monthly rent in 'Monthly Rent' field", "Monthly rent is entered successfully", "monthly_rent", "1500")
execute_test_step(7, "Enter valid security deposit in 'Security Deposit' field", "Security deposit is entered successfully", "security_deposit", "1500")
execute_test_step(8, "Enter valid payment due date in 'Payment Due Date' field", "Payment due date is entered successfully", "payment_due_date", "2024-01-15")
execute_test_step(9, "Enter valid payment method in 'Payment Method' field", "Payment method is entered successfully", "payment_method", "Check")
execute_test_step(10, "Click on 'Create Lease' button", "Lease is created successfully and displayed in the Leases table", "Create Lease")

# Test Case TC_LEASE_02
driver.get(base_url)
execute_test_step(1, "Click on 'Prepare Lease' button", "Prepare New Lease screen is displayed", "Prepare Lease")
execute_test_step(2, "Select an invalid property (non-existent) from the 'Property' dropdown", "Error message is displayed for invalid property selection", "property_id", "Invalid Property")
execute_test_step(3, "Select an invalid tenant (non-existent) from the 'Tenant' dropdown", "Error message is displayed for invalid tenant selection", "tenant_id", "Invalid Tenant")
execute_test_step(4, "Enter invalid start date (future date) in 'Start Date' field", "Error message is displayed for invalid start date", "start_date", "2025-01-01")
execute_test_step(5, "Enter invalid end date (past date) in 'End Date' field", "Error message is displayed for invalid end date", "end_date", "2023-01-01")
execute_test_step(6, "Enter invalid monthly rent (alphabets) in 'Monthly Rent' field", "Error message is displayed for invalid monthly rent", "monthly_rent", "abc")
execute_test_step(7, "Enter invalid security deposit (alphabets) in 'Security Deposit' field", "Error message is displayed for invalid security deposit", "security_deposit", "abc")
execute_test_step(8, "Enter invalid payment due date (future date) in 'Payment Due Date' field", "Error message is displayed for invalid payment due date", "payment_due_date", "2025-01-01")
execute_test_step(9, "Enter invalid payment method (special characters) in 'Payment Method' field", "Error message is displayed for invalid payment method", "payment_method", "Invalid Payment Method")
execute_test_step(10, "Click on 'Create Lease' button", "Lease is not created and error message is displayed", "Create Lease")

# Test Case TC_LEASE_03
driver.get(base_url)
execute_test_step(1, "Click on 'Prepare Lease' button", "Prepare New Lease screen is displayed", "Prepare Lease")
execute_test_step(2, "Leave 'Property' field empty", "Error message is displayed for empty property selection", "property_id", "")
execute_test_step(3, "Leave 'Tenant' field empty", "Error message is displayed for empty tenant selection", "tenant_id", "")
execute_test_step(4, "Leave 'Start Date' field empty", "Error message is displayed for empty start date", "start_date", "")
execute_test_step(5, "Leave 'End Date' field empty", "Error message is displayed for empty end date", "end_date", "")
execute_test_step(6, "Leave 'Monthly Rent' field empty", "Error message is displayed for empty monthly rent", "monthly_rent", "")
execute_test_step(7, "Leave 'Security Deposit' field empty", "Error message is displayed for empty security deposit", "security_deposit", "")
execute_test_step(8, "Leave 'Payment Due Date' field empty", "Error message is displayed for empty payment due date", "payment_due_date", "")
execute_test_step(9, "Leave 'Payment Method' field empty", "Error message is displayed for empty payment method", "payment_method", "")
execute_test_step(10, "Click on 'Create Lease' button", "Lease is not created and error message is displayed", "Create Lease")

# Test Case TC_LEASE_04
driver.get(base_url)
execute_test_step(1, "Click on 'Prepare Lease' button", "Prepare New Lease screen is displayed", "Prepare Lease")
execute_test_step(2, "Enter valid data in all fields", "Data is entered successfully", "property_id", "123 Main St", "tenant_id", "John Doe", "start_date", "2024-01-01", "end_date", "2025-01-01", "monthly_rent", "1500", "security_deposit", "1500", "payment_due_date", "2024-01-15", "payment_method", "Check")
execute_test_step(3, "Click on 'Cancel' button", "Prepare New Lease screen is closed and user is redirected to the main screen", "Cancel")

# Test Case TC_LEASE_05
driver.get(base_url)
execute_test_step(1, "Navigate to the Leases table", "Leases table is displayed", "Leases")
execute_test_step(2, "Click on 'Actions' button for an existing lease", "Edit Lease screen is displayed", "Actions")
execute_test_step(3, "Edit the 'Monthly Rent' field", "Monthly rent is updated successfully", "monthly_rent", "1750")
execute_test_step(4, "Click on 'Save' button", "Lease details are updated successfully and displayed in the Leases table", "Save")

# Test Case TC_LEASE_06
driver.get(base_url)
execute_test_step(1, "Navigate to the Leases table", "Leases table is displayed", "Leases")
execute_test_step(2, "Click on 'Actions' button for an existing lease", "Delete confirmation dialog is displayed", "Actions")
execute_test_step(3, "Click on 'Delete' button", "Lease is deleted successfully and removed from the Leases table", "Delete")

# Test Case TC_LEASE_07
driver.get(base_url)
execute_test_step(1, "Navigate to the Leases table", "Leases table is displayed", "Leases")
execute_test_step(2, "Enter a valid tenant name in the search field", "Leases matching the entered tenant name are displayed", "search_lease", "John Doe")
execute_test_step(3, "Clear the search field", "All leases are displayed again", "search_lease", "")

# Test Case TC_LEASE_08
driver.get(base_url)
execute_test_step(1, "Navigate to the Leases table", "Leases table is displayed", "Leases")
execute_test_step(2, "Click on the 'Tenant' of a lease", "Lease details are displayed in a separate screen", "Tenant")
execute_test_step(3, "Click on 'Back' button", "User is redirected to the Leases table", "Back")

# Generate test report
print(f"\nTest Report:")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

# Quit the WebDriver
driver.quit()