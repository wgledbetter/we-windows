from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def browserWaitForElement(browser, elementIdentifier, timeout: float = 10):
    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(elementIdentifier)
    )
