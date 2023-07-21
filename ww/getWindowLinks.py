from typing import List

from bs4 import BeautifulSoup


def getWindowLinks(buildingPage: BeautifulSoup) -> List[str]:
    roomDescriptions = buildingPage.find_all(
        "div", class_="selection-card-product-description"
    )

    out = []
    for roomDesc in roomDescriptions:
        if len(roomDesc.contents) > 0:
            if roomDesc.contents[0].lower().find("window") > -1:
                out.append(roomDesc.find_parent("a")["href"])

    return out
