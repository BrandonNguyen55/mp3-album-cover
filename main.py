#!/usr/bin/env python
# Library Imports
import string
import os
import pathlib
import eyed3
from eyed3.id3.frames import ImageFrame
from bs4 import BeautifulSoup
from utils import *
from scraping import *
import urllib.request
  
#===========================================================================================
# Functions
#===========================================================================================
""" Split the filename into artist and song name
        @param filename - the filename of the mp3 file
        @return - a tuple of strings for the artist and song name
"""
def split_file_name(filename:string): 
    # If filename doesn't have the "{artist} - {song} format return early
    if filename.count('-') != 1:
        return None, None 

    # Stem off the file extension
    filename = pathlib.Path(filename).stem

    # Split the file into artist and song
    artist_name, song_name = filename.split('-')
    artist_name = artist_name.strip()
    song_name = song_name.strip()
    return artist_name, song_name 

""" Prints the Audio Metadata given an AudioFile
        @param audio - an AudioFile with the metadata      
"""
def print_audio_meta_data(audio:eyed3.AudioFile)-> None:
    print(f"Title: {audio.tag.title}")
    print(f"Artist: {audio.tag.artist}")
    print(f"Album: {audio.tag.album}")
    print(f"Album Artist: {audio.tag.album_artist}")
    print(f"Composer: {audio.tag.composer}")
    print(f"Publisher: {audio.tag.publisher}")
    print(f"Genre: {audio.tag.genre}")


""" Edit the Artist and Title Metadata of the AudioFile
        @param audio_file - an AudioFile with the metadata      
        @param artist - the name of the artist
        @param song_title - the title of the song       
"""
def edit_audio(audio_file:eyed3.AudioFile, artist:string, song_title:string, album:string)-> None:
    # Edit the metadata
    audio_file.tag.artist = artist 
    audio_file.tag.title = song_title 
    audio_file.tag.album = album 

    # Save the AudioFile
    audio_file.tag.save()

def add_album_art(audio_file:eyed3.AudioFile, art_url:string):
    response = urllib.request.urlopen(art_url)
    image_data = response.read()
    audio_file.tag.images.set(ImageFrame.FRONT_COVER, image_data, u"cover")
    audio_file.tag.save()


def process_file(audio_filename):
    name1, name2 = split_file_name(audio_filename) 

    # Search on Google
    search_query = google(f"{name1} {name2}")
    # TODO: Pick wikipedia site
    url = search_query[3]

    # Make an instance of the Website to scrape     
    html_text, status = get_website_html(url)
    website = Wikipedia(html_text)

    # Save the new info to the audio_file 
    audio_file = eyed3.load(os.path.join(TEST_DATA_DIR, audio_filename))
    audio_file.initTag(version=(2, 3, 0))  

    edit_audio(audio_file, website.get_artist(), website.get_song_title(), website.get_album())
    add_album_art(audio_file, website.get_album_art_url())


#===========================================================================================
# Main Function
#===========================================================================================
def main():
    filenameDump = []
    
    # Now to edit the audio
    for audio_filename in os.listdir(TEST_DATA_DIR):
        artist_name, song_title = split_file_name(audio_filename) 
        if artist_name == None:
            filenameDump.append(audio_filename)
            continue

        process_file(audio_filename)
    
    return 0

# url = "https://genius.com/Saosin-i-never-wanted-to-lyrics"
# url = "https://en.wikipedia.org/wiki/Ruby_(Kaiser_Chiefs_song)"
# url = "https://en.wikipedia.org/wiki/Cliffs_of_Dover_(composition)"
# url = "https://open.spotify.com/track/0VhhaYztcRWc7PEjJCjr1g"
# url = "https://en.wikipedia.org/wiki/The_Ghost_of_You"
main()
