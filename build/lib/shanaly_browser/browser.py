import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
from typing import List, Dict, Any

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




class EnhancedShanalyBrowser(ShanalyBrowser):
    def __init__(self, query: str, num_results: int = 1, num_content: int = 10):
        super().__init__(query, num_results)
        self.num_content = num_content

    def extract_content(self, url: str) -> List[str]:
        self.driver.get(url)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Extract content from <p> tags
            paragraphs = soup.find_all('p', limit=self.num_content)
            if paragraphs:
                texts = [p.get_text() for p in paragraphs]
            else:
                # If no <p> tags, fallback to <div> tags
                divs = soup.find_all('div', limit=self.num_content)
                texts = [div.get_text() for div in divs]
        
        except Exception as e:
            print(f"Error extracting content from {url}: {e}")
            texts = []
        
        return texts

    def fetch_content(self) -> Dict[str, Any]:
        links = self.search_bing()
        all_content = {}
        for idx, url in enumerate(links, start=1):
            print(f"\nVisiting top result {idx}: {url}")
            content = self.extract_content(url)
            if not content:
                print(f"No content found on {url}")
            all_content[url] = content
        
        self.close_driver()
        
        # Return results as JSON
        return all_content

    def get_content_as_json(self) -> str:
        content = self.fetch_content()
        return json.dumps(content, indent=2, ensure_ascii=False)





class EnhancedShanalyBrowserPro:
    def __init__(self, query: str, num_results: int = 1, num_content: int = 10):
        self.query = query
        self.num_results = num_results
        self.num_content = num_content
        self.driver = self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def search_bing(self) -> List[str]:
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

    def extract_content(self, url: str) -> List[str]:
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            paragraphs = soup.find_all('p', limit=self.num_content)
            if paragraphs:
                texts = [p.get_text() for p in paragraphs]
            else:
                divs = soup.find_all('div', limit=self.num_content)
                texts = [div.get_text() for div in divs]
        except Exception as e:
            print(f"Error extracting content from {url}: {e}")
            texts = []
        return texts

    def close_driver(self):
        self.driver.quit()

    def fetch_content(self) -> Dict[str, Any]:
        links = self.search_bing()
        all_content = {}
        
        # Use ThreadPoolExecutor to handle concurrency
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(self.extract_content, url): url for url in links}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    content = future.result()
                    all_content[url] = content
                except Exception as e:
                    print(f"Error fetching content for {url}: {e}")
                    all_content[url] = []

        self.close_driver()
        return all_content

    def get_content_as_json(self) -> str:
        content = self.fetch_content()
        return json.dumps(content, indent=2, ensure_ascii=False)
    
    
    

import aiohttp
import asyncio


class AsyncShanalyBrowser:
    def __init__(self, query: str, num_results: int = 1, num_content: int = 10):
        self.query = query
        self.num_results = num_results
        self.num_content = num_content

    async def fetch(self, session, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    async def extract_content(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('p', limit=self.num_content)
        if paragraphs:
            texts = [p.get_text() for p in paragraphs]
        else:
            divs = soup.find_all('div', limit=self.num_content)
            texts = [div.get_text() for div in divs]
        return texts

    async def search_bing(self) -> List[str]:
        search_url = f"https://www.bing.com/search?q={self.query}"
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, search_url)
            soup = BeautifulSoup(html, 'html.parser')
            search_results = soup.select('a[href^="http"]')
            links = [result['href'] for result in search_results[:self.num_results]]
            return links

    async def fetch_content(self) -> Dict[str, List[str]]:
        links = await self.search_bing()
        all_content = {}
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in links]
            responses = await asyncio.gather(*tasks)
            for url, html in zip(links, responses):
                content = await self.extract_content(html)
                all_content[url] = content
        return all_content

    def get_content_as_json(self) -> str:
        loop = asyncio.get_event_loop()
        content = loop.run_until_complete(self.fetch_content())
        return json.dumps(content, indent=2, ensure_ascii=False)
