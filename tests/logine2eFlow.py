from playwright.sync_api import sync_playwright, expect

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
      
        # Verify login form elements are present
        expect(page.locator("#input-email")).to_be_visible()
        expect(page.locator("#input-password")).to_be_visible()
        expect(page.get_by_role("button", name="Login")).to_be_enabled()
        
        # Fill login credentials
        page.fill("#input-email", "johnpeter123@yopmail.com")
        page.fill("#input-password", "Test@1234")
        
        # Verify input values
        expect(page.locator("#input-email")).to_have_value("johnpeter123@yopmail.com")
        expect(page.locator("#input-password")).to_have_value("Test@1234")
        
        # Submit login
        page.click("input[value='Login']")
        expect(page.locator("body")).not_to_contain_text("Warning: No match for E-Mail Address")
        
        # Verify successful login by checking account page elements
        expect(page).to_have_url("https://naveenautomationlabs.com/opencart/index.php?route=account/account")
        expect(page.locator("#content")).to_contain_text("My Account")
        page.wait_for_timeout(5000)  # Wait for 5 seconds to observe the result
        
        browser.close()