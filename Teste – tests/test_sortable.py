from ui_tests.pages.sortable_page import SortablePage

def test_sortable(browser):
    page = SortablePage(browser)
    page.load()
    sorted_list = page.sort_list()
    assert len(sorted_list) > 0
