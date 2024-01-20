
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

str_to_appiumby = {
    "id": AppiumBy.ID,
    "xpath": AppiumBy.XPATH,
    "classname": AppiumBy.CLASS_NAME
}


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_list: list[str], by_values: list[str]):
        if len(by_list) != len(by_values):
            raise ValueError("by_list and by_values should have equal amount of elements!")

        element = self.driver
        for i in range(len(by_list)):
            element = element.find_element(str_to_appiumby[by_list[i]], by_values[i])

        return element

    def click_element(self, by_list: list[str], by_values: list[str]):
        (self.find_element(by_list=by_list, by_values=by_values).click())

    def set_value_to_element(self, by_list: list[str], by_values: list[str], value):
        (self.find_element(by_list=by_list, by_values=by_values).send_keys(value))
