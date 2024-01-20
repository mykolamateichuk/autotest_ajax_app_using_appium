from .page import Page
from tests.defines import CREDENTIALS, ELEMENTS


class LoginPage(Page):
    def enter_credentials(self, credentials: dict = CREDENTIALS):
        self.set_value_to_element(
            by_list=["id"],
            by_values=[ELEMENTS["EMAIL_FIELD"]["id"]],
            value=credentials["email"]
        )
        self.set_value_to_element(
            by_list=["id"],
            by_values=[ELEMENTS["PASSWORD_FIELD"]["id"]],
            value=credentials["password"]
        )

    def remove_credentials(self):
        self.find_element(
            by_list=["id"],
            by_values=[ELEMENTS["EMAIL_FIELD"]["id"]],
        ).clear()
        self.find_element(
            by_list=["id"],
            by_values=[ELEMENTS["PASSWORD_FIELD"]["id"]],
        ).clear()

    def click_login_button(self):
        self.click_element(
            by_list=["id", "classname", "classname", "classname"],
            by_values=[
                "com.ajaxsystems:id/compose_view",
                "android.view.View",
                "android.view.View",
                "android.widget.Button"
            ]
        )

