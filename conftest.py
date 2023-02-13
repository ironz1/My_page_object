import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser


@pytest.fixture()
def base_url():
    cfg_file = configparser.ConfigParser()
    cfg_file.read('pytest.ini')
    url = cfg_file.get('pytest', 'base_url')
    return url


# @pytest.fixture()
def selenium():
    service = Service(executable_path="selenium_drivers/chromedriver")
    driver = webdriver.Chrome(service=service)
    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):
    session.config._metadata.pop("JAVA_HOME")
    session.config._metadata.pop("Packages")
    session.config._metadata.pop("Plugins")
    session.config._metadata['Project Name'] = 'Frontend tests'


def pytest_html_report_title(report):
    report.title = f"Automation Test Report 2.0"

