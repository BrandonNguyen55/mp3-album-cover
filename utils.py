#!/usr/bin/env python
# Library Imports
import string
import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Global variables
CWD = os.getcwd()
TEST_DIR = os.path.join(CWD, "..", "test", "music")
ROCK_DIR = os.path.join(TEST_DIR, "Rock")
TEST_DATA_DIR = os.path.join(TEST_DIR, "TestData")

#===========================================================================================
# Functions
#===========================================================================================
""" Get the Website HTML From the url
        @param url - The url link of the website
        @return - The htmlText and status
"""
def getWebsiteHTML(url):
    # Make a request to genius
    res = requests.get(url)
    htmlText = res.text
    status = res.status_code
    return htmlText, status
    
""" Search up Google and return a list of urls
        @param query - The search quere
        @param num - The num of urls to return
        @return - A list of urls
"""
def google(query, num=10):
    return [i for i in search(query, tld="co.in", num=num, stop=10, pause=2)]


""" Save the html file
        @param filename - The name of the html file
        @param html - The HTML 
"""
def saveHTML(filename, html):
    with open(os.path.join(CWD, 'temp', f'{filename}.html'), 'w', encoding = 'utf-8') as f:
        f.write(str(html))


""" Save the jpeg file from a url link
        @param url - The url link
"""
def saveJPG(url, filename):
    
    with open(os.path.join(CWD, 'temp', f'{filename}.jpg'), 'wb') as f:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            f.write(block)

    return open(os.path.join(CWD, 'temp', f'{filename}.jpg'), 'rb').read() 



