from lxml.html import HtmlElement

class Scraper():

    def element(self, html: HtmlElement, xpath: str) -> HtmlElement | None:
        """
        Returns the first element match

        Args:
            html: element to search
            xpath: xpath selector

        Returns:
            HtmlElement
        """
        return html.xpath(f".{xpath}")[0] if html.xpath(f".{xpath}") else None

    def elements(self, html: HtmlElement, xpath: str) -> list[HtmlElement | None]:
        """
        Returns all matching elements

        Args:
            html: element to search
            xpath: xpath selector

        Returns:
            list[HtmlElement]
        """
        return [*html.xpath(f".{xpath}")]

    def contains_string(self, element: HtmlElement, target: str) -> bool:
        """
        Recursive search of element and children for a single string

        Args:
            element: element to search
            target: string

        Returns:
            bool
        """
        if target in (element.text or ''):
            return True
        for child in element.iterchildren():
            if self.contains_string(child, target):
                return True
        return False

    def contains_any_string(self, element: HtmlElement, targets: list[str]) -> bool:
        """
        Recursive search of element and children for any string in list

        Args:
            element: element to search
            targets: list of strings

        Returns:
            bool
        """
        if any([x in (element.text or '') for x in targets]):
            return True
        for child in element.iterchildren():
            if self.contains_any_string(child, targets):
                return True
        return False

scraper = Scraper()