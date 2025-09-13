from playwright.sync_api import sync_playwright, expect

def test_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Fill email and password
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        
        # Locate the login button
        login_button = page.locator('button[id="loginBtn"]')
        
        # Assert button is visible and enabled
        expect(login_button).to_be_visible()
        expect(login_button).to_be_enabled()
        
        # Click the login button
        login_button.click()
        
        # Additional steps or assertions can follow here
        
        browser.close()