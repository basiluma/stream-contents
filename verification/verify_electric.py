from playwright.sync_api import sync_playwright
import os

def check_electric():
    asset = "vtuber_assets/11_electric_sparks/index.html"
    base_path = os.getcwd()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = f"file://{base_path}/{asset}"
        print(f"Checking {url}")

        try:
            page.goto(url)
            # Wait for animation to likely be visible (it's erratic, so maybe 0.5s is a good hit)
            page.wait_for_timeout(500)

            page.set_viewport_size({"width": 1920, "height": 1080})

            # Take multiple screenshots to catch the flash
            for i in range(3):
                screenshot_path = f"verification/electric_sparks_{i}.png"
                page.screenshot(path=screenshot_path)
                print(f"Saved screenshot to {screenshot_path}")
                page.wait_for_timeout(200)

        except Exception as e:
            print(f"Error checking {asset}: {e}")
        finally:
            page.close()
            browser.close()

if __name__ == "__main__":
    check_electric()
