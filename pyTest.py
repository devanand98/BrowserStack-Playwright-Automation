import json
import urllib
import subprocess
import pytest
from playwright.sync_api import sync_playwright

# Desired capabilities for BrowserStack
desired_cap = {
    'browser': 'chrome',
    'browser_version': 'latest',
    'os': 'osx',
    'os_version': 'catalina',
    'name': 'BrowserStack Demo',
    'build': 'playwright-python-tutorial',
    'browserstack.username': 'BROWSERSTACK_USERNAME',
    'browserstack.accessKey': 'BROWSERSTACK_ACCESS_KEY'
}

# Get the Playwright version installed
clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
desired_cap['client.playwrightVersion'] = clientPlaywrightVersion

# Test 1: Login Test
@pytest.mark.login
def test_login(playwright):
    # Modify desired capabilities for the test
    desired_cap['browser'] = "edge"
    desired_cap['name'] = "Test Login"
    
    # URL for BrowserStack with the test capabilities
    cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(desired_cap))
    browser = playwright.chromium.connect(cdpUrl)  # Connect to BrowserStack
    page = browser.new_page()  # Create a new page for interaction
    
    try:
        page.goto("https://bstackdemo.com/")  # Go to the demo site
        page.click('#signin')  # Click sign-in button
        page.get_by_text("Select Username").click()  # Select username option
        page.locator("#react-select-2-option-0-0").click()  # Choose a username
        page.get_by_text("Select Password").click()  # Select password option
        page.locator("#react-select-3-option-0-0").click()  # Choose a password
        page.get_by_role("button", name="Log In").click()  # Click the login button
        
        if page.get_by_text("demouser").is_visible():
            mark_test_status("passed", "User successfully logged in", page)
        else:
            mark_test_status("failed", "User login failure", page)
    except Exception as err:
        mark_test_status("failed", str(err), page)
    
    browser.close()  # Close the browser

# Test 2: Item Purchase Test
@pytest.mark.item_purchase
def test_item_purchase(playwright):
    # Modify desired capabilities for the test
    desired_cap['browser'] = "chrome"
    desired_cap['name'] = "Test Item Purchase"
    
    # URL for BrowserStack with the test capabilities
    cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(desired_cap))
    browser = playwright.chromium.connect(cdpUrl)  # Connect to BrowserStack
    page = browser.new_page()  # Create a new page for interaction
    
    try:
        page.goto("https://bstackdemo.com/")  # Go to the demo site
        page.locator("[id=\"\\35 \"]").get_by_text("Add to cart").click()  # Add an item to the cart
        page.get_by_text("Checkout").click()  # Proceed to checkout
        page.type("#react-select-2-input", "demouser\n")  # Type username
        page.type("#react-select-3-input", "testingisfun99\n")  # Type password
        page.get_by_role("button", name="Log In").click()  # Click the login button
        
        # Fill in checkout information
        page.get_by_label("First Name").fill("Test")
        page.get_by_label("Last Name").fill("Test")
        page.get_by_label("Address").fill("Test address")
        page.get_by_label("State/Province").fill("Test State")
        page.get_by_label("Postal Code").fill("123456")
        page.locator("#checkout-shipping-continue").click()
        page.wait_for_timeout(1000)  # Wait for a moment
        
        if page.locator("#confirmation-message").is_visible():  # Check if confirmation message appears
            mark_test_status("passed", "Order placed successfully", page)
        else:
            mark_test_status("failed", "Order not placed", page)
    except Exception as err:
        mark_test_status("failed", str(err), page)
    
    browser.close()  # Close the browser

# Function to mark test status and report to BrowserStack
def mark_test_status(status, reason, page):
    page.evaluate("_ => {}", "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\""+ status + "\", \"reason\": \"" + reason + "\"}}");

# Run the tests
with sync_playwright() as playwright:
    test_login(playwright)
    test_item_purchase(playwright)
