from lxml.html import HtmlElement, fromstring, etree


class LightElement():

    _context: HtmlElement

    def __init__(self, html: str | HtmlElement):
        if isinstance(html, str):
            self._context = fromstring(html)
        else:
            self._context = html

    def element(self, xpath: str) -> HtmlElement | None:
        """
        Returns the first element match

        Args:
            xpath: xpath selector

        Returns:
            HtmlElement
        """
        return LightElement(self._context.xpath(f".{xpath}")[0]) if self._context.xpath(f".{xpath}") else None

    def elements(self, xpath: str) -> list[HtmlElement | None]:
        """
        Returns all matching elements

        Args:
            xpath: xpath selector

        Returns:
            list[HtmlElement]
        """
        return [LightElement(e) for e in self._context.xpath(f".{xpath}")]


    def contains_string(self, target: str) -> bool:
        """
        Recursive search of element and children for a single string

        Args:
            target: string

        Returns:
            bool
        """
        if target in (self._context.text or ''):
            return True
        for child in self._context.iterchildren():
            if self.contains_string(child, target):
                return True
        return False

    def contains_any_string(self, targets: list[str]) -> bool:
        """
        Recursive search of element and children for any string in list

        Args:
            targets: list of strings

        Returns:
            bool
        """
        if any([x in (self._context.text or '') for x in targets]):
            return True
        for child in self._context.iterchildren():
            if self.contains_any_string(child, targets):
                return True
        return False