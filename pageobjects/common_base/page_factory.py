"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

from pageobjects.login_page.login_page_actions import LoginPage
from pageobjects.main_page.main_page_actions import MainPage


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name, base_url, selenium):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["login_page"]:
            test_obj = LoginPage(base_url, selenium)
        elif page_name in ["main_page"]:
            test_obj = MainPage(base_url, selenium)
        return test_obj

    get_page_object = staticmethod(get_page_object)