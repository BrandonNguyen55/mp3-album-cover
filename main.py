#!/usr/bin/env python
# Library Imports
import string
import os
import eyed3

# Global variables
CWD = os.getcwd()
TEST_DIR = os.path.join(CWD, "..", "test", "music")
#===========================================================================================
#Main Function
#===========================================================================================
def main():
    audio = eyed3.load(os.path.join(TEST_DIR, "Rock", "Eric Johnson - Cliffs Of Dover.mp3"))

    print(f"Title: {audio.tag.title}")
    print(f"Artist: {audio.tag.artist}")
    print(f"Album: {audio.tag.album}")
    print(f"Album Artist: {audio.tag.album_artist}")
    print(f"Composer: {audio.tag.composer}")
    print(f"Publisher: {audio.tag.publisher}")
    print(f"Genre: {audio.tag.genre}")

    return 0


main()
