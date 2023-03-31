from pageobjects.common_base.base_page import BasePage
from pageobjects.main_page.locators import MainPageLocators


class MainPage(BasePage):

    def click_add_task(self):
        self.click(MainPageLocators.locators.add_task)

    def enter_task_name(self):
        self.enter_text(MainPageLocators.locators.task_title_field, 'New task1')

    def enter_task_description(self):
        self.enter_text(MainPageLocators.locators.task_description_field, 'New description 1')

    def click_add_task_submit_button(self):
        self.click(MainPageLocators.locators.add_task_submit_button)

    def is_task_on_list(self):
        return self.is_element_displayed(MainPageLocators.locators.task_on_list)

