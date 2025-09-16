from playwright.sync_api import sync_playwright, expect

def test_AddProduct():
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
        
        # Verify initial cart is empty
        expect(page.locator("#cartCount")).to_have_text("0")

        # Click Shop Now under Men Fashion
        page.get_by_role("link", name="Shop Now", exact=True).first.click()

        #  Add Black T-Shirt to cart
        page.get_by_role("link", name="Black T-Shirt").click()
        page.get_by_role("button", name="Add to Cart").click()
        
        # Verify cart count updated
        expect(page.locator("#cartCount")).to_have_text("1")

        # Click Cart icon 
        page.locator("#cartdesk").click()

        # Verify Black T-Shirt is in cart summary
        assert page.locator("#cartTable").inner_text().count("Black T-Shirt") > 0 
        cart_table = page.locator("#cartTable")

        # Wait until cart table is visible
        expect(cart_table).to_be_visible(timeout=30000)

        # Assertion: verify table text includes "Black T-Shirt"
        expect(cart_table).to_contain_text("Black T-Shirt")
        page.wait_for_timeout(5000)
    
        browser.close()