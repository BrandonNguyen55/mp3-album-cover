import os
import sys
from inspect import getsourcefile

TEST_DIR=os.path.dirname(getsourcefile(lambda:0))
PROJECT_DIR = os.path.join(TEST_DIR, "..")
SRC_DIR = os.path.join(PROJECT_DIR, "src")

sys.path.insert(1, SRC_DIR)

import scraping
import utils


# Testing Code
"""
URL INFO:
    Song Title:         Closer
    Artist:             Lacuna Coil
    Album:              Karmacode
    Album Cover URL:    
"""
closer_lacuna_coil_spotify_url = "https://open.spotify.com/track/0hjOQVfGYP2NXINPOp4EgI" 
# Make an instance of the Website to scrape     

def test_get_song_title():
    html_text, status = utils.get_website_html(closer_lacuna_coil_spotify_url)
    assert status != 400

    song_spotify = scraping.Spotify(html_text)
    assert song_spotify.get_song_title() == "Closer"


def test_get_artist():
    html_text, status = utils.get_website_html(closer_lacuna_coil_spotify_url)
    assert status != 400

    song_spotify = scraping.Spotify(html_text)
    assert song_spotify.get_artist() == "Lacuna Coil"


def test_get_album():
    html_text, status = utils.get_website_html(closer_lacuna_coil_spotify_url)
    assert status != 400

    song_spotify = scraping.Spotify(html_text)
    assert song_spotify.get_album() == "Karmacode"


def test_get_album_art_url():
    html_text, status = utils.get_website_html(closer_lacuna_coil_spotify_url)
    assert status != 400

    song_spotify = scraping.Spotify(html_text)
    assert song_spotify.get_album_art_url() == "https://i.scdn.co/image/ab67616d0000b27321167f46d2169bf8cba15063"
