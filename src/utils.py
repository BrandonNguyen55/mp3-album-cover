#!/usr/bin/env python
# Library Imports
import string
import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from inspect import getsourcefile
import pathlib as pathlib

# Global variables
CWD=os.path.dirname(getsourcefile(lambda:0))

PROJECT_DIR = os.path.join(CWD, "..")
TEST_DIR = os.path.join(PROJECT_DIR, "test", "music")
TEMP_DIR = os.path.join(PROJECT_DIR, "temp")
ROCK_DIR = os.path.join(TEST_DIR, "Rock")
TEST_DATA_DIR = os.path.join(TEST_DIR, "TestData")

#===========================================================================================
# Functions
#===========================================================================================
def split_filename(filename:string):
    """ 
    Split the filename into artist and song name.
            
    @param filename - the filename of the mp3 file
    @return - a tuple of strings for the artist and song name
    """ 
    # If filename doesn't have the "{artist} - {song}" format return early
    if filename.count('-') != 1:
        return None, filename  

    # Stem off the file extension
    filename = pathlib.Path(filename).stem

    # Split the file into artist and song
    artist_name, song_name = filename.split('-')
    artist_name = artist_name.strip()
    song_name = song_name.strip()
    return artist_name, song_name

def get_website_html(url):
    """ 
    Get the Website HTML From the url.
    
    @param url - The url link of the website
    @return - The htmlText and status
    """
    # Make a request to genius
    res = requests.get(url)
    html_text = res.text
    status = res.status_code
    return html_text, status
    
def google(query, num=10):
    """ 
    Search up Google and return a list of urls.
   
    @param query - The search quere
    @param num - The num of urls to return
    @return - A list of urls
    """
    return [i for i in search(query, tld="co.in", num=num, stop=10, pause=2)]


def save_html(filename, html):
    """ 
    Save the html file.
        
    @param filename - The name of the html file
    @param html - The HTML 
    """
    with open(os.path.join(TEMP_DIR, f'{filename}.html'), 'w', encoding = 'utf-8') as f:
        f.write(str(html))


def save_jpg(url, filename):
    """ 
    Save the jpeg file from a url link.
   
    @param url - The url link
    """
    with open(os.path.join(TEMP_DIR, f'{filename}.jpg'), 'wb') as f:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            f.write(block)

    return open(os.path.join(CWD, 'temp', f'{filename}.jpg'), 'rb').read() 



