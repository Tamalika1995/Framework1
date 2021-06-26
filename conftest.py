import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as op
from selenium.webdriver.firefox.options import Options
chrome_option=op()
firefox_option=Options()
# chrome_option.add_argument('--headless')
from utils import Utils as util
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser n(me e.g.chrome OR firefox")

@pytest.fixture(scope='class')#by default the fixture run at function level
def test_setup(request):
    browser=request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_option,executable_path=ChromeDriverManager().install())
    elif browser=='firefox':
        driver=webdriver.Firefox(options=firefox_option,executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(util.URL)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    print("Done")