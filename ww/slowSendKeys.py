import time

from selenium.webdriver.remote.webelement import WebElement


def slowSendKeys(element: WebElement, string: str, pause: float = 0.15):
    for char in string:
        element.send_keys(char)
        time.sleep(pause)
