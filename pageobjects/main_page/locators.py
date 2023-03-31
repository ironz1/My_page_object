from attrdict import AttrDict
from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Class where are stored all locators from welcome page
    """
    locators = AttrDict(dict(
        add_task=(
            By.XPATH, '//*[@class="icon_add"]'),
        task_title_field=(
            By.XPATH, '//*[@data-placeholder="Task name"]'),
        task_description_field=(
            By.XPATH, '//*[@data-placeholder="Description"]'),
        add_task_submit_button=(
            By.XPATH, '//*[@data-testid="task-editor-submit-button"]'),
        task_on_list=(
            By.XPATH, '//*[@class="task_content"][contains(text(),"New task")]')
    ))
