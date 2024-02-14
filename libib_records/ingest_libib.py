#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
import csv

marker = 'marker'
def func(csv):
    print(csv)
    

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    csv = os.getenv("TEST_INCOMING_CSV")
    func(csv)

if __name__ == '__main__':
    main()