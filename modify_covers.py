#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
from db.find_paths import get_book_folders
marker = 'marker'
"""
check a folder
things to look for:
  cover
  cover_raw

if no cover - no meta data pulled back OR metadata pull not tried
if cover and no cover_raw - havent modified, need to modify
  copy cover cover -> cover_raw

"""
def get_folders():
    ut1, ut2, format = os.getenv(
        "USER_1_TAG"), os.getenv("USER_2_TAG"), "Hardcopy"
    db_path = os.getenv("TEST_CALIBRE_DB_PATH")
    return get_book_folders(db_path, ut1, format)


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    mod_folders = get_folders()
    print(mod_folders)

if __name__ == '__main__':
    main()