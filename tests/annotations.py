import pytest
import sys
from playwright.sync_api import expect

@pytest.mark.skip(reason="Feature is under development")
def test_homepage_loads_testCase(page):
    page.goto("https://qaautomationlabs.com/")
    assert page.title() == "Home - QA Automation Labs"
      
@pytest.mark.xfail(reason="Known bug in checkout flow")
def test_annotation_fail_testCase(page):
    page.goto("https://qaautomationlabs.com/")
    assert page.title() == "Home - QA Automation Labs1"
    
@pytest.mark.skipif(sys.platform == "darwin", reason="does not run on mac")
def test_annotation_skipIf_testCase(page):
    # Use the pytest-playwright `page` fixture — no sync_playwright() here
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
    # assert title
    expect(page, "The page title did not match the expected value.").to_have_title("Account Login")
    # check email field attribute
    expect(page.locator("#input-email")).to_have_attribute("type", "text")
    
@pytest.mark.skip_browser("firefox", reason="Firefox doesn’t support this feature")
def test_annotation_skipBrowser_testCase(page):
    # Use the pytest-playwright `page` fixture — no sync_playwright() here
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
    # assert title
    expect(page, "The page title did not match the expected value.").to_have_title("Account Login")
    expect(page.locator("#input-email")).to_have_attribute("type", "text")

@pytest.mark.only_browser("firefox", reason="Run only in Firefox")
def test_annotation_onlyBrowser_testCase(page):
    # Use the pytest-playwright `page` fixture — no sync_playwright() here
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
    # assert title
    expect(page, "The page title did not match the expected value.").to_have_title("Account Login")
    # check email field attribute
    expect(page.locator("#input-email")).to_have_attribute("type", "text")