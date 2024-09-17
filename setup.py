from setuptools import setup, find_packages

setup(
    name='shanaly_browser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'webdriver-manager',
    ],
    description='A library for browsing and extracting content from search results',
    author='Alfred Baraka Rugoye',
    author_email='your.email@example.com',
    url='https://github.com/Shanaly34/shanaly_browser',
)
