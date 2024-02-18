#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
from db.find_paths import get_book_folders
from covers.detect_covers import get_covers
from covers.cover_actions import make_new_cover, copy_cover
from covers.add_stamp import stamp_cover

class CoverManager:
    def __init__(self, folder = "", covers = [], ownership=""):
        self.folder = folder
        self.covers = covers
        self.ownership = ownership
        self.new_cover_files = []
        self.cover_set = ["cover.jpg" , "raw_cover.jpg"]
        self.conditions = [
            (["cover.jpg" , "raw_cover.jpg"], self.make_full_set),
            (["raw_cover.jpg"], self.make_raw)
        ]
        self.post_init()
        self.cover_name = self.folder + "/" + "cover.jpg"
        self.raw_name = self.folder + "/" + "raw_cover.jpg"

    def post_init(self):
        self.new_cover_files = list( set(self.cover_set) - set(self.covers))
    
    def manage_covers(self):
        for pattern, action in self.conditions:
            if set(pattern) == set(self.new_cover_files):
                action()
    
    def make_full_set(self):
        """
        1. Makes entirely new cover
        2. Stamps new cover
        3. Copies it across so bothe cover and raw_cover are present
        """
        print("no covers detected, making full set")
        make_new_cover(self.cover_name)
        stamp_cover(self.cover_name, self.cover_name, self.ownership)
        copy_cover(self.cover_name, self.raw_name)

    def make_raw(self):
        """
        1. Copies existing cover.jpg to raw_cover.jpg
        2. Stamps cover.jpg to be seen in calibre
        """
        print("copying cover and stamping")
        copy_cover(self.cover_name, self.raw_name)
        stamp_cover(self.cover_name, self.cover_name, self.ownership)

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    ut1, ut2, format = os.getenv(
        "USER_1_TAG"), os.getenv("USER_2_TAG"), "Hardcopy"
    db_path = os.getenv("TEST_CALIBRE_DB_PATH")
    user = ut1 #! change to user 2 for other stamp
    mod_folders =  get_book_folders(db_path, user, format)

    for folder in mod_folders:
        book_path = os.getenv("TEST_CALIBRE_LIBRARY_PATH") + "/" + folder
        print("Checking:", folder)
        cover_set = CoverManager(
            folder=book_path, covers=get_covers(book_path), ownership=user)
        cover_set.manage_covers()

if __name__ == '__main__':
    main()