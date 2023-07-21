from typing import List

from bs4 import BeautifulSoup


def getBuildingLinks(searchPage: BeautifulSoup) -> List[str]:
    buildingResults = searchPage.find_all("div", class_="search-building-card")
    return [bld.find("a")["href"] for bld in buildingResults]
