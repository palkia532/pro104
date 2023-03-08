import sys
import time
import random

import os
import shutil


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:\Users\pc\OneDrive\Desktop\C103\PRO-C103-Student-Boilerplate-main"
to_dir = "C:\Users\pc\OneDrive\Desktop\C103\PRO-C103-Student-Boilerplate-main"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
         if extension in value:
            file_name=os.path.basename(event.src_path)

            path1=from_dir+'/'+file_name
            path2=to_dir+'/'+key
            path3=to_dir+'/'+key+file_name

            if os.path.exists(key):
                print("Directory exists")
                print("Moving"+file_name+'......')
                shutil.move(path1,path3)
                time.sleep(1)
            else:
               print("Making Directory.....")
               os.makedirs(path2)
               print("Making"+file_name+'........')
               shutil.make(path1,path3)
               time.sleep(1)


        print(event)
        print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

# 