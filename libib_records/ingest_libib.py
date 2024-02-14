#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
import csv

marker = 'marker'
def get_path():
    return  os.getenv("TEST_INCOMING_CSV")

def get_book_records(csv_path):
    with open(csv_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        return [ row for row in csv_reader]

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
  
    csv_path = get_path()
    hardcopy_records = get_book_records(csv_path)
    print(len(hardcopy_records))

if __name__ == '__main__':
    main()