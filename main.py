import time

import fire
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import ww.settings as st
from ww.browserWaitForElement import browserWaitForElement
from ww.getBuildingLinks import getBuildingLinks
from ww.getWindowLinks import getWindowLinks
from ww.makeWeWorkBuildingUrl import makeWeWorkBuildingURL
from ww.searchForLocation import searchForLocation

# Main #################################################################################


def main(location: str):
    with webdriver.Firefox() as browser:
        searchForLocation(browser, location)

        try:
            browserWaitForElement(browser, (By.CLASS_NAME, "search-building-card"))
        except:
            errStr = f"No WeWork buildings found in {location}."
            raise ValueError(errStr)

        buildLinks1 = getBuildingLinks(
            BeautifulSoup(browser.page_source, "html.parser")
        )
        time.sleep(st.PAUSE())
        buildLinks = getBuildingLinks(BeautifulSoup(browser.page_source, "html.parser"))
        while len(buildLinks) > len(buildLinks1):
            buildLinks1 = buildLinks
            buildLinks = getBuildingLinks(
                BeautifulSoup(browser.page_source, "html.parser")
            )

        windows = []
        for bl in buildLinks:
            browser.get(makeWeWorkBuildingURL(bl[0:-1]))
            time.sleep(2 * st.PAUSE())
            newWins = getWindowLinks(BeautifulSoup(browser.page_source, "html.parser"))
            for win in newWins:
                print(win)
            windows += newWins

        with open(f"{location}.txt", "w") as f:
            for win in windows:
                f.write(win + "\n")


# Run ##################################################################################

if __name__ == "__main__":
    fire.Fire(main)
