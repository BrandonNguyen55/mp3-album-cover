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
def splitFileName(filename:string): 
    # If filename doesn't have the "{artist} - {song} format return early
    if filename.count('-') != 1:
        return None, None 

    # Stem off the file extension
    filename = pathlib.Path(filename).stem

    # Split the file into artist and song
    artistName, songName = filename.split('-')
    artistName = artistName.strip()
    songName = songName.strip()
    return artistName, songName 



   
""" Prints the Audio Metadata given an AudioFile
        @param audio - an AudioFile with the metadata      
"""
def printAudioMetaData(audio:eyed3.AudioFile)-> None:
    print(f"Title: {audio.tag.title}")
    print(f"Artist: {audio.tag.artist}")
    print(f"Album: {audio.tag.album}")
    print(f"Album Artist: {audio.tag.album_artist}")
    print(f"Composer: {audio.tag.composer}")
    print(f"Publisher: {audio.tag.publisher}")
    print(f"Genre: {audio.tag.genre}")


""" Edit the Artist and Title Metadata of the AudioFile
        @param audio - an AudioFile with the metadata      
        @param artist - the name of the artist
        @param songTitle - the title of the song       
"""
def editAudio(audioFile:eyed3.AudioFile, artist:string, songTitle:string, album:string)-> None:
    # Edit the metadata
    audioFile.tag.artist = artist 
    audioFile.tag.title = songTitle 
    audioFile.tag.album = album 

    # Save the AudioFile
    audioFile.tag.save()

def addAlbumArt(audioFile:eyed3.AudioFile, artUrl:string):
    # binData = saveJPG(artUrl, "art_cover")
    response = urllib.request.urlopen(artUrl)
    imageData = response.read()
    audioFile.tag.images.set(ImageFrame.FRONT_COVER, imageData, u"cover")
    audioFile.tag.save()


def processFile(audioFileName):
    name1, name2 = splitFileName(audioFileName) 

    # Search on Google
    searchQuery = google(f"{name1} {name2}")
    # TODO: Pick wikipedia site
    url = searchQuery[3]

    # Make an instance of the Website to scrape     
    htmlText, status = getWebsiteHTML(url)
    website = Wikipedia(htmlText)

    # Save the new info to the audioFile 
    audioFile = eyed3.load(os.path.join(TEST_DATA_DIR, audioFileName))
    audioFile.initTag(version=(2, 3, 0))  

    editAudio(audioFile, website.getArtist(), website.getSongTitle(), website.getAlbum())
    addAlbumArt(audioFile, website.getAlbumArtUrl())


#===========================================================================================
# Main Function
#===========================================================================================
def main():
    filenameDump = []
    
    # Now to edit the audio
    for audioFileName in os.listdir(TEST_DATA_DIR):
        artistName, songTitle = splitFileName(audioFileName) 
        if artistName == None:
            filenameDump.append(audioFileName)
            continue

        processFile(audioFileName)
    
    return 0


main()
