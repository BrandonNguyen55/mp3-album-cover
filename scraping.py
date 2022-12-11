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

    def __repr__(self):
        return f"{self.get_artist()} - {self.get_song_title()}\nAlbum: {self.get_album()}\nAlbum Art url: {self.get_album_art_url()}"

    def get_artist(self):
        pass

    def get_song_title(self):
        pass

    def get_album(self):
        pass

    def get_jpg(self):
        pass

class Wikipedia(Website):
    def __init__(self, html):
        super().__init__(html)
        self.domain = "https://en.wikipedia.org/"
        self.table_vevant = self.html_soup.find("table", class_="infobox vevent")

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

class Spotify(Website):
    def __init__(self, html):
        super().__init__(html)
        self.domain = "https://open.spotify.com/"

    def get_artist(self):
        artist_info_tag = self.html_soup.find("div", class_="rS_2dJG9pgqS2A2BZ5rZ")
        artist_tag = artist_info_tag.find("div") 
        return artist_tag.text.strip()

    def get_song_title(self):
        song_tag = self.html_soup.find("span", class_="JmV8FMNND0hJM4fCS9E4")
        return song_tag.text.strip()

    def get_album(self):
        album_info_tag = self.html_soup.find("div", class_="TS85Qkpioa31wR0p4kzT")
        album_tag = album_info_tag.find("div", class_=re.compile("TypeElement"))
        return album_tag.text.strip()

    def get_album_art_url(self):
        jpg_tag = self.html_soup.find("meta", property="og:image")
        if jpg_tag:
            return jpg_tag["content"]        
        return None    

if __name__ == "__main__":
    # Testing Code
    url = "https://open.spotify.com/track/1fulFeOm8Zm5QJDSLRpoCc" 
    # url = "https://open.spotify.com/track/429IbFR4yp2J81CeTwF5iY"
    # Make an instance of the Website to scrape     
    html_text, status = get_website_html(url)
    
    a = Spotify(html_text)
    z = a.html_soup
    b = a.get_song_title()
    c = a.get_artist()
    d = a.get_album()
    print(f"{c} - {b} ({d})")