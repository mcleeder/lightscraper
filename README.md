# lightscraper
Lightweight web scraping library.


# Example Use

```
import requests
from lightelement import LightElement

response = requests.get("https://www.google.com")

html = LightElement(response.text)

first_div = html.element("//div")
first_nested_div = first_div.element("//div")

all_divs = html.elements("//div")

string_in_all_divs = any([e.contains_text("the_string") for e in all_divs])

```