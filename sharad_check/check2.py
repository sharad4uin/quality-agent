```python
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
def test_tc_tenant_01():
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

    # Wait for the tenant to be created and displayed in the Tenants table
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']/tbody/tr[1]/td[1]")))

    # Verify that the tenant is created successfully
    tenant_name = driver.find_element(By.XPATH, "//table[@class='table table-striped']/tbody/tr[1]/td[1]").text
    assert tenant_name == "John"

# Test Case TC_TENANT_02: Create a new tenant with invalid data - empty first name
def test_tc_tenant_02():
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

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "First Name is required" in error_message

# Test Case TC_TENANT_03: Create a new tenant with invalid data - invalid email address
def test_tc_tenant_03():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter an invalid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Invalid email address" in error_message

# Test Case TC_TENANT_04: Create a new tenant with invalid data - special characters in first name
def test_tc_tenant_04():
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

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Invalid first name" in error_message

# Test Case TC_TENANT_05: Create a new tenant with invalid data - special characters in last name
def test_tc_tenant_05():
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

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Invalid last name" in error_message

# Test Case TC_TENANT_06: Create a new tenant with invalid data - invalid contact number
def test_tc_tenant_06():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter an invalid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("12345678901234567890")

    # Enter a valid email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Invalid contact number" in error_message

# Test Case TC_TENANT_07: Cancel tenant creation
def test_tc_tenant_07():
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

    # Wait for the Add New Tenant screen to be closed
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//h1[text()='Add New Tenant']")))

    # Verify that no tenant is created
    assert driver.find_element(By.XPATH, "//table[@class='table table-striped']/tbody/tr").is_displayed() == False

# Test Case TC_TENANT_08: Create a new tenant with existing email address
def test_tc_tenant_08():
    # Click on "Add Tenant" button
    driver.find_element(By.LINK_TEXT, "Add Tenant").click()

    # Enter a valid first name in the "First Name" field
    driver.find_element(By.ID, "first_name").send_keys("John")

    # Enter a valid last name in the "Last Name" field
    driver.find_element(By.ID, "last_name").send_keys("Doe")

    # Enter a valid contact number in the "Contact Number" field
    driver.find_element(By.ID, "contact_number").send_keys("1234567890")

    # Enter an existing email address in the "Email" field
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Click on "Add Tenant" button
    driver.find_element(By.XPATH, "//button[text()='Add Tenant']").click()

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Email address already exists" in error_message

# Test Case TC_TENANT_09: Create a new tenant with existing contact number
def test_tc_tenant_09():
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

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))

    # Verify that the error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']").text
    assert "Contact number already exists" in error_message

# Test Case TC_TENANT_10: Create a new tenant with empty contact number
def test_tc_tenant_10():
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

    # Wait for the tenant to be created and displayed in the Tenants table
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']/tbody/tr[1]/td[1]")))

    # Verify that the tenant is created successfully
    tenant_name = driver.find_element(By.XPATH, "//table[@class='table table-striped']/tbody/tr[1]/td[1]").text
    assert tenant_name == "John"

# Run the test cases
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

# Close the browser
driver.quit()
```

**Explanation:**

1. **Import necessary libraries:**
   - `selenium` for web automation
   - `webdriver.Chrome` to use Chrome browser
   - `By` for locating elements
   - `WebDriverWait` for explicit waits
   - `expected_conditions` for wait conditions
   - `time` for pausing execution

2. **Initialize WebDriver:**
   - Create a `webdriver.Chrome` instance to control Chrome.

3. **Navigate to the landing page:**
   - Use `driver.get()` to open the application URL.

4. **Define test functions:**
   - Each test case is implemented as a separate function.
   - Functions follow the pattern:
     - `test_tc_tenant_XX()`, where `XX` is the test case ID.
   - Inside each function:
     - Locate elements using `driver.find_element()` with appropriate locators (e.g., `By.ID`, `By.XPATH`, `By.LINK_TEXT`).
     - Perform actions like clicking, typing, and waiting.
     - Use `assert` statements to verify expected results.

5. **Run test cases:**
   - Call each test function to execute the test cases.

6. **Close the browser:**
   - Use `driver.quit()` to close the browser window after all tests are completed.

**Key points:**

- **Locators:** The code uses various locators to find elements:
  - `By.ID`: For elements with unique IDs.
  - `By.XPATH`: For complex element selection using XPath expressions.
  - `By.LINK_TEXT`: For links with specific text.
- **Explicit waits:** `WebDriverWait` is used to wait for specific conditions before performing actions, ensuring that the elements are loaded before interacting with them.
- **Assertions:** `assert` statements are used to verify expected results and raise an error if the condition is not met.
- **Test case structure:** Each test case is a separate function, making the code more organized and readable.

**Remember to:**

- Install the necessary libraries (`pip install selenium`).
- Download the ChromeDriver for your Chrome version and place it in your system's PATH.
- Adjust the locators and test steps based on the actual application's HTML structure.
- Add more test cases to cover all the required functionalities.
