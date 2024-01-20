import logging

import pytest
from selenium.common.exceptions import NoSuchElementException

from framework.login_page import LoginPage


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope="function")
def click_login_button(user_login_fixture):
    """
    Click "hello" log in button, if on the "hello" screen
    (if not than the first find_element call is successful and no action performed)
    """

    try:
        user_login_fixture.find_element(
            by_list=["id", "id", "classname", "classname", "classname"],
            by_values=[
                "com.ajaxsystems:id/authLogin",
                "com.ajaxsystems:id/compose_view",
                "android.view.View",
                "android.view.View",
                "android.widget.Button"
            ]
        )
    except NoSuchElementException:
        try:
            user_login_fixture.click_element(
                by_list=["classname", "classname", "classname", "classname"],
                by_values=[
                    "androidx.compose.ui.platform.ComposeView",
                    "android.view.View",
                    "android.view.View",
                    "android.widget.Button"
                ]
            )
        except NoSuchElementException:
            user_login_fixture.click_element(
                by_list=["id", "classname", "classname", "classname"],
                by_values=[
                    "com.ajaxsystems:id/compose_view",
                    "android.view.View",
                    "android.view.View",
                    "android.widget.Button"
                ]
            )
