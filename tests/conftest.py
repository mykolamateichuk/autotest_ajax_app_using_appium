import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope="session")
def driver():
    options = (UiAutomator2Options()
               .load_capabilities(android_get_desired_capabilities()))
    driver = webdriver.Remote(
        "http://127.0.0.1:4723", options=options
    )
    yield driver
    driver.quit()
