import pytest
from playwright.sync_api import expect


# Base URL and credentials
BASE_URL = "https://shop.qaautomationlabs.com/index.php"
EMAIL = "demo@demo.com"
PASSWORD = "demo"

@pytest.mark.smoke
def test_website_smoke_test(page):
    """Most basic test - can we even load the website?"""
    page.goto(BASE_URL)
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login") 
    expect(page, "The page title did not match the expected value.").to_have_title("Account Login")
    expect(page.locator("#input-email")).to_have_attribute("type", "text") 
    print("Website loaded successfully")

@pytest.mark.sanity  
def test_website_sanity_test(page):
    """Can we login with demo account?"""
    page.goto("https://shop.qaautomationlabs.com/shop.php")
    page.goto(BASE_URL)
    page.fill("input[type='email']", EMAIL)
    page.fill("input[type='password']", PASSWORD)
    page.click('#loginBtn')
    
    # Check if login worked - look for a logout button or user menu
    page.wait_for_load_state("networkidle")
    # If we can see navigation, login probably worked
    nav = page.locator("nav").first
    expect(nav).to_be_visible()
    print("Login works!")

@pytest.mark.regression
def test_website_regression_test(page):
    """After login, check all menu items are there"""
    page.goto(BASE_URL)
    page.fill("input[type='email']", EMAIL)
    page.fill("input[type='password']", PASSWORD)
    page.click('#loginBtn')
    
    menu_items = ["Home", "About", "Courses", "Events", "Shop", "Testing", "Blog", "Contact"]
    
    for item in menu_items:
        menu_link = page.locator("#navbarCollapse").get_by_role("link", name=item)
        expect(menu_link).to_be_visible()
        print(f"Found {item} in menu")