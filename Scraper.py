from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from constants import (
    ConstantKeys as Constants,
    HtmlTags,
    Markers,
)


class Scraper:
    def __init__(self, rootDir: str):
        self.url = rootDir
        pass

    def run(
        self,
        pages: list[str],
        headers: list[str],
        filename: str,
        sectionTag: HtmlTags,
    ):

        content = ""
        content += self.makeContentListPage(pages)
        for page in pages:
            content += self.makePatchPage(page, headers, sectionTag)
        self.write(content, filename)

    def write(self, content: str, filename: str):
        with open(f"{filename}.md", "w+") as f:
            f.write(content)

    def makePatchPage(
        self,
        page: str,
        headers: list[str],
        sectionTag: HtmlTags,
    ):
        content = f"## {page}" + "\n"

        completeUrl = f"{self.url}/{page}"
        page = urlopen(completeUrl)
        soup = BeautifulSoup(page.read().decode(Constants.UTF_8), Constants.HTML_PARSER)
        soupHeadlines = soup.find_all(HtmlTags.SPAN, Constants.HEADLINE_ID)
        soupHeadlinesFiltered = [
            headline for headline in soupHeadlines if headline.getText() in headers
        ]

        for headline in soupHeadlinesFiltered:
            content += self.makeHeaderPage(headline, sectionTag) + "\n"
        return content

    def makeHeaderPage(
        self,
        headline: Tag,
        sectionTag: HtmlTags,
    ):
        content = ""
        content += f"### {headline.getText()}" + "\n"
        temp_headline = headline.findParent()
        temp_headline = temp_headline.findNextSibling()
        while temp_headline.name != sectionTag:
            content += self.makePage(temp_headline)
            temp_headline = temp_headline.findNextSibling()
        return content

    def makePage(
        self,
        headline: Tag,
    ) -> str:
        content: str = ""
        space: str = " "
        prefixMarker: str = self.getMarker(headline, Markers.HTML_TO_MARKDOWN_PREFIX)
        suffixMarker: str = self.getMarker(headline, Markers.HTML_TO_MARKDOWN_SUFFIX)
        intextMarker: str = self.getMarker(headline, Markers.HTML_TO_MARKDOWN_INTEXT)
        prefixMarker += space
        suffixMarker = space + suffixMarker
        content += (
            self.processRawText(
                headline.getText(), intextMarker, prefixMarker, suffixMarker
            )
            + "\n"
        )
        print(f"> {headline.name}: " + headline.getText())

        return content

    def makeContentListPage(self, headers: list[str]):
        contentPageTitle = "# Content  \n"
        content = " \n".join([self.linkify(header) for header in headers])
        return contentPageTitle + content + "\n"

    def linkify(self, header: str):
        return f"[{header}](#{header.lower().replace(' ', '-')})"

    def getMarker(self, tag: Tag, mapper: dict[HtmlTags, str]) -> str:
        if tag.name in mapper.keys():
            return mapper[tag.name]
        return ""

    def processRawText(
        self, rawText: str, intextMarker: str, prefixMarker: str, suffixMarker: str
    ) -> str:
        return "\n".join(
            [
                prefixMarker
                + intextMarker
                + line.replace("’", "'")
                + intextMarker
                + suffixMarker
                for line in rawText.strip().split("\n")
            ]
        )
