from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/")
    page.goto("http://127.0.0.1:8000/polls")
    page.goto("http://127.0.0.1:8000/nocodb-data")
    page.goto("http://127.0.0.1:8000/admin/login/?next=/admin/")
    page.get_by_role("textbox", name="Username:").fill("admin")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("127823")
    page.get_by_role("textbox", name="Password:").press("Enter")
    page.get_by_role("link", name="Questions").click()
    page.get_by_role("link", name="Add question").click()
    page.get_by_role("textbox", name="Question text:").fill("123")
    page.get_by_text("Date published: Date: Today").click()
    page.locator("#id_pub_date_0").click()
    page.get_by_role("link", name="Today").click()
    page.locator("#id_pub_date_1").click()
    page.get_by_role("link", name="Now").click()
    page.get_by_role("button", name="Save", exact=True).click()
    page.get_by_role("button", name="Log out").click()

    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
