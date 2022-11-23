#!/usr/bin/env python
# Library Imports
import string
import os
import eyed3

# Global variables
CWD = os.getcwd()
TEST_DIR = os.path.join(CWD, "..", "test", "music")
ROCK_DIR =  os.path.join(CWD, "..", "test", "music", "Rock")



#===========================================================================================
# Functions
#===========================================================================================
def splitFileName(filename:string)-> (string, string): 
    if filename.count('-') != 1:
        return None, None 
    artistName, songName = filename.split('-')
    artistName = artistName.strip()
    songName = songName.strip()
    return artistName, songName 



""" Prints the Audio Metadata given an filename
        @param audio - an filename of the audio      
"""
def printAudioMetaData(audio:string)-> None:
    audio = eyed3.load(os.path.join(TEST_DIR, "Rock", "Eric Johnson - Cliffs Of Dover.mp3"))

    print(f"Title: {audio.tag.title}")
    print(f"Artist: {audio.tag.artist}")
    print(f"Album: {audio.tag.album}")
    print(f"Album Artist: {audio.tag.album_artist}")
    print(f"Composer: {audio.tag.composer}")
    print(f"Publisher: {audio.tag.publisher}")
    print(f"Genre: {audio.tag.genre}")




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




#===========================================================================================
# Main Function
#===========================================================================================
def main():
    for audioFile in os.listdir(ROCK_DIR):
        artistName, songName = splitFileName(audioFile) 
        if artistName == None:
            continue
        print(f"{artistName} : {songName}")

    
    print()
    print() 
    audio = eyed3.load(os.path.join(TEST_DIR, "Rock", "Eric Johnson - Cliffs Of Dover.mp3"))
    printAudioMetaData(audio)

    return 0


main()
