from shanaly_browser import ShanalyBrowser, EnhancedShanalyBrowser, EnhancedShanalyBrowserPro, AsyncShanalyBrowser

# # Initialize with a query and number of top results
# browser = ShanalyBrowser("Alfred Baraka Rugoye?", num_results=1)

# # Fetch content from the top search results
# content = browser.fetch_content()

# print(content)

# # Print the extracted content
# for url, texts in content.items():
#     print(f"Content from {url}:")
#     for i, text in enumerate(texts, start=1):
#         print(f"Content {i}: {text}")



# # Example usage
# browser = EnhancedShanalyBrowser(query="Alfred Baraka Rugoye", num_results=1, num_content=3)
# json_content = browser.get_content_as_json()
# print(json_content)


# # # Example usage
# browser = EnhancedShanalyBrowserPro(query="jinsi ya kulipia maji dar es salaam?", num_results=1, num_content=10)
# json_content = browser.get_content_as_json()
# print(json_content)


# Example usage
# browser = AsyncShanalyBrowser(query="jinsi ya kulipia luku", num_results=1, num_content=3)
# json_content = browser.get_content_as_json()
# print(json_content)
