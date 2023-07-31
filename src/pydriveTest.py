#!/usr/bin/env python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import utils as utils
import os

# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)

# Create folder
folder_name = 'Python_Test_Music'
folder_metadata = {'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'}
folder = drive.CreateFile(folder_metadata)
folder.Upload()

# Upload file to folder
folderid = folder['id']
file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folderid}]})
file.SetContentFile('testfile.txt')
file.Upload()

# iterating thought all the files/folder
# of the desired directory
for x in os.listdir(utils.TEST_DATA_DIR):
    f = drive.CreateFile({'title': x})
    f.SetContentFile(os.path.join(utils.TEST_DATA_DIR, x))
    f.Upload()
  
    # Due to a known bug in pydrive if we 
    # don't empty the variable used to
    # upload the files to Google Drive the
    # file stays open in memory and causes a
    # memory leak, therefore preventing its 
    # deletion
    f = None

