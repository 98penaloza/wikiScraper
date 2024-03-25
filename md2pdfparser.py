from markdown_pdf import Section, MarkdownPdf


class MD2PDFParser:
    def __init__(self) -> None:
        self.pdf = MarkdownPdf(toc_level=2)

    def parse(self, docName: str, content: str) -> None:
        self.pdf.add_section(Section(content))
        self.pdf.save(f"{docName}.pdf")
        pass
