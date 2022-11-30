#!/usr/bin/env python
# Library Imports
import string
import os
import pathlib
import eyed3
import requests
import re
from bs4 import BeautifulSoup
from utils import *



#===========================================================================================
# Functions
#===========================================================================================
class Website:
    def __init__(self, html):
        # Use Beatiful Soup to make parsing easier
        htmlBSoup = BeautifulSoup(html, "html.parser")
        self.htmlBSoup = BeautifulSoup(htmlBSoup.prettify(), "html.parser")

    def getArtist(self):
        pass

    def getSongTitle(self):
        pass

    def getAlbum(self):
        pass

    def getJPEG(self):
        pass

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




class Wikipedia(Website):
    def __init__(self, html):
        super().__init__(html)
        self.website = "https://en.wikipedia.org/"
        self.tableVevant = self.htmlBSoup.find("table", class_="infobox vevent")

    def __repr__(self):
        return f"{self.getArtist()} - {self.getSongTitle()}\nAlbum: {self.getAlbum()}\nAlbum Art url: {self.getAlbumArtUrl()}"

    def getArtist(self):
        songByArtistTag = self.tableVevant.find("th", class_="infobox-header description")        
        artistTag = songByArtistTag.find_all("a")[1]
        return artistTag.text.strip()

    def getSongTitle(self):
        songTag = self.tableVevant.find("th", class_="infobox-above summary")
        songStr = songTag.string
        return songStr.strip()[1:-1]

    def getAlbum(self):
        albumTag = self.tableVevant.find(text = re.compile('from the album\n')).parent   
        albumTagList = [i.text.strip() for i in albumTag.children] 
        return albumTagList[1]

    def getAlbumArtUrl(self):
        jpgTag = self.htmlBSoup.find("meta", property="og:image")
        if jpgTag:
            return jpgTag["content"]        
        return None

    """ Scrape the artist and song from the HTML
            @param htmlText - The HTML of the Website
            @return - The artist and song title 
    """




#===========================================================================================
# Main
#===========================================================================================

# url = "https://genius.com/Saosin-i-never-wanted-to-lyrics"
# url = "https://en.wikipedia.org/wiki/Ruby_(Kaiser_Chiefs_song)"
# url = "https://en.wikipedia.org/wiki/Cliffs_of_Dover_(composition)"
# url = "https://open.spotify.com/track/0VhhaYztcRWc7PEjJCjr1g"
url = "https://en.wikipedia.org/wiki/The_Ghost_of_You"
htmlText, status = getWebsiteHTML(url)

# artist, songTitle, album, songType, table = scrpeWikipedia(htmlText)

htmlBSoup = BeautifulSoup(htmlText, "html.parser")
htmlBSoup = BeautifulSoup(htmlBSoup.prettify(), "html.parser")

wiki = Wikipedia(htmlText)
