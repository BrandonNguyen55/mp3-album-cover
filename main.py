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
def split_filename(filename:string): 
    """ 
    Split the filename into artist and song name.
            
    @param filename - the filename of the mp3 file
    @return - a tuple of strings for the artist and song name
    """ 
    # If filename doesn't have the "{artist} - {song}" format return early
    if filename.count('-') != 1:
        return None, None 

    # Stem off the file extension
    filename = pathlib.Path(filename).stem

    # Split the file into artist and song
    artist_name, song_name = filename.split('-')
    artist_name = artist_name.strip()
    song_name = song_name.strip()
    return artist_name, song_name 


def print_audio_metadata(audio:eyed3.AudioFile)-> None:
    """ 
    Prints the Audio Metadata given an AudioFile.
            
    @param audio - an AudioFile with the metadata      
    """    
    print(f"Title: {audio.tag.title}")
    print(f"Artist: {audio.tag.artist}")
    print(f"Album: {audio.tag.album}")
    print(f"Album Artist: {audio.tag.album_artist}")
    print(f"Composer: {audio.tag.composer}")
    print(f"Publisher: {audio.tag.publisher}")
    print(f"Genre: {audio.tag.genre}")


def edit_audio(audio_file:eyed3.AudioFile, artist:string, song_title:string, album:string)-> None:
    """ 
    Edit the Artist and Title Metadata of the AudioFile.

    @param audio_file - an AudioFile with the metadata      
    @param artist - the name of the artist
    @param song_title - the title of the song       
    """
    # Edit the metadata
    audio_file.tag.artist = artist 
    audio_file.tag.title = song_title 
    audio_file.tag.album = album 

    # Save the AudioFile
    audio_file.tag.save()


def add_album_art(audio_file:eyed3.AudioFile, art_url:string):
    """
    Add album art to the AudioFile.

    @param audio_file - an AudioFile with the metadata      
    @param art_url - the url of the album art
    """
    response = urllib.request.urlopen(art_url)
    image_data = response.read()
    audio_file.tag.images.set(ImageFrame.FRONT_COVER, image_data, u"cover")
    audio_file.tag.save()


def process_file(audio_filename):
    """
    Process the audio filename, giving it the metadata and album art.

    @param audio_filename - the filename of the mp3 audio file
    """
    name1, name2 = split_filename(audio_filename) 

    # Search on Google
    search_query = google(f"Spotify {name1} {name2} song")
    # TODO: Pick wikipedia site
    url = search_query[0]

    # Make an instance of the Website to scrape     
    html_text, status = get_website_html(url)
    website = Spotify(html_text)

    # Save the new info to the audio_file 
    audio_file = eyed3.load(os.path.join(TEST_DATA_DIR, audio_filename))
    audio_file.initTag(version=(2, 3, 0))  


    edit_audio(audio_file, website.get_artist(), website.get_song_title(), website.get_album())
    add_album_art(audio_file, website.get_album_art_url())


#===========================================================================================
# Main Function
#===========================================================================================
if __name__ == "__main__":
    file_fail = []
    process_fail = []
    
    # Now to edit the audio
    for audio_filename in os.listdir(TEST_DATA_DIR):
        artist_name, song_title = split_filename(audio_filename) 
        print(f"{artist_name} -- {song_title}")
        if artist_name == None:
            file_fail.append(audio_filename)
            continue
        try: 
            process_file(audio_filename)
        except:
            process_fail.append(audio_filename)

    print("\n\nSongs that Failed File Split:")
    for i in file_fail:
        print(f" {i}") 
    print("\n\nSongs that Failed Process:")
    for i in process_fail:
        print(f" {i}") 