from playwright.sync_api import sync_playwright, expect

def test_ContextAsseration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/shop.php", wait_until="load")
    
    # Assert element has specific inner text
        expect(page.get_by_role("button", name="Login")).to_have_text("Login")
        browser.close()