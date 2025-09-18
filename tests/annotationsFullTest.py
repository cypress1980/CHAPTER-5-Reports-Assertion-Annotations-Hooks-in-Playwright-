import pytest
from playwright.sync_api import sync_playwright, expect

# Base URL and credentials
BASE_URL = "https://shop.qaautomationlabs.com/index.php"
EMAIL = "demo@demo.com"
PASSWORD = "demo"

# Test 1: Run only this test for debugging
@pytest.mark.only
def test_login_button_enabled(page):
    page.goto(BASE_URL)
    #page.click("text=Log in")
    page.fill("input[type='email']", EMAIL)
    page.fill("input[type='password']", PASSWORD)
    page.click('#loginBtn')
    
# Test 2: Skip test for Firefox due to potential browser-specific issue
@pytest.mark.skip_browser("firefox", reason="Firefox has issues with modal rendering")
def test_login_modal_display(page):
    page.goto(BASE_URL)
    #page.click("text=Log in")
    #expect(page.locator("div#modal-login")).to_be_visible()
    page.fill("input[type='email']", EMAIL)
    page.fill("input[type='password']", PASSWORD)
    page.click('#loginBtn')
    #expect(page.locator("text=Welcome")).to_be_visible()

# Test 3: Mark as expected to fail due to a hypothetical bug
@pytest.mark.xfail(reason="Known issue with incorrect error message display")
def test_invalid_login(page):
    page.goto(BASE_URL)
    #page.click("text=Log in")
    page.fill("input[type='email']", "wrong@demo.com")
    page.fill("input[type='password']", "wrongpassword")
    page.click("button[name='login']")
    #expect(page.locator("text=Invalid email or password")).to_be_visible()
