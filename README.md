# Light Scraper

`Light Scraper` is a Python library that provides a convenient wrapper around the `lxml.html.HtmlElement` class, making it easier to work with HTML elements and perform common operations such as XPath queries and string searches.

## Installation

To install `lxml`, you can use pip:

```sh
pip install lxml
```

## Usage

### Creating a `LightElement`

You can create a `LightElement` from an HTML string or an `lxml.etree._Element` instance:

```python
html_str = "<div><p>Hello, World!</p></div>"
element = LightElement(html_str)
```

### Methods

#### `element(xpath: str) -> LightElement`

Returns the first element that matches the given XPath expression.

```python
first_p = element.element("//p")
print(first_p)  # Output: <p>Hello, World!</p>
```

#### `elements(xpath: str) -> list[LightElement]`

Returns all elements that match the given XPath expression.

```python
all_divs = element.elements("//div")
for div in all_divs:
    print(div)
```

#### `contains_string(target: str) -> bool`

Recursively searches the element and its children for a specific string.

```python
has_hello = element.contains_string("Hello")
print(has_hello)  # Output: True
```

#### `contains_any_string(targets: list[str]) -> bool`

Recursively searches the element and its children for any string in the given list.

```python
has_any = element.contains_any_string(["Hello", "World"])
print(has_any)  # Output: True
```

## Example

Here is a complete example demonstrating the use of `LightElement`:

```python
from your_module import LightElement

html = """
<div>
    <p>Hello, World!</p>
    <p>Another paragraph.</p>
</div>
"""

element = LightElement(html)

# Find the first paragraph
first_p = element.element("//p")
print(first_p)  # <p>Hello, World!</p>

# Find all paragraphs
all_ps = element.elements("//p")
for p in all_ps:
    print(p)

# Check if the document contains a specific string
contains_hello = element.contains_string("Hello")
print(contains_hello)  # True

# Check if the document contains any of the specified strings
contains_any = element.contains_any_string(["Another", "Missing"])
print(contains_any)  # True
```
