from urllib.request import urlopen
from bs4 import BeautifulSoup
from constants import ConstantKeys as Constants, HtmlTags
from scraper import Scraper

if __name__ == "__main__":

    def main():
        print("Hello World")
        url = "https://valorant.fandom.com/wiki/Patch_Notes"
        scpr = Scraper(url)
        scpr.run(
            [
                "6.0",
                "6.01",
                "6.02",
                "6.03",
                "6.04",
                "6.05",
                "6.06",
                "6.07",
                "6.08",
                "6.10",
                "6.11",
                ##
                "7.0",
                "7.01",
                "7.02",
                "7.03",
                "7.04",
                "7.05",
                "7.06",
            ],
            ["Agent Updates", "Map Updates", "Competitive Updates"],
            filename="someFile",
            sectionTag=HtmlTags.H2,
        )

    main()
