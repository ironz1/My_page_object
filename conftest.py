import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
import requests


@pytest.fixture()
def base_url():
    cfg_file = configparser.ConfigParser()
    cfg_file.read('pytest.ini')
    url = cfg_file.get('pytest', 'base_url')
    return url


@pytest.fixture()
def selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Logowanie webrdiver wyłączone
    service = Service(executable_path="selenium_drivers/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):
    # session.config._metadata.pop("JAVA_HOME")
    session.config._metadata.pop("Packages")
    session.config._metadata.pop("Plugins")
    session.config._metadata['Project Name'] = 'Frontend tests'


def pytest_html_report_title(report):
    report.title = f"Automation Test Report 2.0"


@pytest.fixture()
def logged_in_api():
    session = requests.Session()
    login_info = {'email': 'homkonektred@gmail.com',
                  'password': 'homeconnect1#'}
    landing_resp = session.post('https://todoist.com/API/v9.0/user/login', data=login_info)
    if landing_resp.status_code != 200:
        raise ValueError('Nie udalo się zalogować')
    return session


@pytest.fixture()
def app_url_api():
    return 'https://todoist.com/'
