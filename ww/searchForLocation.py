from selenium.webdriver.common.by import By

from ww.browserWaitForElement import browserWaitForElement
from ww.slowSendKeys import slowSendKeys


def searchForLocation(browser, location: str, timeout: float = 10):
    browser.get("https://www.wework.com/search")
    browserWaitForElement(browser, (By.ID, "search-input"))

    searchBox = browser.find_element(By.ID, "search-input")
    slowSendKeys(searchBox, location)
    browserWaitForElement(browser, (By.CLASS_NAME, "result-item"))
    firstResult = browser.find_element(By.ID, "search-results").find_element(
        By.CLASS_NAME, "result-item"
    )
    firstResult.click()
