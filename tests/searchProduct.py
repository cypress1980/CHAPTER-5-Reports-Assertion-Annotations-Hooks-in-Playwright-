from playwright.sync_api import sync_playwright, expect

def test_ContextAsseration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
        page.get_by_placeholder("Search").fill("MacBook")
        macbook_product = page.locator(".product-layout").filter(has_text="MacBook")
        expect(macbook_product).not_to_be_empty()
        page.locator(".input-group-btn").click()
        expect(page.locator(".product-layout")).to_have_count(3)  # Check number of results
        expect(page.locator(".product-layout")).to_have_count(3)  # Check number of results
        expect(page.get_by_text("MacBook").first).to_be_visible()  # Check product name
        browser.close()