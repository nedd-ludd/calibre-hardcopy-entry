#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
marker = 'marker'


def make_cover(cover):
    # 500 * 326?
    pass

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    cover=""
    make_cover(cover)

if __name__ == '__main__':
    main()