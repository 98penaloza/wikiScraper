class ConstantKeys:
    UTF_8 = "utf-8"
    HTML_PARSER = "html.parser"
    HEADLINE_ID = {"class": "mw-headline"}


class HtmlTags:
    """
    Refer to https://www.w3schools.com/TAGS for full details
    """

    LI = "li"  ## list
    UL = "ul"  ## unordered list
    OL = "ol"  ## ordered list
    DL = "dl"  ## defines a description list
    DT = "dt"  ## defines a term/name in a description list
    DD = "dd"  ## used to describe a term/name in a description list

    H1 = "h1"  ## header 1
    H2 = "h2"  ## header 2
    H3 = "h3"  ## header 3
    H4 = "h4"  ## header 4
    H5 = "h5"  ## header 5
    H6 = "h6"  ## header 6
    P = "p"  ## defines a paragraph
    B = "b"  ## specifies bold text without any extra importance
    I = "i"  ## defines a part of text in an alternate voice or mood
    SPAN = "span"  ## element which is used to color a part of a text
    BR = "br"  ## inserts a single line break

    DIV = "div"  ## section in a document that is styled with CSS
    IMG = "img"  ## used to embed an image in an HTML page
    A = "a"  ## defines a hyperlink


class Markers:
    HTML_TO_MARKDOWN_PREFIX: dict[HtmlTags, str] = {
        HtmlTags.LI: "",
        HtmlTags.UL: "-",
        HtmlTags.OL: "1.",
        HtmlTags.DL: "",
        HtmlTags.DT: "",
        HtmlTags.DD: "",
        HtmlTags.H1: "",
        HtmlTags.H2: "###",
        HtmlTags.H3: "####",
        HtmlTags.H4: "#####",
        HtmlTags.H5: "######",
        HtmlTags.H6: "######",
    }
    HTML_TO_MARKDOWN_SUFFIX: dict[HtmlTags, str] = {
        HtmlTags.LI: "",
        HtmlTags.UL: "",
        HtmlTags.OL: "",
        HtmlTags.DL: "",
        HtmlTags.DT: "",
        HtmlTags.DD: "",
        HtmlTags.H1: "",
        HtmlTags.H2: "",
        HtmlTags.H3: "",
        HtmlTags.H4: "",
        HtmlTags.H5: "",
        HtmlTags.H6: "",
        HtmlTags.P: " ",
        HtmlTags.B: "",
        HtmlTags.I: "",
        HtmlTags.SPAN: "",
        HtmlTags.BR: "",
        HtmlTags.DIV: "",
        HtmlTags.IMG: "",
        HtmlTags.A: "",
    }
    HTML_TO_MARKDOWN_INTEXT: dict[HtmlTags, str] = {
        HtmlTags.LI: "",
        HtmlTags.UL: "",
        HtmlTags.OL: "",
        HtmlTags.DL: "**",
        HtmlTags.DT: "**",
        HtmlTags.DD: "",
        HtmlTags.H1: "",
        HtmlTags.H2: "",
        HtmlTags.H3: "",
        HtmlTags.H4: "",
        HtmlTags.H5: "",
        HtmlTags.H6: "",
        HtmlTags.P: " ",
        HtmlTags.B: "**",
        HtmlTags.I: "*",
        HtmlTags.SPAN: "",
        HtmlTags.BR: "",
        HtmlTags.DIV: "",
        HtmlTags.IMG: "",
        HtmlTags.A: "",
    }
