from playwright.sync_api import sync_playwright, expect

def test_ContextAsseration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login") 
        expect(page, "The page title did not match the expected value.").to_have_title("Account Login")
        expect(page.locator("#input-email")).to_have_attribute("type", "text") 
        browser.close()