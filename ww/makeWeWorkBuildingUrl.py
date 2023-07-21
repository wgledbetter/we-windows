from ww.settings import WEWORK_URL_BASE


def makeWeWorkBuildingURL(href: str) -> str:
    return WEWORK_URL_BASE() + href + "/reserve?capacity=1"
