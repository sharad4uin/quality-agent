
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

# Function to log test results
def log_test_result(test_case_id, test_step_id, test_step_description, expected_result, actual_result, status):
    global passed_tests, failed_tests
    if status == "Pass":
        passed_tests += 1
    else:
        failed_tests += 1
    print(f"Test Case ID: {test_case_id}")
    print(f"Test Step ID: {test_step_id}")
    print(f"Test Step Description: {test_step_description}")
    print(f"Expected Result: {expected_result}")
    print(f"Actual Result: {actual_result}")
    print(f"Status: {status}")
    print("-" * 30)

# Test Case TC_TENANT_01: Create a new tenant with valid data
try:
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Test Step 1: Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Test Step 2: Enter valid first name in "First Name" field
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("John")
    time.sleep(0.5)

    # Test Step 3: Enter valid last name in "Last Name" field
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("Doe")
    time.sleep(0.5)

    # Test Step 4: Enter valid contact number in "Contact Number" field
    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.send_keys("1234567890")
    time.sleep(0.5)

    # Test Step 5: Enter valid email address in "Email" field
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john.doe@example.com")
    time.sleep(0.5)

    # Test Step 6: Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is created successfully
    try:
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        tenant_found = False
        for row in tenant_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "John" and cells[1].text == "Doe":
                tenant_found = True
                break
        if tenant_found:
            log_test_result("TC_TENANT_01", 6, "Click on 'Add Tenant' button", "Tenant is created successfully and displayed in the Tenants table", "Tenant is created successfully and displayed in the Tenants table", "Pass")
        else:
            log_test_result("TC_TENANT_01", 6, "Click on 'Add Tenant' button", "Tenant is created successfully and displayed in the Tenants table", "Tenant is not created successfully", "Fail")
            take_screenshot("TC_TENANT_01_Step_6")
    except Exception as e:
        log_test_result("TC_TENANT_01", 6, "Click on 'Add Tenant' button", "Tenant is created successfully and displayed in the Tenants table", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_01_Step_6")

except Exception as e:
    log_test_result("TC_TENANT_01", 1, "Click on 'Add Tenant' button", "Add New Tenant screen is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_01_Step_1")

# Test Case TC_TENANT_02: Create a new tenant with invalid data
try:
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Test Step 1: Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Test Step 2: Enter invalid first name (special characters) in "First Name" field
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("!@#$%^")
    time.sleep(0.5)

    # Test Step 3: Enter invalid last name (numbers only) in "Last Name" field
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("12345")
    time.sleep(0.5)

    # Test Step 4: Enter invalid contact number (alphabets) in "Contact Number" field
    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.send_keys("abcdefg")
    time.sleep(0.5)

    # Test Step 5: Enter invalid email address (without @ symbol) in "Email" field
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("john.doeexample.com")
    time.sleep(0.5)

    # Test Step 6: Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is not created and an error message is displayed
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text:
            log_test_result("TC_TENANT_02", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Tenant is not created and error message is displayed", "Pass")
        else:
            log_test_result("TC_TENANT_02", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Tenant is created successfully", "Fail")
            take_screenshot("TC_TENANT_02_Step_6")
    except Exception as e:
        log_test_result("TC_TENANT_02", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_02_Step_6")

except Exception as e:
    log_test_result("TC_TENANT_02", 1, "Click on 'Add Tenant' button", "Add New Tenant screen is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_02_Step_1")

# Test Case TC_TENANT_03: Create a new tenant with empty data
try:
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Test Step 1: Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Test Step 2: Leave "First Name" field empty
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.clear()
    time.sleep(0.5)

    # Test Step 3: Leave "Last Name" field empty
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.clear()
    time.sleep(0.5)

    # Test Step 4: Leave "Contact Number" field empty
    contact_number_field = driver.find_element(By.ID, "contact_number")
    contact_number_field.clear()
    time.sleep(0.5)

    # Test Step 5: Leave "Email" field empty
    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    time.sleep(0.5)

    # Test Step 6: Click on "Add Tenant" button
    add_tenant_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Tenant')]")
    add_tenant_button.click()
    time.sleep(0.5)

    # Assert that the tenant is not created and an error message is displayed
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text:
            log_test_result("TC_TENANT_03", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Tenant is not created and error message is displayed", "Pass")
        else:
            log_test_result("TC_TENANT_03", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", "Tenant is created successfully", "Fail")
            take_screenshot("TC_TENANT_03_Step_6")
    except Exception as e:
        log_test_result("TC_TENANT_03", 6, "Click on 'Add Tenant' button", "Tenant is not created and error message is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_03_Step_6")

except Exception as e:
    log_test_result("TC_TENANT_03", 1, "Click on 'Add Tenant' button", "Add New Tenant screen is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_03_Step_1")

# Test Case TC_TENANT_04: Cancel tenant creation
try:
    # Navigate to the Add Tenant page
    driver.get(base_url + "add_tenant")

    # Test Step 1: Click on "Add Tenant" button
    add_tenant_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Tenant')]"))
    )
    add_tenant_button.click()
    time.sleep(0.5)

    # Test Step 2: Enter valid data in all fields
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

    # Test Step 3: Click on "Cancel" button
    cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
    cancel_button.click()
    time.sleep(0.5)

    # Assert that the Add New Tenant screen is closed and the user is redirected to the main screen
    try:
        add_tenant_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Tenant')]"))
        )
        if add_tenant_button:
            log_test_result("TC_TENANT_04", 3, "Click on 'Cancel' button", "Add New Tenant screen is closed and user is redirected to the main screen", "Add New Tenant screen is closed and user is redirected to the main screen", "Pass")
        else:
            log_test_result("TC_TENANT_04", 3, "Click on 'Cancel' button", "Add New Tenant screen is closed and user is redirected to the main screen", "Add New Tenant screen is not closed", "Fail")
            take_screenshot("TC_TENANT_04_Step_3")
    except Exception as e:
        log_test_result("TC_TENANT_04", 3, "Click on 'Cancel' button", "Add New Tenant screen is closed and user is redirected to the main screen", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_04_Step_3")

except Exception as e:
    log_test_result("TC_TENANT_04", 1, "Click on 'Add Tenant' button", "Add New Tenant screen is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_04_Step_1")

# Test Case TC_TENANT_05: Edit existing tenant
try:
    # Navigate to the Tenants table
    driver.get(base_url)
    time.sleep(0.5)

    # Test Step 1: Navigate to the Tenants table
    tenants_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
    )
    time.sleep(0.5)

    # Test Step 2: Click on "Actions" button for an existing tenant
    actions_button = tenants_table.find_element(By.XPATH, "//tr[1]/td[3]/button")
    actions_button.click()
    time.sleep(0.5)

    # Test Step 3: Edit the "First Name" field
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.clear()
    first_name_field.send_keys("Jane")
    time.sleep(0.5)

    # Test Step 4: Click on "Save" button
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
    save_button.click()
    time.sleep(0.5)

    # Assert that the tenant details are updated successfully and displayed in the Tenants table
    try:
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        tenant_found = False
        for row in tenant_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "Jane" and cells[1].text == "Doe":
                tenant_found = True
                break
        if tenant_found:
            log_test_result("TC_TENANT_05", 4, "Click on 'Save' button", "Tenant details are updated successfully and displayed in the Tenants table", "Tenant details are updated successfully and displayed in the Tenants table", "Pass")
        else:
            log_test_result("TC_TENANT_05", 4, "Click on 'Save' button", "Tenant details are updated successfully and displayed in the Tenants table", "Tenant details are not updated successfully", "Fail")
            take_screenshot("TC_TENANT_05_Step_4")
    except Exception as e:
        log_test_result("TC_TENANT_05", 4, "Click on 'Save' button", "Tenant details are updated successfully and displayed in the Tenants table", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_05_Step_4")

except Exception as e:
    log_test_result("TC_TENANT_05", 1, "Navigate to the Tenants table", "Tenants table is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_05_Step_1")

# Test Case TC_TENANT_06: Delete existing tenant
try:
    # Navigate to the Tenants table
    driver.get(base_url)
    time.sleep(0.5)

    # Test Step 1: Navigate to the Tenants table
    tenants_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
    )
    time.sleep(0.5)

    # Test Step 2: Click on "Actions" button for an existing tenant
    actions_button = tenants_table.find_element(By.XPATH, "//tr[1]/td[3]/button")
    actions_button.click()
    time.sleep(0.5)

    # Test Step 3: Click on "Delete" button
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")
    delete_button.click()
    time.sleep(0.5)

    # Assert that the tenant is deleted successfully and removed from the Tenants table
    try:
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        tenant_found = False
        for row in tenant_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "Jane" and cells[1].text == "Doe":
                tenant_found = True
                break
        if not tenant_found:
            log_test_result("TC_TENANT_06", 3, "Click on 'Delete' button", "Tenant is deleted successfully and removed from the Tenants table", "Tenant is deleted successfully and removed from the Tenants table", "Pass")
        else:
            log_test_result("TC_TENANT_06", 3, "Click on 'Delete' button", "Tenant is deleted successfully and removed from the Tenants table", "Tenant is not deleted successfully", "Fail")
            take_screenshot("TC_TENANT_06_Step_3")
    except Exception as e:
        log_test_result("TC_TENANT_06", 3, "Click on 'Delete' button", "Tenant is deleted successfully and removed from the Tenants table", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_06_Step_3")

except Exception as e:
    log_test_result("TC_TENANT_06", 1, "Navigate to the Tenants table", "Tenants table is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_06_Step_1")

# Test Case TC_TENANT_07: Search for a tenant
try:
    # Navigate to the Tenants table
    driver.get(base_url)
    time.sleep(0.5)

    # Test Step 1: Navigate to the Tenants table
    tenants_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
    )
    time.sleep(0.5)

    # Test Step 2: Enter a valid first name in the search field
    search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_field.send_keys("John")
    time.sleep(0.5)

    # Assert that tenants matching the entered first name are displayed
    try:
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        tenant_found = False
        for row in tenant_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "John":
                tenant_found = True
                break
        if tenant_found:
            log_test_result("TC_TENANT_07", 2, "Enter a valid first name in the search field", "Tenants matching the entered first name are displayed", "Tenants matching the entered first name are displayed", "Pass")
        else:
            log_test_result("TC_TENANT_07", 2, "Enter a valid first name in the search field", "Tenants matching the entered first name are displayed", "No tenants matching the entered first name are displayed", "Fail")
            take_screenshot("TC_TENANT_07_Step_2")
    except Exception as e:
        log_test_result("TC_TENANT_07", 2, "Enter a valid first name in the search field", "Tenants matching the entered first name are displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_07_Step_2")

    # Test Step 3: Clear the search field
    search_field.clear()
    time.sleep(0.5)

    # Assert that all tenants are displayed again
    try:
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        if len(tenant_rows) > 1:
            log_test_result("TC_TENANT_07", 3, "Clear the search field", "All tenants are displayed again", "All tenants are displayed again", "Pass")
        else:
            log_test_result("TC_TENANT_07", 3, "Clear the search field", "All tenants are displayed again", "Not all tenants are displayed", "Fail")
            take_screenshot("TC_TENANT_07_Step_3")
    except Exception as e:
        log_test_result("TC_TENANT_07", 3, "Clear the search field", "All tenants are displayed again", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_07_Step_3")

except Exception as e:
    log_test_result("TC_TENANT_07", 1, "Navigate to the Tenants table", "Tenants table is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_07_Step_1")

# Test Case TC_TENANT_08: View tenant details
try:
    # Navigate to the Tenants table
    driver.get(base_url)
    time.sleep(0.5)

    # Test Step 1: Navigate to the Tenants table
    tenants_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
    )
    time.sleep(0.5)

    # Test Step 2: Click on the "First Name" of a tenant
    first_name_link = tenants_table.find_element(By.XPATH, "//tr[1]/td[1]/a")
    first_name_link.click()
    time.sleep(0.5)

    # Assert that tenant details are displayed in a separate screen
    try:
        tenant_details_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Tenant Details')]"))
        )
        if tenant_details_header:
            log_test_result("TC_TENANT_08", 2, "Click on the 'First Name' of a tenant", "Tenant details are displayed in a separate screen", "Tenant details are displayed in a separate screen", "Pass")
        else:
            log_test_result("TC_TENANT_08", 2, "Click on the 'First Name' of a tenant", "Tenant details are displayed in a separate screen", "Tenant details are not displayed", "Fail")
            take_screenshot("TC_TENANT_08_Step_2")
    except Exception as e:
        log_test_result("TC_TENANT_08", 2, "Click on the 'First Name' of a tenant", "Tenant details are displayed in a separate screen", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_08_Step_2")

    # Test Step 3: Click on "Back" button
    back_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Back')]")
    back_button.click()
    time.sleep(0.5)

    # Assert that the user is redirected to the Tenants table
    try:
        tenants_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        if tenants_table:
            log_test_result("TC_TENANT_08", 3, "Click on 'Back' button", "User is redirected to the Tenants table", "User is redirected to the Tenants table", "Pass")
        else:
            log_test_result("TC_TENANT_08", 3, "Click on 'Back' button", "User is redirected to the Tenants table", "User is not redirected to the Tenants table", "Fail")
            take_screenshot("TC_TENANT_08_Step_3")
    except Exception as e:
        log_test_result("TC_TENANT_08", 3, "Click on 'Back' button", "User is redirected to the Tenants table", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_TENANT_08_Step_3")

except Exception as e:
    log_test_result("TC_TENANT_08", 1, "Navigate to the Tenants table", "Tenants table is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_TENANT_08_Step_1")

# Test Case TC_PROPERTY_01: Create a new property with valid data
try:
    # Navigate to the Add Property page
    driver.get(base_url + "add_property")

    # Test Step 1: Click on "Add Property" button
    add_property_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add Property')]"))
    )
    add_property_button.click()
    time.sleep(0.5)

    # Test Step 2: Enter valid address line 1 in "Address Line 1" field
    address_line1_field = driver.find_element(By.ID, "address_line1")
    address_line1_field.send_keys("123 Main Street")
    time.sleep(0.5)

    # Test Step 3: Enter valid address line 2 in "Address Line 2" field
    address_line2_field = driver.find_element(By.ID, "address_line2")
    address_line2_field.send_keys("Apt 1")
    time.sleep(0.5)

    # Test Step 4: Enter valid city in "City" field
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("Anytown")
    time.sleep(0.5)

    # Test Step 5: Enter valid state in "State" field
    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("CA")
    time.sleep(0.5)

    # Test Step 6: Enter valid zip code in "Zip Code" field
    zip_code_field = driver.find_element(By.ID, "zip_code")
    zip_code_field.send_keys("12345")
    time.sleep(0.5)

    # Test Step 7: Enter valid status in "Status" field
    status_dropdown = driver.find_element(By.ID, "status")
    status_dropdown.select_by_value("to rent")
    time.sleep(0.5)

    # Test Step 8: Enter valid unit number in "Unit Number" field
    unit_number_field = driver.find_element(By.ID, "unit_number")
    unit_number_field.send_keys("1")
    time.sleep(0.5)

    # Test Step 9: Click on "Add Property" button
    add_property_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Property')]")
    add_property_button.click()
    time.sleep(0.5)

    # Assert that the property is created successfully
    try:
        property_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]"))
        )
        property_rows = property_table.find_elements(By.TAG_NAME, "tr")
        property_found = False
        for row in property_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "123 Main Street" and cells[1].text == "Anytown" and cells[2].text == "CA" and cells[3].text == "12345":
                property_found = True
                break
        if property_found:
            log_test_result("TC_PROPERTY_01", 9, "Click on 'Add Property' button", "Property is created successfully and displayed in the Properties table", "Property is created successfully and displayed in the Properties table", "Pass")
        else:
            log_test_result("TC_PROPERTY_01", 9, "Click on 'Add Property' button", "Property is created successfully and displayed in the Properties table", "Property is not created successfully", "Fail")
            take_screenshot("TC_PROPERTY_01_Step_9")
    except Exception as e:
        log_test_result("TC_PROPERTY_01", 9, "Click on 'Add Property' button", "Property is created successfully and displayed in the Properties table", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
        take_screenshot("TC_PROPERTY_01_Step_9")

except Exception as e:
    log_test_result("TC_PROPERTY_01", 1, "Click on 'Add Property' button", "Add New Property screen is displayed", f"Test step failed: {getattr(e, 'msg', str(e))}", "Fail")
    take_screenshot("TC_PROPERTY_01_Step_1")

# Test Case TC_PROPERTY_02: Create a new property with invalid data
try:
    # Navigate to the Add Property page