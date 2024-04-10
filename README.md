# lightscraper
Lightweight web scraping library for use in my own projects

```python
import requests
from lxml.html import fromstring
from scraper import scraper as ls

response = requests.get("http://www.google.com")

html_tree = fromstring(response.text)

search_btn = ls.element(html_tree, "//input[starts-with(@name, 'btn')]")
search_btns = ls.elements(html_tree, "//input[contains(@value, 'Lucky')]")

assert search_btn is not None
assert len(search_btns) == 1

test_one = ls.contains_string(html_tree, "Google")
test_two = ls.contains_any_string(html_tree, ["RockyRoad", "Lucky"])

assert test_one == True
assert test_two == True

test_three = ls.contains_string(html_tree, "RockyRoad")
test_four = ls.contains_any_string(html_tree, ["Waterloo", "Harbour"])

assert test_three == False
assert test_four == False
```