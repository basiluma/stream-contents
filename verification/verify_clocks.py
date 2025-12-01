from playwright.sync_api import sync_playwright

def verify_clocks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open the index gallery
        # Assuming the absolute path works for the file protocol
        import os
        pwd = os.getcwd()
        url = f"file://{pwd}/vtuber_clocks/index.html"

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for clocks to render
        page.wait_for_timeout(2000)

        # Take a screenshot
        screenshot_path = "verification/vtuber_clocks.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_clocks()
