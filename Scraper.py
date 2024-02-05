from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from constants import ConstantKeys as Constants, HtmlTags


class Scraper:
    def __init__(self, rootDir: str):
        self.root = rootDir
        pass

    def run(self, pages: [str], headers: [str], filename: str):
        # contentPage = self.makeContentPage();
        content = ""
        content += self.makeContentListPage(pages)
        for page in pages:
            content += self.makePatchPage(page, headers)
        self.write(content, filename)

    def write(self, content: str, filename: str):
        pass

    def makePatchPage(self, page: str, headers: [str]):
        content = f"## {page}" + "\n"

        completeUrl = self.url + page
        page = urlopen(completeUrl)
        soup = BeautifulSoup(page.read().decode(Constants.UTF_8), Constants.HTML_PARSER)
        soupHeadlines = soup.find_all("span", Constants.HEADLINE_ID)
        for header in headers:
            for headline in soupHeadlines:
                if self.isHeaderHeadlineKey(header, headline):
                    content += self.makeHeaderPage(header, headline) + "\n"

    def makeHeaderPage(self, header: str, headline: Tag):
        content += f"### {header}" + "\n"
        parent = temp_headline = headline.findParent()
        temp_headline = temp_headline.findNextSibling()
        while temp_headline.name != parent.name and temp_headline:
            if temp_headline.name == HtmlTags.H3:
                pass

    def makeContentListPage(self, headers: [str]):
        contentPageTitle = "# Content  \n"
        content = [self.linkify(header) for header in headers].join("  \n")
        return contentPageTitle + content

    def linkify(self, header: str):
        return f"[{header}](#{header.lower().replace(' ', '-')})"

    def isHeaderHeadlineKey(header: str, headlineId: str):
        return header.lower().replace(" ", "_") == headlineId.lower()


if __name__ == "__main__":

    def main():
        print("Hello World")
        url = "https://valorant.fandom.com/wiki/Patch_Notes/6.0"
        page = urlopen(url)
        # print(page)
        # print(page.read().decode(Constants.UTF_8))
        print(
            BeautifulSoup(page.read().decode(Constants.UTF_8), Constants.HTML_PARSER)
            .find_all("span", Constants.HEADLINE_ID)[0]
            .findParent()
            .findChildren()
        )

    main()
