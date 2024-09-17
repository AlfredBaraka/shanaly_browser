import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class ShanalyBrowser:
    def __init__(self, query, num_results=1):
        self.query = query
        self.num_results = num_results
        self.driver = self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def search_bing(self):
        self.driver.get('https://www.bing.com')
        
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.send_keys(self.query)
            search_box.send_keys(Keys.RETURN)
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="http"]'))
            )
            
            search_results = self.driver.find_elements(By.CSS_SELECTOR, 'a[href^="http"]')
            if not search_results:
                print("No search results found.")
                return []
            
            links = [result.get_attribute('href') for result in search_results[:self.num_results]]
            return links
        
        except Exception as e:
            print(f"Error during Bing search: {e}")
            return []

    def extract_content(self, url):
        self.driver.get(url)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            paragraphs = soup.find_all('p')
            if paragraphs:
                texts = [p.get_text() for p in paragraphs]
            else:
                divs = soup.find_all('div', limit=10)
                texts = [div.get_text() for div in divs]
        
        except Exception as e:
            print(f"Error extracting content from {url}: {e}")
            texts = []
        
        return texts

    def close_driver(self):
        self.driver.quit()

    def fetch_content(self):
        links = self.search_bing()
        all_content = {}
        for idx, url in enumerate(links, start=1):
            print(f"\nVisiting top result {idx}: {url}")
            content = self.extract_content(url)
            if not content:
                print(f"No content found on {url}")
            all_content[url] = content
        self.close_driver()
        return all_content
