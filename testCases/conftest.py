import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'C:\\Users\\Hello\\PycharmProjects\\CelcomDigital\\testCases\\geckodriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == 'edge':
        driver = webdriver.Edge('C:\\Users\\Hello\\PycharmProjects\\CelcomDigital\\testCases\\msedgedriver.exe')
        driver.implicitly_wait(30)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption('--browser')
