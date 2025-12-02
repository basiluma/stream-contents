from playwright.sync_api import sync_playwright, Page, expect
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the HTML file
    cwd = os.getcwd()
    file_path = f"file://{cwd}/vtuber_assets/12_nordic_notification/index.html"

    print(f"Navigating to: {file_path}")
    page.goto(file_path)

    # Wait for the element to be visible (animation start)
    # The animation puts opacity to 0 at start, so we might need to wait a moment or wait for a state.
    # However, since it's a CSS keyframe animation running on load, we just need to catch it in the middle.

    # We'll wait 0.5 seconds to catch the "bounced in" state before it fades out (which happens at 6s)
    page.wait_for_timeout(600)

    # Take a screenshot
    screenshot_path = "/home/jules/verification/verification.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
