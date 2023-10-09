import os
import sys
from inspect import getsourcefile

TEST_DIR=os.path.dirname(getsourcefile(lambda:0))
PROJECT_DIR = os.path.join(TEST_DIR, "..")
SRC_DIR = os.path.join(PROJECT_DIR, "src")

sys.path.insert(1, SRC_DIR)

import scraping
import utils

# The URL For the test
closer_lacuna_coil_spotify_url = "https://open.spotify.com/track/0hjOQVfGYP2NXINPOp4EgI" 

def test_get_website_html():
    _, status = utils.get_website_html(closer_lacuna_coil_spotify_url)
    assert status != 400

def test_google():
    link_list = utils.google("Closer Lacuna Coil Spotify Song") 
    assert closer_lacuna_coil_spotify_url in link_list
