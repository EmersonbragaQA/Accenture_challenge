from ui_tests.pages.progress_bar_page import ProgressBarPage

def test_progress_bar(browser):
    page = ProgressBarPage(browser)
    page.load()

    value = page.start_and_stop_at(25)
    assert value <= 25

    page.run_to_100_and_reset()
