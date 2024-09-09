
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

# Test Case 1: Create a new tenant with valid data
def test_tc_tenant_01():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter valid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is created successfully
        tenant_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table-striped')]/tbody"))
        )
        tenant_rows = tenant_table.find_elements(By.TAG_NAME, "tr")
        for row in tenant_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells[0].text == "John" and cells[1].text == "Doe":
                print("Test Case TC_TENANT_01: Passed")
                passed_tests += 1
                return

        print("Test Case TC_TENANT_01: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_01_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_01: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_01_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 2: Create a new tenant with invalid data - empty first name
def test_tc_tenant_02():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "First name is required":
            print("Test Case TC_TENANT_02: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_02: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_02_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_02: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_02_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 3: Create a new tenant with invalid data - invalid email address
def test_tc_tenant_03():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Invalid email address":
            print("Test Case TC_TENANT_03: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_03: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_03_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_03: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_03_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 4: Create a new tenant with invalid data - special characters in first name
def test_tc_tenant_04():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John!")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Invalid first name":
            print("Test Case TC_TENANT_04: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_04: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_04_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_04: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_04_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 5: Create a new tenant with invalid data - special characters in last name
def test_tc_tenant_05():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe!")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Invalid last name":
            print("Test Case TC_TENANT_05: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_05: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_05_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_05: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_05_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 6: Create a new tenant with invalid data - invalid contact number
def test_tc_tenant_06():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("123456789")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Invalid contact number":
            print("Test Case TC_TENANT_06: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_06: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_06_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_06: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_06_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 7: Cancel tenant creation
def test_tc_tenant_07():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter valid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Cancel button
        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        time.sleep(0.5)

        # Verify that the user is redirected to the main screen
        if driver.current_url == base_url:
            print("Test Case TC_TENANT_07: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_07: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_07_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_07: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_07_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 8: Create a new tenant with existing email address
def test_tc_tenant_08():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Email address already exists":
            print("Test Case TC_TENANT_08: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_08: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_08_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_08: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_08_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 9: Create a new tenant with existing contact number
def test_tc_tenant_09():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe1@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Contact number already exists":
            print("Test Case TC_TENANT_09: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_09: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_09_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_09: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_09_error_screenshot.png")
        print(f"Error: {e}")

# Test Case 10: Create a new tenant with empty last name
def test_tc_tenant_10():
    global passed_tests, failed_tests
    try:
        # Navigate to the Add Tenant page
        driver.get(base_url + "add_tenant")

        # Enter invalid data in the fields
        driver.find_element(By.ID, "first_name").send_keys("John")
        driver.find_element(By.ID, "last_name").send_keys("")
        driver.find_element(By.ID, "contact_number").send_keys("1234567890")
        driver.find_element(By.ID, "email").send_keys("john.doe2@example.com")

        # Click on the Add Tenant button
        driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()
        time.sleep(0.5)

        # Verify that the tenant is not created and an error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        if error_message.text == "Last name is required":
            print("Test Case TC_TENANT_10: Passed")
            passed_tests += 1
            return

        print("Test Case TC_TENANT_10: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_10_error_screenshot.png")

    except Exception as e:
        print(f"Test Case TC_TENANT_10: Failed")
        failed_tests += 1
        driver.save_screenshot("TC_TENANT_10_error_screenshot.png")
        print(f"Error: {e}")

# Run all test cases
test_tc_tenant_01()
test_tc_tenant_02()
test_tc_tenant_03()
test_tc_tenant_04()
test_tc_tenant_05()
test_tc_tenant_06()
test_tc_tenant_07()
test_tc_tenant_08()
test_tc_tenant_09()
test_tc_tenant_10()

# Generate test report
print(f"\nTest Report:")
print(f"Passed Tests: {passed_tests}")
print(f"Failed Tests: {failed_tests}")

# Close the WebDriver
driver.quit()