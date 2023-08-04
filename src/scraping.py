#!/usr/bin/env python
# Library Imports
import os
import pathlib
import re
import string

import eyed3
import requests
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

    def get_artist(self):
        song_by_artist_tag = self.table_vevant.find("th", class_="infobox-header description")        
        artist_tag = song_by_artist_tag.find_all("a")[1]
        return artist_tag.text.strip()

    def get_song_title(self):
        song_tag = self.table_vevant.find("th", class_="infobox-above summary")
        song_str = song_tag.string
        return song_str.strip()[1:-1]

    def get_album(self):
        album_tag = self.table_vevant.find(text = re.compile('from the album\n'(()))).parent   
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


    """ Get the Artist Name """
    def get_artist(self):
        class_name = "Type__TypeElement-sc-goli3j-0 ieTwfQ b81TNrTkVyPCOH0aDdLG"
        artist_div = self.html_soup.find("div", class_= class_name)

        artist_tag = artist_div.find("a")
        return artist_tag.text.strip()


    """ Get the Song Title """
    def get_song_title(self):
        class_name = "Type__TypeElement-sc-goli3j-0 gyivyS gj6rSoF7K4FohS2DJDEm"
        song_tag = self.html_soup.find("h1", class_=class_name)
        return song_tag.text.strip()


    """ Get the Album Name """
    def get_album(self):
        class_name = "z0LHX2yZ2wBi7LCow2r6"
        album_div = self.html_soup.find("div", class_=class_name)
        
        class_name = "Type__TypeElement-sc-goli3j-0 ieTwfQ"
        album_tag = self.html_soup.find("span", class_=class_name)
        return album_tag.text.strip()


    """ Get the Album Art URL """
    def get_album_art_url(self):
        class_name = "Type__TypeElement-sc-goli3j-0 ieTwfQ b81TNrTkVyPCOH0aDdLG"
        jpg_tag = self.html_soup.find("meta", property="og:image")
        if jpg_tag:
            return jpg_tag["content"]        
        return None    
