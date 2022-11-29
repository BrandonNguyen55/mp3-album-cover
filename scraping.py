#!/usr/bin/env python
# Library Imports
import string
import os
import pathlib
import eyed3
import requests
from bs4 import BeautifulSoup
from utils import *

#===========================================================================================
# Functions
#===========================================================================================
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

    # Get the table vevant
    tableVevant = htmlBSoup.find("table", class_="infobox vevent")

    # Get the Song Title
    songTag = tableVevant.find("th", class_="infobox-above summary")
    songStr = songTag.string

    # Strip the whitespace and remove beginning and end quotes
    songTitle = songStr.strip()[1:-1]

    return htmlBSoup, tableVevant, songTitle




#===========================================================================================
# Main
#===========================================================================================

# url = "https://genius.com/Saosin-i-never-wanted-to-lyrics"
url = "https://en.wikipedia.org/wiki/Ruby_(Kaiser_Chiefs_song)"
# url = "https://en.wikipedia.org/wiki/Cliffs_of_Dover_(composition)"
# url = "https://open.spotify.com/track/0VhhaYztcRWc7PEjJCjr1g"
htmlText, status = getWebsiteHTML(url)

# html, table, song = scrapeWikipedia(htmlText)

htmlBSoup = BeautifulSoup(htmlText, "html.parser")
htmlBSoup = BeautifulSoup(htmlBSoup.prettify(), "html.parser")

    