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
        html_soup = BeautifulSoup(html, "html.parser")
        self.html_soup = BeautifulSoup(html_soup.prettify(), "html.parser")

    def get_artist(self):
        pass

    def get_song_title(self):
        pass

    def get_album(self):
        pass

    def get_jpg(self):
        pass

""" Scrape the artist and song from the HTML
        @param htmlText - The HTML of the Website
        @return - The artist and song title 
"""
def scrape_genius_com(html_text):
    # Use Beatiful Soup to make parsing easier
    html_soup = BeautifulSoup(html_text, "html.parser")
    html_soup = BeautifulSoup(html_soup.prettify(), "html.parser")

    result = None
    return result




class Wikipedia(Website):
    def __init__(self, html):
        super().__init__(html)
        self.website = "https://en.wikipedia.org/"
        self.table_vevant = self.html_soup.find("table", class_="infobox vevent")

    def __repr__(self):
        return f"{self.get_artist()} - {self.get_song_title()}\nAlbum: {self.get_album()}\nAlbum Art url: {self.getAlbumArtUrl()}"

    def get_artist(self):
        song_by_artist_tag = self.table_vevant.find("th", class_="infobox-header description")        
        artist_tag = song_by_artist_tag.find_all("a")[1]
        return artist_tag.text.strip()

    def get_song_title(self):
        song_tag = self.table_vevant.find("th", class_="infobox-above summary")
        song_str = song_tag.string
        return song_str.strip()[1:-1]

    def get_album(self):
        album_tag = self.table_vevant.find(text = re.compile('from the album\n')).parent   
        album_tag_list = [i.text.strip() for i in album_tag.children] 
        return album_tag_list[1]

    def get_album_art_url(self):
        jpg_tag = self.html_soup.find("meta", property="og:image")
        if jpg_tag:
            return jpg_tag["content"]        
        return None






