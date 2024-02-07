from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from constants import ConstantKeys as Constants, HtmlTags


class Scraper:
    def __init__(self, rootDir: str):
        self.url = rootDir
        pass

    def run(
        self,
        pages: [str],
        headers: [str],
        filename: str,
        sectionTag: HtmlTags,
        inTextTagsSet: {HtmlTags},
        nextTextTagsSet: {HtmlTags},
    ):
        # contentPage = self.makeContentPage();
        content = ""
        content += self.makeContentListPage(pages)
        for page in pages:
            content += self.makePatchPage(
                page, headers, sectionTag, inTextTagsSet, nextTextTagsSet
            )
        self.write(content, filename)

    def write(self, content: str, filename: str):
        print(content)

    def makePatchPage(
        self,
        page: str,
        headers: [str],
        sectionTag: HtmlTags,
        inTextTagsSet: {HtmlTags},
        nextTextTagsSet: {HtmlTags},
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
            content += (
                self.makeHeaderPage(
                    headline, sectionTag, inTextTagsSet, nextTextTagsSet
                )
                + "\n"
            )
        return content

    def makeHeaderPage(
        self,
        headline: Tag,
        sectionTag: HtmlTags,
        inTextTagsSet: {HtmlTags},
        nextTextTagsSet: {HtmlTags},
    ):
        content = ""
        content += f"### {headline.getText()}" + "\n"
        parent = temp_headline = headline.findParent()
        temp_headline = temp_headline.findNextSibling()
        while temp_headline.name != sectionTag and temp_headline:
            content += self.makeRecursivePage(
                temp_headline, 2, sectionTag, inTextTagsSet, nextTextTagsSet
            )
        return content

    def makeRecursivePage(
        self,
        headline: Tag,
        depth: int,
        sectionTag: HtmlTags,
        inTextTagsSet: {HtmlTags},
        nextTextTagsSet: {HtmlTags},
    ) -> str:
        content: str = ""
        separator: str = " " * depth

        children = headline.findChildren()
        if not len(children):
            content += separator + headline.getText() + "\n"
            return content

        else:
            content += separator + headline.getText() + "\n"
            for child in children:
                if child.name in inTextTagsSet:
                    content += child.getText()
                elif child.name in nextTextTagsSet:
                    childContent = self.makeRecursivePage(
                        child, depth + 2, inTextTagsSet, nextTextTagsSet
                    )
                    content += childContent
            return content

    def makeContentListPage(self, headers: [str]):
        contentPageTitle = "# Content  \n"
        content = " \n".join([self.linkify(header) for header in headers])
        return contentPageTitle + content + "\n"

    def linkify(self, header: str):
        return f"[{header}](#{header.lower().replace(' ', '-')})"
