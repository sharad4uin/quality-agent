
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
driver.implicitly_wait(10)

# Test Case TC_TENANT_01: Create a new tenant with valid data
def test_tc_tenant_01():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid first name
        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(0.5)

        # Enter valid last name
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(0.5)

        # Enter valid contact number
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        time.sleep(0.5)

        # Enter valid email address
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Assert that the tenant is created successfully
        assert "Tenant added successfully" in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_01: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_01: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_01.png")

# Test Case TC_TENANT_02: Create a new tenant with invalid data
def test_tc_tenant_02():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter invalid first name
        driver.find_element(By.ID, "first_name").send_keys("!@#$%^")
        time.sleep(0.5)

        # Enter invalid last name
        driver.find_element(By.ID, "last_name").send_keys("1234567")
        time.sleep(0.5)

        # Enter invalid contact number
        driver.find_element(By.ID, "contact_number").send_keys("abcdefg")
        time.sleep(0.5)

        # Enter invalid email address
        driver.find_element(By.ID, "email").send_keys("john.doeexample.com")
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Assert that the tenant is not created and an error message is displayed
        assert "Invalid first name" in driver.page_source
        assert "Invalid last name" in driver.page_source
        assert "Invalid contact number" in driver.page_source
        assert "Invalid email address" in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_02: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_02: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_02.png")

# Test Case TC_TENANT_03: Create a new tenant with empty fields
def test_tc_tenant_03():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Leave First Name field empty
        driver.find_element(By.ID, "first_name").clear()
        time.sleep(0.5)

        # Leave Last Name field empty
        driver.find_element(By.ID, "last_name").clear()
        time.sleep(0.5)

        # Leave Contact Number field empty
        driver.find_element(By.ID, "contact_number").clear()
        time.sleep(0.5)

        # Leave Email field empty
        driver.find_element(By.ID, "email").clear()
        time.sleep(0.5)

        # Click on Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Assert that the tenant is not created and an error message is displayed
        assert "First name is required" in driver.page_source
        assert "Last name is required" in driver.page_source
        assert "Email is required" in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_03: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_03: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_03.png")

# Test Case TC_TENANT_04: Cancel tenant creation
def test_tc_tenant_04():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")
        time.sleep(0.5)

        # Enter valid data in all fields
        driver.find_element(By.ID, "first_name").send_keys("Jane")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("Smith")
        time.sleep(0.5)
        driver.find_element(By.ID, "contact_number").send_keys("9876543210")
        time.sleep(0.5)
        driver.find_element(By.ID, "email").send_keys("jane.smith@example.com")
        time.sleep(0.5)

        # Click on Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Assert that the Add New Tenant screen is closed and the user is redirected to the main screen
        assert "Lease Management System" in driver.title
        passed_tests += 1
        print(f"Test Case TC_TENANT_04: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_04: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_04.png")

# Test Case TC_TENANT_05: Edit existing tenant
def test_tc_tenant_05():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Create a new tenant for editing
        driver.find_element(By.XPATH, "//a[text()='Add Tenant']").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("Test")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Click on Actions button for the newly created tenant
        driver.find_element(By.XPATH, "//td[text()='Test']/following-sibling::td/a").click()
        time.sleep(0.5)

        # Edit the First Name field
        driver.find_element(By.ID, "first_name").clear()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("Updated")
        time.sleep(0.5)

        # Click on Save button
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(0.5)

        # Assert that the tenant details are updated successfully
        assert "Updated" in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_05: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_05: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_05.png")

# Test Case TC_TENANT_06: Delete existing tenant
def test_tc_tenant_06():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Create a new tenant for deletion
        driver.find_element(By.XPATH, "//a[text()='Add Tenant']").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("Delete")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Click on Actions button for the newly created tenant
        driver.find_element(By.XPATH, "//td[text()='Delete']/following-sibling::td/a").click()
        time.sleep(0.5)

        # Click on Delete button
        driver.find_element(By.XPATH, "//button[text()='Delete']").click()
        time.sleep(0.5)

        # Assert that the tenant is deleted successfully
        assert "Delete" not in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_06: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_06: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_06.png")

# Test Case TC_TENANT_07: Search for a tenant
def test_tc_tenant_07():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Create a new tenant for searching
        driver.find_element(By.XPATH, "//a[text()='Add Tenant']").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("Search")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Enter a valid first name in the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Search")
        time.sleep(0.5)

        # Assert that tenants matching the entered first name are displayed
        assert "Search" in driver.page_source
        assert "User" in driver.page_source

        # Clear the search field
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").clear()
        time.sleep(0.5)

        # Assert that all tenants are displayed again
        assert "Search" in driver.page_source
        assert "User" in driver.page_source
        passed_tests += 1
        print(f"Test Case TC_TENANT_07: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_07: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_07.png")

# Test Case TC_TENANT_08: View tenant details
def test_tc_tenant_08():
    global passed_tests, failed_tests
    try:
        # Navigate to the Tenants table
        driver.get(base_url)
        time.sleep(0.5)

        # Create a new tenant for viewing details
        driver.find_element(By.XPATH, "//a[text()='Add Tenant']").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "first_name").send_keys("View")
        time.sleep(0.5)
        driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Click on the First Name of a tenant
        driver.find_element(By.XPATH, "//td[text()='View']").click()
        time.sleep(0.5)

        # Assert that tenant details are displayed in a separate screen
        assert "View" in driver.page_source
        assert "User" in driver.page_source

        # Click on Back button
        driver.find_element(By.XPATH, "//button[text()='Back']").click()
        time.sleep(0.5)

        # Assert that the user is redirected to the Tenants table
        assert "Lease Management System" in driver.title
        passed_tests += 1
        print(f"Test Case TC_TENANT_08: Passed")
    except Exception as e:
        failed_tests += 1
        print(f"Test Case TC_TENANT_08: Failed")
        if hasattr(e, 'msg'):
            print(f"Error: {e.msg}")
        else:
            print(f"Error: {e}")
        driver.save_screenshot(f"error_screenshot_TC_TENANT_08.png")

# Execute all test cases
test_tc_tenant_01()
test_tc_tenant_02()
test_tc_tenant_03()
test_tc_tenant_04()
test_tc_tenant_05()
test_tc_tenant_06()
test_tc_tenant_07()
test_tc_tenant_08()

# Generate test report
print(f"\nTest Report:")
print(f"Total Passed Tests: {passed_tests}")
print(f"Total Failed Tests: {failed_tests}")

# Close the WebDriver
driver.quit()