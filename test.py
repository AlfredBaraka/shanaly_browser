from shanaly_browser import ShanalyBrowser

# Initialize with a query and number of top results
browser = ShanalyBrowser("Alfred Baraka Rugoye?", num_results=1)

# Fetch content from the top search results
content = browser.fetch_content()

# Print the extracted content
for url, texts in content.items():
    print(f"Content from {url}:")
    for i, text in enumerate(texts, start=1):
        print(f"Content {i}: {text}")