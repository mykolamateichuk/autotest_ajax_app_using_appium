import time
import datetime
import logging

import pytest

# Set up logger
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("tests/logs/test.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s : %(message)s")

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.info(f"[{datetime.datetime.now()}] TESTING STARTED")


invalid_credentials = [
    ("that_is_not_an_email", "somepassword", "Invalid email format"),
    ("almost_an@email", "passwordtest", "Invalid email format"),
    ("missed_the_dot@emailcom", "testpassword", "Invalid email format"),
    ("test@email.com", "testpassword", "Wrong login or password"),
    ("wrong@email.com", "wrongpassword", "Wrong login or password"),
    ("notevenclose@gmail.com", "strong_password", "Wrong login or password")
]


@pytest.mark.parametrize("email,password,result_message", invalid_credentials)
def test_user_login_invalid_credentials(user_login_fixture,
                                        click_login_button,
                                        email: str,
                                        password: str,
                                        result_message: str):
    """
    (1) Enter invalid credentials
    (2) Click "auth" login button
    (3) Wait for the message to appear
    (4) Read message and compare with expected result
    (5) Remove credentials and start over
    """

    logger.info(f"Test invalid credentials [\"{email}\", \"{password}\"]:"
                f" expected result \"{result_message}\"")
    start_time = time.perf_counter()

    user_login_fixture.enter_credentials(
        credentials={
            "email": email,
            "password": password
        }
    )

    user_login_fixture.click_element(
        by_list=["id", "id", "classname", "classname", "classname"],
        by_values=[
            "com.ajaxsystems:id/authLogin",
            "com.ajaxsystems:id/compose_view",
            "android.view.View",
            "android.view.View",
            "android.widget.Button"
        ]
    )

    time.sleep(1.5)

    text_message = user_login_fixture.find_element(
        by_list=["id", "classname", "classname"],
        by_values=[
            "android:id/content",
            "android.widget.LinearLayout",
            "android.widget.TextView"
        ]
    )

    if text_message.get_attribute("text") == result_message:
        exec_time = time.perf_counter() - start_time
        logger.info(f"TEST PASSED IN {exec_time} SEC")
    else:
        logger.error(f"TEST FAILED [got \"{text_message.get_attribute('text')}"
                     f"\" instead of \"{result_message}\"]")

    assert text_message.get_attribute("text") == result_message

    user_login_fixture.remove_credentials()


def test_user_login_valid_credentials(user_login_fixture):
    """
    (1) Enter valid credentials
    (2) Click "auth" login button
    (3) Wait for the next screen to load
    (4) Try to find "Add Hub" button, if succeeded -> log in was successful.
    """

    logger.info(f"Test valid credentials:"
                f" expected result \"Add Hub\" button found")
    start_time = time.perf_counter()

    user_login_fixture.enter_credentials()

    user_login_fixture.click_element(
        by_list=["id", "id", "classname", "classname", "classname"],
        by_values=[
            "com.ajaxsystems:id/authLogin",
            "com.ajaxsystems:id/compose_view",
            "android.view.View",
            "android.view.View",
            "android.widget.Button"
        ]
    )

    time.sleep(7)

    element = user_login_fixture.find_element(
        by_list=["id", "id", "classname", "id"],
        by_values=[
            "android:id/content",
            "com.ajaxsystems:id/drawer_layout",
            "android.view.ViewGroup",
            "com.ajaxsystems:id/hubAdd"
        ]
    )

    if element:
        exec_time = time.perf_counter() - start_time
        logger.info(f"TEST PASSED IN {exec_time} SEC")
    else:
        logger.error(f"TEST FAILED")

    assert element


def test_sidebar_elements(user_login_fixture):
    logger.info(f"Test sidebar elements: expected result \"Settings\" button,"
                f" \"Help\" button and \"Logs\" button present")
    start_time = time.perf_counter()

    user_login_fixture.click_element(
        by_list=["classname", "classname", "classname"],
        by_values=[
            "androidx.drawerlayout.widget.DrawerLayout",
            "android.widget.FrameLayout",
            "android.widget.ImageView",
        ]
    )

    time.sleep(0.5)

    assert user_login_fixture.find_element(
        by_list=["classname", "classname", "classname", "id"],
        by_values=[
            "androidx.drawerlayout.widget.DrawerLayout",
            "androidx.compose.ui.platform.ComposeView",
            "android.widget.ScrollView",
            "com.ajaxsystems:id/settings"
        ]
    )

    assert user_login_fixture.find_element(
        by_list=["classname", "classname", "classname", "id"],
        by_values=[
            "androidx.drawerlayout.widget.DrawerLayout",
            "androidx.compose.ui.platform.ComposeView",
            "android.widget.ScrollView",
            "com.ajaxsystems:id/help"
        ]
    )

    assert user_login_fixture.find_element(
        by_list=["classname", "classname", "classname", "id"],
        by_values=[
            "androidx.drawerlayout.widget.DrawerLayout",
            "androidx.compose.ui.platform.ComposeView",
            "android.widget.ScrollView",
            "com.ajaxsystems:id/logs"
        ]
    )

    assert user_login_fixture.find_element(
        by_list=["classname", "classname", "classname", "id"],
        by_values=[
            "androidx.drawerlayout.widget.DrawerLayout",
            "androidx.compose.ui.platform.ComposeView",
            "android.widget.ScrollView",
            "com.ajaxsystems:id/addHub"
        ]
    )

    exec_time = time.perf_counter() - start_time
    logger.info(f"TEST PASSED IN {exec_time} SEC")
