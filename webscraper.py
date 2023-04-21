''' 
install requests 
    $ pip install requests
install BeautifulSoup 
    $ pip install beautifulsoup4
# install  lxml 
    $ pip install lxml

to run the script
    python webscraper.py
'''
import requests
from bs4 import BeautifulSoup

# Send a request to the webpage
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'lxml')

# Extract information from the HTML content
title = soup.find('title').text
paragraphs = [p.text for p in soup.find_all('p')]

print(title)
print(paragraphs)
