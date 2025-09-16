from playwright.sync_api import sync_playwright, expect

def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Fill email and password
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        
        # Locate the login button
        login_button = page.locator('button[id="loginBtn"]')
        
        # Click the login button
        login_button.click()
        page.get_by_role("link", name="Shop Now", exact=True).first.click()
        # Assert specific count of products
    
        expect(page.locator(".product-item")).to_have_count(20)
        browser.close()