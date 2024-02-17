#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
import shutil

from covers.create_cover import make_cover

marker = 'marker'

def make_new_cover(cover):
    make_cover(cover)

def copy_cover(source_file_path, destination_file_path):
    shutil.copy(source_file_path, destination_file_path)

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    

if __name__ == '__main__':
    main()