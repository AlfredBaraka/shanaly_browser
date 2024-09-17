import unittest
from shanaly_browser import ShanalyBrowser

class TestShanalyBrowser(unittest.TestCase):
    def test_search_bing(self):
        browser = ShanalyBrowser("Python programming", num_results=1)
        links = browser.search_bing()
        self.assertTrue(len(links) > 0)
        browser.close_driver()
    
    def test_extract_content(self):
        browser = ShanalyBrowser("Python programming", num_results=1)
        links = browser.search_bing()
        if links:
            content = browser.extract_content(links[0])
            self.assertTrue(len(content) > 0)
        browser.close_driver()

if __name__ == "__main__":
    unittest.main()
