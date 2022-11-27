#!/usr/bin/env python
# Library Imports
import string
import os
import pathlib
import eyed3
import requests
from bs4 import BeautifulSoup

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

""" Scrape the artist and song from the HTML
        @param htmlText - The HTML of the Website
        @return - The artist and song title 
"""
def scrapeGeniusCom(htmlText):
    # Use Beatiful Soup to make parsing easier
    htmlBSoup = BeautifulSoup(htmlText, "html.parser")
    htmlBSoup = BeautifulSoup(htmlBSoup.prettify(), "html.parser")

    result = None
    return result


""" Scrape the artist and song from the HTML
        @param htmlText - The HTML of the Website
        @return - The artist and song title 
"""
def scrapeWikipedia(htmlText):
    # Use Beatiful Soup to make parsing easier
    htmlBSoup = BeautifulSoup(htmlText, "html.parser")
    htmlBSoup = BeautifulSoup(htmlBSoup.prettify(), "html.parser")

    # Get the Song Title
    songTag = htmlBSoup.find("th", class_="infobox-above summary")
    songStr = songTag.string
    # Strip the whitespace and remove beginning and end quotes
    songTitle = songStr.strip()[1:-1]

    table = htmlBSoup.find("table")



    return htmlBSoup, table, songTitle




# url = "https://genius.com/Saosin-i-never-wanted-to-lyrics"
url = "https://en.wikipedia.org/wiki/Ruby_(Kaiser_Chiefs_song)"
htmlText, status = getWebsiteHTML(url)

html, table, song = scrapeWikipedia(htmlText)


# with open(os.path.join(CWD, 'temp', 'outputWiki.html'), 'w', encoding = 'utf-8') as f:
    # f.write(str(htmlBSoup))
    