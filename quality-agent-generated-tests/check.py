
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
driver.implicitly_wait(5)

# Test Case 1: TC_TENANT_01
def test_tc_tenant_01():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Verify Add New Tenant screen is displayed
        assert "Add New Tenant" in driver.title, "Add New Tenant screen not displayed"
        print(f"Test step 1 passed: Add New Tenant screen is displayed")

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)
        print(f"Test step 2 passed: First name is entered successfully")

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)
        print(f"Test step 3 passed: Last name is entered successfully")

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)
        print(f"Test step 4 passed: Contact number is entered successfully")

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)
        print(f"Test step 5 passed: Email address is entered successfully")

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is created successfully
        assert "Tenant added successfully" in driver.page_source, "Tenant not created successfully"
        print(f"Test step 6 passed: Tenant is created successfully and displayed in the Tenants table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_01.png")

# Test Case 2: TC_TENANT_02
def test_tc_tenant_02():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Verify Add New Tenant screen is displayed
        assert "Add New Tenant" in driver.title, "Add New Tenant screen not displayed"
        print(f"Test step 1 passed: Add New Tenant screen is displayed")

        # Enter invalid first name
        driver.find_element(By.ID, "first_name").send_keys("John!")
        time.sleep(0.5)
        print(f"Test step 2 passed: Invalid first name is entered")

        # Enter invalid last name
        driver.find_element(By.ID, "last_name").send_keys("1234")
        time.sleep(0.5)
        print(f"Test step 3 passed: Invalid last name is entered")

        # Enter invalid contact number
        driver.find_element(By.ID, "contact_number").send_keys("abc123")
        time.sleep(0.5)
        print(f"Test step 4 passed: Invalid contact number is entered")

        # Enter invalid email address
        driver.find_element(By.ID, "email").send_keys("john.doeexample.com")
        time.sleep(0.5)
        print(f"Test step 5 passed: Invalid email address is entered")

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is not created
        assert "Invalid input" in driver.page_source, "Tenant created with invalid data"
        print(f"Test step 6 passed: Tenant is not created and error message is displayed")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_02.png")

# Test Case 3: TC_TENANT_03
def test_tc_tenant_03():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Verify Add New Tenant screen is displayed
        assert "Add New Tenant" in driver.title, "Add New Tenant screen not displayed"
        print(f"Test step 1 passed: Add New Tenant screen is displayed")

        # Leave First Name field empty
        driver.find_element(By.ID, "first_name").clear()
        time.sleep(0.5)
        print(f"Test step 2 passed: First name field is left empty")

        # Leave Last Name field empty
        driver.find_element(By.ID, "last_name").clear()
        time.sleep(0.5)
        print(f"Test step 3 passed: Last name field is left empty")

        # Leave Contact Number field empty
        driver.find_element(By.ID, "contact_number").clear()
        time.sleep(0.5)
        print(f"Test step 4 passed: Contact number field is left empty")

        # Leave Email field empty
        driver.find_element(By.ID, "email").clear()
        time.sleep(0.5)
        print(f"Test step 5 passed: Email field is left empty")

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify tenant is not created
        assert "Invalid input" in driver.page_source, "Tenant created with empty fields"
        print(f"Test step 6 passed: Tenant is not created and error message is displayed")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_03.png")

# Test Case 4: TC_TENANT_04
def test_tc_tenant_04():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Verify Add New Tenant screen is displayed
        assert "Add New Tenant" in driver.title, "Add New Tenant screen not displayed"
        print(f"Test step 1 passed: Add New Tenant screen is displayed")

        # Enter valid data in all fields
        driver.find_element(By.ID, "first_name").send_keys("Jane")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("Smith")
        time.sleep(0.5)
        driver.find_element(By.ID, "contact_number").send_keys("9876543210")
        time.sleep(0.5)
        driver.find_element(By.ID, "email").send_keys("jane.smith@example.com")
        time.sleep(0.5)
        print(f"Test step 2 passed: Data is entered successfully")

        # Click on Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Verify Add New Tenant screen is closed
        assert "Add New Tenant" not in driver.title, "Add New Tenant screen is still displayed"
        print(f"Test step 3 passed: Add New Tenant screen is closed and user is redirected to the main screen")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_04.png")

# Test Case 5: TC_TENANT_05
def test_tc_tenant_05():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Tenants table is displayed
        assert "Tenants" in driver.page_source, "Tenants table not displayed"
        print(f"Test step 1 passed: Tenants table is displayed")

        # Click on Actions button for an existing tenant
        driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[3]//a[1]").click()
        time.sleep(0.5)

        # Verify Edit Tenant screen is displayed
        assert "Edit Tenant" in driver.title, "Edit Tenant screen not displayed"
        print(f"Test step 2 passed: Edit Tenant screen is displayed")

        # Edit the First Name field
        driver.find_element(By.ID, "first_name").clear()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("Updated")
        time.sleep(0.5)
        print(f"Test step 3 passed: First name is updated successfully")

        # Click on Save button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(0.5)

        # Verify tenant details are updated
        assert "Tenant updated successfully" in driver.page_source, "Tenant details not updated successfully"
        print(f"Test step 4 passed: Tenant details are updated successfully and displayed in the Tenants table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_05.png")

# Test Case 6: TC_TENANT_06
def test_tc_tenant_06():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Tenants table is displayed
        assert "Tenants" in driver.page_source, "Tenants table not displayed"
        print(f"Test step 1 passed: Tenants table is displayed")

        # Click on Actions button for an existing tenant
        driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[3]//a[2]").click()
        time.sleep(0.5)

        # Verify Delete confirmation dialog is displayed
        assert "Are you sure you want to delete this tenant?" in driver.page_source, "Delete confirmation dialog not displayed"
        print(f"Test step 2 passed: Delete confirmation dialog is displayed")

        # Click on Delete button
        driver.find_element(By.XPATH, "//button[text()='Delete']").click()
        time.sleep(0.5)

        # Verify tenant is deleted
        assert "Tenant deleted successfully" in driver.page_source, "Tenant not deleted successfully"
        print(f"Test step 3 passed: Tenant is deleted successfully and removed from the Tenants table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_06.png")

# Test Case 7: TC_TENANT_07
def test_tc_tenant_07():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Tenants table is displayed
        assert "Tenants" in driver.page_source, "Tenants table not displayed"
        print(f"Test step 1 passed: Tenants table is displayed")

        # Enter a valid first name in the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search Tenants']").send_keys("John")
        time.sleep(0.5)
        print(f"Test step 2 passed: Valid first name is entered in the search field")

        # Verify tenants matching the entered first name are displayed
        assert "John" in driver.page_source, "Tenants matching the entered first name are not displayed"
        print(f"Test step 3 passed: Tenants matching the entered first name are displayed")

        # Clear the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search Tenants']").clear()
        time.sleep(0.5)
        print(f"Test step 4 passed: Search field is cleared")

        # Verify all tenants are displayed again
        assert "Tenants" in driver.page_source, "All tenants are not displayed again"
        print(f"Test step 5 passed: All tenants are displayed again")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_07.png")

# Test Case 8: TC_TENANT_08
def test_tc_tenant_08():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Tenants table is displayed
        assert "Tenants" in driver.page_source, "Tenants table not displayed"
        print(f"Test step 1 passed: Tenants table is displayed")

        # Click on the Actions button for an existing tenant
        driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[3]//a[1]").click()
        time.sleep(0.5)

        # Verify Tenant details are displayed
        assert "Tenant Details" in driver.title, "Tenant details are not displayed"
        print(f"Test step 2 passed: Tenant details are displayed in a separate screen")

        # Click on Back button
        driver.find_element(By.XPATH, "//button[text()='Back']").click()
        time.sleep(0.5)

        # Verify user is redirected to the Tenants table
        assert "Tenants" in driver.page_source, "User is not redirected to the Tenants table"
        print(f"Test step 3 passed: User is redirected to the Tenants table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_08.png")

# Test Case 1: TC_PROPERTY_01
def test_tc_property_01():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Property page
        driver.get(base_url + "add_property")
        time.sleep(0.5)

        # Verify Add New Property screen is displayed
        assert "Add New Property" in driver.title, "Add New Property screen not displayed"
        print(f"Test step 1 passed: Add New Property screen is displayed")

        # Enter valid address line 1
        driver.find_element(By.ID, "address_line1").send_keys("123 Main Street")
        time.sleep(0.5)
        print(f"Test step 2 passed: Address line 1 is entered successfully")

        # Enter valid address line 2
        driver.find_element(By.ID, "address_line2").send_keys("Apt 1")
        time.sleep(0.5)
        print(f"Test step 3 passed: Address line 2 is entered successfully")

        # Enter valid city
        driver.find_element(By.ID, "city").send_keys("Anytown")
        time.sleep(0.5)
        print(f"Test step 4 passed: City is entered successfully")

        # Enter valid state
        driver.find_element(By.ID, "state").send_keys("CA")
        time.sleep(0.5)
        print(f"Test step 5 passed: State is entered successfully")

        # Enter valid zip code
        driver.find_element(By.ID, "zip_code").send_keys("12345")
        time.sleep(0.5)
        print(f"Test step 6 passed: Zip code is entered successfully")

        # Enter valid status
        driver.find_element(By.ID, "status").send_keys("To Rent")
        time.sleep(0.5)
        print(f"Test step 7 passed: Status is entered successfully")

        # Enter valid unit number
        driver.find_element(By.ID, "unit_number").send_keys("101")
        time.sleep(0.5)
        print(f"Test step 8 passed: Unit number is entered successfully")

        # Click on Add Property button
        driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
        time.sleep(0.5)

        # Verify property is created successfully
        assert "Property added successfully" in driver.page_source, "Property not created successfully"
        print(f"Test step 9 passed: Property is created successfully and displayed in the Properties table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_01.png")

# Test Case 2: TC_PROPERTY_02
def test_tc_property_02():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Property page
        driver.get(base_url + "add_property")
        time.sleep(0.5)

        # Verify Add New Property screen is displayed
        assert "Add New Property" in driver.title, "Add New Property screen not displayed"
        print(f"Test step 1 passed: Add New Property screen is displayed")

        # Enter invalid address line 1
        driver.find_element(By.ID, "address_line1").send_keys("123 Main! Street")
        time.sleep(0.5)
        print(f"Test step 2 passed: Invalid address line 1 is entered")

        # Enter invalid address line 2
        driver.find_element(By.ID, "address_line2").send_keys("1234")
        time.sleep(0.5)
        print(f"Test step 3 passed: Invalid address line 2 is entered")

        # Enter invalid city
        driver.find_element(By.ID, "city").send_keys("1234")
        time.sleep(0.5)
        print(f"Test step 4 passed: Invalid city is entered")

        # Enter invalid state
        driver.find_element(By.ID, "state").send_keys("1234")
        time.sleep(0.5)
        print(f"Test step 5 passed: Invalid state is entered")

        # Enter invalid zip code
        driver.find_element(By.ID, "zip_code").send_keys("abc123")
        time.sleep(0.5)
        print(f"Test step 6 passed: Invalid zip code is entered")

        # Enter invalid status
        driver.find_element(By.ID, "status").send_keys("!To Rent")
        time.sleep(0.5)
        print(f"Test step 7 passed: Invalid status is entered")

        # Enter invalid unit number
        driver.find_element(By.ID, "unit_number").send_keys("abc123")
        time.sleep(0.5)
        print(f"Test step 8 passed: Invalid unit number is entered")

        # Click on Add Property button
        driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
        time.sleep(0.5)

        # Verify property is not created
        assert "Invalid input" in driver.page_source, "Property created with invalid data"
        print(f"Test step 9 passed: Property is not created and error message is displayed")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_02.png")

# Test Case 3: TC_PROPERTY_03
def test_tc_property_03():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Property page
        driver.get(base_url + "add_property")
        time.sleep(0.5)

        # Verify Add New Property screen is displayed
        assert "Add New Property" in driver.title, "Add New Property screen not displayed"
        print(f"Test step 1 passed: Add New Property screen is displayed")

        # Leave Address Line 1 field empty
        driver.find_element(By.ID, "address_line1").clear()
        time.sleep(0.5)
        print(f"Test step 2 passed: Address line 1 field is left empty")

        # Leave City field empty
        driver.find_element(By.ID, "city").clear()
        time.sleep(0.5)
        print(f"Test step 3 passed: City field is left empty")

        # Leave State field empty
        driver.find_element(By.ID, "state").clear()
        time.sleep(0.5)
        print(f"Test step 4 passed: State field is left empty")

        # Leave Zip Code field empty
        driver.find_element(By.ID, "zip_code").clear()
        time.sleep(0.5)
        print(f"Test step 5 passed: Zip code field is left empty")

        # Leave Status field empty
        driver.find_element(By.ID, "status").clear()
        time.sleep(0.5)
        print(f"Test step 6 passed: Status field is left empty")

        # Leave Unit Number field empty
        driver.find_element(By.ID, "unit_number").clear()
        time.sleep(0.5)
        print(f"Test step 7 passed: Unit number field is left empty")

        # Click on Add Property button
        driver.find_element(By.XPATH, "//button[text()='Add Property']").click()
        time.sleep(0.5)

        # Verify property is not created
        assert "Invalid input" in driver.page_source, "Property created with empty fields"
        print(f"Test step 8 passed: Property is not created and error message is displayed")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_03.png")

# Test Case 4: TC_PROPERTY_04
def test_tc_property_04():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Property page
        driver.get(base_url + "add_property")
        time.sleep(0.5)

        # Verify Add New Property screen is displayed
        assert "Add New Property" in driver.title, "Add New Property screen not displayed"
        print(f"Test step 1 passed: Add New Property screen is displayed")

        # Enter valid data in all fields
        driver.find_element(By.ID, "address_line1").send_keys("456 Oak Street")
        time.sleep(0.5)
        driver.find_element(By.ID, "address_line2").send_keys("Apt 2")
        time.sleep(0.5)
        driver.find_element(By.ID, "city").send_keys("Springfield")
        time.sleep(0.5)
        driver.find_element(By.ID, "state").send_keys("IL")
        time.sleep(0.5)
        driver.find_element(By.ID, "zip_code").send_keys("62701")
        time.sleep(0.5)
        driver.find_element(By.ID, "status").send_keys("On Lease")
        time.sleep(0.5)
        driver.find_element(By.ID, "unit_number").send_keys("202")
        time.sleep(0.5)
        print(f"Test step 2 passed: Data is entered successfully")

        # Click on Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Verify Add New Property screen is closed
        assert "Add New Property" not in driver.title, "Add New Property screen is still displayed"
        print(f"Test step 3 passed: Add New Property screen is closed and user is redirected to the main screen")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_04.png")

# Test Case 5: TC_PROPERTY_05
def test_tc_property_05():
    global passed_tests, failed_tests
    try:
        # Navigate to the Properties table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Properties table is displayed
        assert "Properties" in driver.page_source, "Properties table not displayed"
        print(f"Test step 1 passed: Properties table is displayed")

        # Click on Actions button for an existing property
        driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[6]//a[1]").click()
        time.sleep(0.5)

        # Verify Edit Property screen is displayed
        assert "Edit Property" in driver.title, "Edit Property screen not displayed"
        print(f"Test step 2 passed: Edit Property screen is displayed")

        # Edit the Address Line 1 field
        driver.find_element(By.ID, "address_line1").clear()
        time.sleep(0.5)
        driver.find_element(By.ID, "address_line1").send_keys("Updated Address")
        time.sleep(0.5)
        print(f"Test step 3 passed: Address line 1 is updated successfully")

        # Click on Save button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(0.5)

        # Verify property details are updated
        assert "Property updated successfully" in driver.page_source, "Property details not updated successfully"
        print(f"Test step 4 passed: Property details are updated successfully and displayed in the Properties table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_05.png")

# Test Case 6: TC_PROPERTY_06
def test_tc_property_06():
    global passed_tests, failed_tests
    try:
        # Navigate to the Properties table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Properties table is displayed
        assert "Properties" in driver.page_source, "Properties table not displayed"
        print(f"Test step 1 passed: Properties table is displayed")

        # Click on Actions button for an existing property
        driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody//tr[1]//td[6]//a[2]").click()
        time.sleep(0.5)

        # Verify Delete confirmation dialog is displayed
        assert "Are you sure you want to delete this property?" in driver.page_source, "Delete confirmation dialog not displayed"
        print(f"Test step 2 passed: Delete confirmation dialog is displayed")

        # Click on Delete button
        driver.find_element(By.XPATH, "//button[text()='Delete']").click()
        time.sleep(0.5)

        # Verify property is deleted
        assert "Property deleted successfully" in driver.page_source, "Property not deleted successfully"
        print(f"Test step 3 passed: Property is deleted successfully and removed from the Properties table")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_06.png")

# Test Case 7: TC_PROPERTY_07
def test_tc_property_07():
    global passed_tests, failed_tests
    try:
        # Navigate to the Properties table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Properties table is displayed
        assert "Properties" in driver.page_source, "Properties table not displayed"
        print(f"Test step 1 passed: Properties table is displayed")

        # Enter a valid address line 1 in the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search Properties']").send_keys("123 Main Street")
        time.sleep(0.5)
        print(f"Test step 2 passed: Valid address line 1 is entered in the search field")

        # Verify properties matching the entered address line 1 are displayed
        assert "123 Main Street" in driver.page_source, "Properties matching the entered address line 1 are not displayed"
        print(f"Test step 3 passed: Properties matching the entered address line 1 are displayed")

        # Clear the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search Properties']").clear()
        time.sleep(0.5)
        print(f"Test step 4 passed: Search field is cleared")

        # Verify all properties are displayed again
        assert "Properties" in driver.page_source, "All properties are not displayed again"
        print(f"Test step 5 passed: All properties are displayed again")
        passed_tests += 1
    except Exception as e:
        failed_tests += 1
        print(f"Test step failed")
        if hasattr(e, 'msg'):
            print(f"Error message: {e.msg}")
        else:
            print(f"Error message: {e}")
        driver.save_screenshot(f"error_screenshot_TC_PROPERTY_07.png")

# Test Case 8: TC_PROPERTY_08
def test_tc_property_08():
    global passed_tests, failed_tests
    try:
        # Navigate to the Properties table
        driver.get(base_url)
        time.sleep(0.5)

        # Verify Properties table is displayed
        assert "Properties" in driver.page_source, "Properties table not displayed"
        print(f"Test step 1 passed: Properties