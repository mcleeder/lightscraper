from lxml import etree, html


class LightElement(etree.ElementBase):

    @classmethod
    def from_html(cls, html_string: str) -> 'LightElement':
        """
        Factory method to create LightElement instance from HTML string

        Args:
            html_string: HTML string to parse

        Returns:
            LightElement
        """
        html_tree = html.fromstring(html_string)
        return cls(html_tree)

    def element(self, xpath: str) -> 'LightElement':
        """
        Returns the first element match

        Args:
            xpath: xpath selector

        Returns:
            LightElement
        """
        found = self.xpath(f".{xpath}")
        return LightElement(found[0]) if found else None

    def elements(self, xpath: str) -> list['LightElement' | None]:
        """
        Returns all matching elements

        Args:
            xpath: xpath selector

        Returns:
            list[LightElement]
        """
        found = self.xpath(f".{xpath}")
        return [LightElement(e) for e in found]


    def contains_string(self, target: str) -> bool:
        """
        Recursive search of element and children for a single string

        Args:
            target: string

        Returns:
            bool
        """
        if target in (self.text or ''):
            return True
        for child in self.iterchildren():
            if LightElement(child).contains_string(target):
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
        if any([x in (self.text or '') for x in targets]):
            return True
        for child in self.iterchildren():
            if LightElement(child).contains_any_string(targets):
                return True
        return False