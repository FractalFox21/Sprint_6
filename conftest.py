import pytest
from selenium import  webdriver

@pytest.fixture(params=['firefox','chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome()
    yield browser
    browser.quit()