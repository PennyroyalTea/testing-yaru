from .pages.main import YaMainPage as MainPage


def test_search_button_text(browser):
    main_page = MainPage(browser)
    main_page.load()

    assert main_page.get_button_text() == 'Найти'


def test_enter_email_text(browser):
    main_page = MainPage(browser)
    main_page.load()

    assert main_page.get_email_link_text() == 'Войти\xa0в\xa0почту'


def test_press_main_yandex_link(browser):
    main_page = MainPage(browser)
    main_page.load()
    url_after_click = main_page.press_yandex_button()
    assert url_after_click == 'https://yandex.ru/'

def test_press_mail_link(browser):
    main_page = MainPage(browser)
    main_page.load()
    url_after_click = main_page.press_mail_link()
    assert url_after_click == 'https://mail.yandex.ru/'


def test_empty_search(browser):
    main_page = MainPage(browser)
    main_page.load()
    empty_search_res = main_page.do_empty_search()
    assert empty_search_res == 'Задан пустой поисковый запрос'