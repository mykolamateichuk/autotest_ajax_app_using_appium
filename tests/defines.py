
CREDENTIALS = {
    "email": "qa.ajax.app.automation@gmail.com",
    "password": "qa_automation_password"
}


ELEMENTS = {
    "LOGIN_BUTTON": {
        "id": "",
        "xpath": "(//androidx.compose.ui.platform.ComposeView[@resource-id=\""
                 "com.ajaxsystems:id/compose_view\"])[1]/android.view.View/"
                 "android.view.View/android.widget.Button"
    },
    "EMAIL_FIELD": {
        "id": "com.ajaxsystems:id/authLoginEmail",
        "xpath": "//android.widget.EditText[@resource-id=\""
                 "com.ajaxsystems:id/authLoginEmail\"]"
    },
    "PASSWORD_FIELD": {
        "id": "com.ajaxsystems:id/authLoginPassword",
        "xpath": "//android.widget.EditText[@resource-id=\""
                 "com.ajaxsystems:id/authLoginPassword\"]"
    }
}
