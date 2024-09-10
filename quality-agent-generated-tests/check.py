
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize variables
base_url = "https://lease-management-service-729496874389.us-central1.run.app/"
passed_tests = 0
failed_tests = 0

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

# Function to take screenshot on error
def take_screenshot(test_step_description):
    try:
        driver.save_screenshot(f'error_screenshot_{test_step_description}.png')
    except Exception as e:
        print(f"Error taking screenshot: {e}")

# Function to handle test steps
def execute_test_step(test_step_id, test_step_description, expected_result):
    global passed_tests, failed_tests
    try:
        # Execute test step based on description
        if "Click on 'Add Tenant' button" in test_step_description:
            add_tenant_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Add Tenant"))
            )
            add_tenant_button.click()
            time.sleep(0.5)
        elif "Enter valid first name in 'First Name' field" in test_step_description:
            first_name_field = driver.find_element(By.ID, "first_name")
            first_name_field.send_keys("John")
            time.sleep(0.5)
        elif "Enter valid last name in 'Last Name' field" in test_step_description:
            last_name_field = driver.find_element(By.ID, "last_name")
            last_name_field.send_keys("Doe")
            time.sleep(0.5)
        elif "Enter valid contact number in 'Contact Number' field" in test_step_description:
            contact_number_field = driver.find_element(By.ID, "contact_number")
            contact_number_field.send_keys("1234567890")
            time.sleep(0.5)
        elif "Enter valid email address in 'Email' field" in test_step_description:
            email_field = driver.find_element(By.ID, "email")
            email_field.send_keys("john.doe@example.com")
            time.sleep(0.5)
        elif "Click on 'Add Tenant' button" in test_step_description:
            add_tenant_button = driver.find_element(By.XPATH, "//button[text()='Add Tenant']")
            add_tenant_button.click()
            time.sleep(0.5)
        elif "Enter invalid first name (special characters) in 'First Name' field" in test_step_description:
            first_name_field = driver.find_element(By.ID, "first_name")
            first_name_field.send_keys("John!")
            time.sleep(0.5)
        elif "Enter invalid last name (numbers only) in 'Last Name' field" in test_step_description:
            last_name_field = driver.find_element(By.ID, "last_name")
            last_name_field.send_keys("1234")
            time.sleep(0.5)
        elif "Enter invalid contact number (alphabets) in 'Contact Number' field" in test_step_description:
            contact_number_field = driver.find_element(By.ID, "contact_number")
            contact_number_field.send_keys("abcd")
            time.sleep(0.5)
        elif "Enter invalid email address (without @ symbol) in 'Email' field" in test_step_description:
            email_field = driver.find_element(By.ID, "email")
            email_field.send_keys("john.doeexample.com")
            time.sleep(0.5)
        elif "Leave 'First Name' field empty" in test_step_description:
            first_name_field = driver.find_element(By.ID, "first_name")
            first_name_field.clear()
            time.sleep(0.5)
        elif "Leave 'Last Name' field empty" in test_step_description:
            last_name_field = driver.find_element(By.ID, "last_name")
            last_name_field.clear()
            time.sleep(0.5)
        elif "Leave 'Contact Number' field empty" in test_step_description:
            contact_number_field = driver.find_element(By.ID, "contact_number")
            contact_number_field.clear()
            time.sleep(0.5)
        elif "Leave 'Email' field empty" in test_step_description:
            email_field = driver.find_element(By.ID, "email")
            email_field.clear()
            time.sleep(0.5)
        elif "Click on 'Cancel' button" in test_step_description:
            cancel_button = driver.find_element(By.XPATH, "//button[text()='Cancel']")
            cancel_button.click()
            time.sleep(0.5)
        elif "Click on 'Add Property' button" in test_step_description:
            add_property_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Add Property"))
            )
            add_property_button.click()
            time.sleep(0.5)
        elif "Enter valid address line 1 in 'Address Line 1' field" in test_step_description:
            address_line1_field = driver.find_element(By.ID, "address_line1")
            address_line1_field.send_keys("123 Main Street")
            time.sleep(0.5)
        elif "Enter valid address line 2 in 'Address Line 2' field" in test_step_description:
            address_line2_field = driver.find_element(By.ID, "address_line2")
            address_line2_field.send_keys("Apt 1")
            time.sleep(0.5)
        elif "Enter valid city in 'City' field" in test_step_description:
            city_field = driver.find_element(By.ID, "city")
            city_field.send_keys("Anytown")
            time.sleep(0.5)
        elif "Enter valid state in 'State' field" in test_step_description:
            state_field = driver.find_element(By.ID, "state")
            state_field.send_keys("CA")
            time.sleep(0.5)
        elif "Enter valid zip code in 'Zip Code' field" in test_step_description:
            zip_code_field = driver.find_element(By.ID, "zip_code")
            zip_code_field.send_keys("12345")
            time.sleep(0.5)
        elif "Enter valid status in 'Status' field" in test_step_description:
            status_dropdown = driver.find_element(By.ID, "status")
            status_dropdown.send_keys("To Rent")
            time.sleep(0.5)
        elif "Enter valid unit number in 'Unit Number' field" in test_step_description:
            unit_number_field = driver.find_element(By.ID, "unit_number")
            unit_number_field.send_keys("1")
            time.sleep(0.5)
        elif "Enter invalid address line 1 (special characters) in 'Address Line 1' field" in test_step_description:
            address_line1_field = driver.find_element(By.ID, "address_line1")
            address_line1_field.send_keys("123 Main Street!")
            time.sleep(0.5)
        elif "Enter invalid address line 2 (numbers only) in 'Address Line 2' field" in test_step_description:
            address_line2_field = driver.find_element(By.ID, "address_line2")
            address_line2_field.send_keys("1234")
            time.sleep(0.5)
        elif "Enter invalid city (numbers only) in 'City' field" in test_step_description:
            city_field = driver.find_element(By.ID, "city")
            city_field.send_keys("1234")
            time.sleep(0.5)
        elif "Enter invalid state (numbers only) in 'State' field" in test_step_description:
            state_field = driver.find_element(By.ID, "state")
            state_field.send_keys("1234")
            time.sleep(0.5)
        elif "Enter invalid zip code (alphabets) in 'Zip Code' field" in test_step_description:
            zip_code_field = driver.find_element(By.ID, "zip_code")
            zip_code_field.send_keys("abcd")
            time.sleep(0.5)
        elif "Enter invalid status (special characters) in 'Status' field" in test_step_description:
            status_dropdown = driver.find_element(By.ID, "status")
            status_dropdown.send_keys("To Rent!")
            time.sleep(0.5)
        elif "Enter invalid unit number (alphabets) in 'Unit Number' field" in test_step_description:
            unit_number_field = driver.find_element(By.ID, "unit_number")
            unit_number_field.send_keys("abc")
            time.sleep(0.5)
        elif "Leave 'Address Line 1' field empty" in test_step_description:
            address_line1_field = driver.find_element(By.ID, "address_line1")
            address_line1_field.clear()
            time.sleep(0.5)
        elif "Leave 'City' field empty" in test_step_description:
            city_field = driver.find_element(By.ID, "city")
            city_field.clear()
            time.sleep(0.5)
        elif "Leave 'State' field empty" in test_step_description:
            state_field = driver.find_element(By.ID, "state")
            state_field.clear()
            time.sleep(0.5)
        elif "Leave 'Zip Code' field empty" in test_step_description:
            zip_code_field = driver.find_element(By.ID, "zip_code")
            zip_code_field.clear()
            time.sleep(0.5)
        elif "Leave 'Status' field empty" in test_step_description:
            status_dropdown = driver.find_element(By.ID, "status")
            status_dropdown.clear()
            time.sleep(0.5)
        elif "Leave 'Unit Number' field empty" in test_step_description:
            unit_number_field = driver.find_element(By.ID, "unit_number")
            unit_number_field.clear()
            time.sleep(0.5)
        elif "Click on 'Prepare Lease' button" in test_step_description:
            prepare_lease_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Prepare Lease"))
            )
            prepare_lease_button.click()
            time.sleep(0.5)
        elif "Select a valid property from the 'Property' dropdown" in test_step_description:
            property_dropdown = driver.find_element(By.ID, "property_id")
            property_dropdown.click()
            time.sleep(0.5)
            property_dropdown.send_keys("123 Main Street")
            time.sleep(0.5)
        elif "Select a valid tenant from the 'Tenant' dropdown" in test_step_description:
            tenant_dropdown = driver.find_element(By.ID, "tenant_id")
            tenant_dropdown.click()
            time.sleep(0.5)
            tenant_dropdown.send_keys("John Doe")
            time.sleep(0.5)
        elif "Enter valid start date in 'Start Date' field" in test_step_description:
            start_date_field = driver.find_element(By.ID, "start_date")
            start_date_field.send_keys("2024-01-01")
            time.sleep(0.5)
        elif "Enter valid end date in 'End Date' field" in test_step_description:
            end_date_field = driver.find_element(By.ID, "end_date")
            end_date_field.send_keys("2025-01-01")
            time.sleep(0.5)
        elif "Enter valid monthly rent in 'Monthly Rent' field" in test_step_description:
            monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
            monthly_rent_field.send_keys("1000")
            time.sleep(0.5)
        elif "Enter valid security deposit in 'Security Deposit' field" in test_step_description:
            security_deposit_field = driver.find_element(By.ID, "security_deposit")
            security_deposit_field.send_keys("1000")
            time.sleep(0.5)
        elif "Enter valid payment due date in 'Payment Due Date' field" in test_step_description:
            payment_due_date_field = driver.find_element(By.ID, "payment_due_date")
            payment_due_date_field.send_keys("2024-02-01")
            time.sleep(0.5)
        elif "Enter valid payment method in 'Payment Method' field" in test_step_description:
            payment_method_field = driver.find_element(By.ID, "payment_method")
            payment_method_field.send_keys("Credit Card")
            time.sleep(0.5)
        elif "Select an invalid property (non-existent) from the 'Property' dropdown" in test_step_description:
            property_dropdown = driver.find_element(By.ID, "property_id")
            property_dropdown.click()
            time.sleep(0.5)
            property_dropdown.send_keys("Invalid Property")
            time.sleep(0.5)
        elif "Select an invalid tenant (non-existent) from the 'Tenant' dropdown" in test_step_description:
            tenant_dropdown = driver.find_element(By.ID, "tenant_id")
            tenant_dropdown.click()
            time.sleep(0.5)
            tenant_dropdown.send_keys("Invalid Tenant")
            time.sleep(0.5)
        elif "Enter invalid start date (future date) in 'Start Date' field" in test_step_description:
            start_date_field = driver.find_element(By.ID, "start_date")
            start_date_field.send_keys("2025-01-01")
            time.sleep(0.5)
        elif "Enter invalid end date (past date) in 'End Date' field" in test_step_description:
            end_date_field = driver.find_element(By.ID, "end_date")
            end_date_field.send_keys("2023-01-01")
            time.sleep(0.5)
        elif "Enter invalid monthly rent (alphabets) in 'Monthly Rent' field" in test_step_description:
            monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
            monthly_rent_field.send_keys("abcd")
            time.sleep(0.5)
        elif "Enter invalid security deposit (alphabets) in 'Security Deposit' field" in test_step_description:
            security_deposit_field = driver.find_element(By.ID, "security_deposit")
            security_deposit_field.send_keys("abcd")
            time.sleep(0.5)
        elif "Enter invalid payment due date (future date) in 'Payment Due Date' field" in test_step_description:
            payment_due_date_field = driver.find_element(By.ID, "payment_due_date")
            payment_due_date_field.send_keys("2025-01-01")
            time.sleep(0.5)
        elif "Enter invalid payment method (special characters) in 'Payment Method' field" in test_step_description:
            payment_method_field = driver.find_element(By.ID, "payment_method")
            payment_method_field.send_keys("!@#$%^")
            time.sleep(0.5)
        elif "Leave 'Property' field empty" in test_step_description:
            property_dropdown = driver.find_element(By.ID, "property_id")
            property_dropdown.clear()
            time.sleep(0.5)
        elif "Leave 'Tenant' field empty" in test_step_description:
            tenant_dropdown = driver.find_element(By.ID, "tenant_id")
            tenant_dropdown.clear()
            time.sleep(0.5)
        elif "Leave 'Start Date' field empty" in test_step_description:
            start_date_field = driver.find_element(By.ID, "start_date")
            start_date_field.clear()
            time.sleep(0.5)
        elif "Leave 'End Date' field empty" in test_step_description:
            end_date_field = driver.find_element(By.ID, "end_date")
            end_date_field.clear()
            time.sleep(0.5)
        elif "Leave 'Monthly Rent' field empty" in test_step_description:
            monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
            monthly_rent_field.clear()
            time.sleep(0.5)
        elif "Leave 'Security Deposit' field empty" in test_step_description:
            security_deposit_field = driver.find_element(By.ID, "security_deposit")
            security_deposit_field.clear()
            time.sleep(0.5)
        elif "Leave 'Payment Due Date' field empty" in test_step_description:
            payment_due_date_field = driver.find_element(By.ID, "payment_due_date")
            payment_due_date_field.clear()
            time.sleep(0.5)
        elif "Leave 'Payment Method' field empty" in test_step_description:
            payment_method_field = driver.find_element(By.ID, "payment_method")
            payment_method_field.clear()
            time.sleep(0.5)
        elif "Navigate to the Tenants table" in test_step_description:
            driver.get(base_url)
            time.sleep(0.5)
        elif "Click on 'Actions' button for an existing tenant" in test_step_description:
            actions_button = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[3]//a[1]")
            actions_button.click()
            time.sleep(0.5)
        elif "Edit the 'First Name' field" in test_step_description:
            first_name_field = driver.find_element(By.ID, "first_name")
            first_name_field.clear()
            first_name_field.send_keys("Jane")
            time.sleep(0.5)
        elif "Click on 'Save' button" in test_step_description:
            save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
            save_button.click()
            time.sleep(0.5)
        elif "Click on 'Delete' button" in test_step_description:
            delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
            delete_button.click()
            time.sleep(0.5)
        elif "Enter a valid first name in the search field" in test_step_description:
            search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search_field.send_keys("John")
            time.sleep(0.5)
        elif "Clear the search field" in test_step_description:
            search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search_field.clear()
            time.sleep(0.5)
        elif "Click on the 'First Name' of a tenant" in test_step_description:
            tenant_name = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[1]")
            tenant_name.click()
            time.sleep(0.5)
        elif "Click on 'Back' button" in test_step_description:
            back_button = driver.find_element(By.XPATH, "//button[text()='Back']")
            back_button.click()
            time.sleep(0.5)
        elif "Navigate to the Properties table" in test_step_description:
            driver.get(base_url)
            time.sleep(0.5)
        elif "Click on 'Actions' button for an existing property" in test_step_description:
            actions_button = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[6]//a[1]")
            actions_button.click()
            time.sleep(0.5)
        elif "Edit the 'Address Line 1' field" in test_step_description:
            address_line1_field = driver.find_element(By.ID, "address_line1")
            address_line1_field.clear()
            address_line1_field.send_keys("124 Main Street")
            time.sleep(0.5)
        elif "Enter a valid city in the search field" in test_step_description:
            search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search_field.send_keys("Anytown")
            time.sleep(0.5)
        elif "Click on the 'Address' of a property" in test_step_description:
            property_address = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[1]")
            property_address.click()
            time.sleep(0.5)
        elif "Navigate to the Leases table" in test_step_description:
            driver.get(base_url)
            time.sleep(0.5)
        elif "Click on 'Actions' button for an existing lease" in test_step_description:
            actions_button = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[6]//a[1]")
            actions_button.click()
            time.sleep(0.5)
        elif "Edit the 'Monthly Rent' field" in test_step_description:
            monthly_rent_field = driver.find_element(By.ID, "monthly_rent")
            monthly_rent_field.clear()
            monthly_rent_field.send_keys("1200")
            time.sleep(0.5)
        elif "Enter a valid tenant name in the search field" in test_step_description:
            search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search_field.send_keys("John Doe")
            time.sleep(0.5)
        elif "Click on the 'Tenant' of a lease" in test_step_description:
            lease_tenant = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[2]")
            lease_tenant.click()
            time.sleep(0.5)
        else:
            print(f"Test step not implemented: {test_step_description}")
            return

        # Verify expected result
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

# Read test cases from Excel file (replace with your actual file path)
# ... (Code to read test cases from Excel file)

# Execute test cases
for test_case in test_cases:
    print(f"Executing test case: {test_case['Test Case Description']}")
    for test_step in test_case['Test Steps']:
        execute_test_step(test_step['Test Step ID'], test_step['Test Step Description'], test_step['Expected Result'])

# Generate test report
print(f"\nTest Report:")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

# Close WebDriver
driver.quit()