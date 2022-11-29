#!/usr/bin/env python
# Library Imports
import string
import os
import pathlib
import eyed3
from bs4 import BeautifulSoup
from utils import *
  
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
        @param artistName - the name of the artist
        @param songTitle - the title of the song       
"""
def editAudioArtistTitle(audioFile:eyed3.AudioFile, artistName:string, songTitle:string)-> None:
    # Edit the metadata
    audioFile.tag.artist = artistName 
    audioFile.tag.title = songTitle 

    # Save the AudioFile
    audioFile.tag.save()



#===========================================================================================
# Main Function
#===========================================================================================
def main():
    filenameDump = []

    # for audioFile in os.listdir(ROCK_DIR):
    #     artistName, songName = splitFileName(audioFile) 
    #     if artistName == None:
    #         filenameDump.append(audioFile)
    #         continue
    #     print(f"{artistName} : {songName}")

    # print("\n\nFiles that didn't fit:")
    # for audioFile in filenameDump:
    #     print(f"\t{audioFile}")
    
    # print()
    # print() 
    # print("Example of using the eyed3 library to get the metadata I currently have on Eric Johnson's Cliffs Of Dover")
    # audio = eyed3.load(os.path.join(TEST_DIR, "Rock", "Eric Johnson - Cliffs Of Dover.mp3"))
    # printAudioMetaData(audio)

    
    # Now to edit the audio
    for audioFileName in os.listdir(TEST_DATA_DIR):
        artistName, songTitle = splitFileName(audioFileName) 
        if artistName == None:
            filenameDump.append(audioFileName)
            continue

        audioFile = eyed3.load(os.path.join(TEST_DATA_DIR, audioFileName))
        editAudioArtistTitle(audioFile, artistName, songTitle)
    
    return 0


main()
