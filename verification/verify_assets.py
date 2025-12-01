from playwright.sync_api import sync_playwright
import os

def check_assets():
    assets = [
        "vtuber_assets/01_floating_bubbles/index.html",
        "vtuber_assets/02_neon_border/index.html",
        "vtuber_assets/05_glitch_text/index.html",
        "vtuber_assets/06_falling_sakura/index.html",
        "vtuber_assets/09_bouncing_ball/index.html"
    ]

    base_path = os.getcwd()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for asset in assets:
            page = browser.new_page()
            url = f"file://{base_path}/{asset}"
            print(f"Checking {url}")
            try:
                page.goto(url)
                # Wait a bit for animation
                page.wait_for_timeout(2000)

                screenshot_path = f"verification/{os.path.basename(os.path.dirname(asset))}.png"
                page.screenshot(path=screenshot_path)
                print(f"Saved screenshot to {screenshot_path}")

            except Exception as e:
                print(f"Error checking {asset}: {e}")
            finally:
                page.close()

        browser.close()

if __name__ == "__main__":
    check_assets()
