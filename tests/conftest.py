import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/arsentiyabramov/Desktop/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://www.aloecare.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            browser_fixture = next(iter(item.funcargs.values()))
            driver = browser_fixture
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(driver, file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

    return report


def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)
