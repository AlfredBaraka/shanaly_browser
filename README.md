# ShanalyBrowser

`ShanalyBrowser` is a Python library for performing web searches and extracting content from the top search results.

## Installation

To install `ShanalyBrowser`, use pip:

```bash
pip install shanaly_browser
```

## Usage

Here's a basic example of how to use the library:

```python
from shanaly_browser import ShanalyBrowser

# Initialize with a query and number of top results
browser = ShanalyBrowser("Python programming", num_results=3)

# Fetch content from the top search results
content = browser.fetch_content()

# Print the extracted content
for url, texts in content.items():
    print(f"Content from {url}:")
    for i, text in enumerate(texts, start=1):
        print(f"Content {i}: {text}")
```

### Parameters

- `query` (str): The search query.
- `num_results` (int): The number of top search results to process.

## License
```
This project is licensed under the MIT License.
```


