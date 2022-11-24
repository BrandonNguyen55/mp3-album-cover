# Design Doc

## Preface
I am too stingy to buy Spotify Premium, and I still want the ability to play music without wifi and with my phone turned off. I can accomplish this with downloading mp3 files onto Documents by Readle, however, there are some problems.
- The Metadata is default blank, so I would have to manually edit each file which is a pain
- The mp3 file does not have a way to add Cover Art, so I would need to add it manually on my computer, which is also a pain

## Goal
Create a Program to supplement my music usage in Documents on the Iphone:
- Add the important Metadata
    - Artist
    - Song Name
    - Album
    - Genre (would be nice for organization)
- Add Cover Art
    - Album Covers
    - Allow for custom Pics if user chooses
- Allow Custom Ordering
    - Documents doesn't have custom ordering, but it can sort by date, so we can make it custom by changing the date
- Encapsulate everything via GUI or website
    - Make it so easy a monkey can use it

## Flow of the Program
1. .mp3 File Comes in
    - Usually in a form of *artist - song.mp3* 
2. If Artist and Songname Metadata is extracted from filename and updated onto the filename
3. Search on a site to figure out more metadata, ideally an album
4. Search on a site to get a album cover art, song cover art, or custom art
5. Sort these files to a custom ordering
6. Allow grouping of these files into various files
    - I have default folders, but if I add new music, they can get sorted into the correct folder 


## Questions
1. How do I get and set the metadata?
    - The eye3d library is a good library to use, just load a filename and an AudioFile object is made to access and modify metadata
2. How do I search online?
    - Google or Spotify maybe, Spotify have a large selection of music, Youtube and Soundcloud
    - The request library seems to be a good library to send https requests
    - The BeautifulSoup library seems to be good library for scraping websites
3. What Websites should I use to scrape Metadata?
    - After research, it seems there isn't specific website to grab metadata given a artist or song title
        - The big problem is we dont really know if the filename will be in the format we want
            - Maybe the format is flipped, *{song title} - {artist}*
            - Maybe only the song title is shown
            - Maybe there is a "-" in the song title or artist name
        - But we do have websites that we can probably test to grab metadata, at least figure out for certain which is the song title and which is the artist
            - wikipedia.com
            - genius.com 
            - azlyrics.com