from ui_tests.pages.browser_windows_page import BrowserWindowsPage

def test_browser_windows(browser):
    page = BrowserWindowsPage(browser)
    page.load()
    text = page.open_new_window()
    assert text == "This is a sample page"
    browser.close()
