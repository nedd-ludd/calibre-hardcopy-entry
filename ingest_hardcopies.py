#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os

from libib_records.ingest_libib import get_book_records as get_books

marker = 'marker'

def get_path(collection):
    return os.getenv(collection)

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    #
    csv_path = get_path(collection="TEST_INCOMING_CSV")
    hardcopies = get_books(csv_path=csv_path)
    print(hardcopies)

if __name__ == '__main__':
    main()