#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-15
"""
import os
marker = 'marker'
def func():
    pass

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    func()

if __name__ == '__main__':
    main()