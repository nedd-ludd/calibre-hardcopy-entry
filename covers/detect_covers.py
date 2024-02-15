#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-15
"""
import os
marker = 'marker'


def get_folder_contents(folder_path):
    """Returns a list of filenames in the given folder path."""
    try:
        filenames = [f for f in os.listdir(
            folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return filenames
    except Exception as e:
        return str(e)
    
def get_covers(folder_path):
    contents = get_folder_contents(folder_path)
    def validator(file):
        return True if "cover" in file and file.endswith(".jpg") else False
    covers = [file for file in contents if validator(file)]
    return covers
    


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    covers = get_covers(os.getenv("TEST_BOOK_PATH"))
    print(covers)


if __name__ == '__main__':
    main()