#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os

import time
from datetime import datetime
from libib_records.ingest_libib import get_book_records as get_books
from pdf.make_pdf import create_pdf

marker = 'marker'




def strip_book_data(complete_data):
    data_keys = complete_data.keys()
    stripped_data = {}
    key_data =["title" ,    "creators",    "first_name",    "last_name",    "ean_isbn13",    "upc_isbn10"]
    for key in key_data:
        if key not in data_keys:
            pass
        else:
            stripped_data[key] = complete_data[key]
    if "title" in stripped_data:
        stripped_data["unknown"] = False
        return stripped_data
    else:
        return {"unknown": True}


def time_ext():
    now = datetime.now()
    milliseconds = int(now.microsecond / 1000)
    formatted_time = now.strftime("%H%M%S") + '{:03}'.format(milliseconds)
    time.sleep(0.001)
    return formatted_time


class BookPDF:
    def __init__(self, data, folder_out, owner=""):
        self.data = data
        self.out_folder = folder_out
        self.owner = owner
        self.metadata_set = {}
        self.filename = "title?@authors?@isbn0@"
        self.output_path = "pdf/book_pdfs"
        self.post_init()

    def make_filename(self):
        name_string = ""
        title_string = "title" + self.data["title"] if self.data["title"] else "?"
        if self.data["first_name"] and self.data["last_name"]:
            author_string = self.data["first_name"] + " " + self.data["last_name"]
        else:
            author_string = "?"
        author = "authors" + \
            self.data["creators"] if self.data["creators"] else author_string
        
        isbn = self.data["upc_isbn10"] if self.data["upc_isbn10"] else "0"
        isbn = "isbn" +  self.data["ean_isbn13"] if self.data["ean_isbn13"] else isbn

        def cleanse_string(info_string):
            if ":" in info_string:
                info_string = info_string.replace(":", "-")
            if "@" in info_string:
                info_string = info_string.replace("@", " ")
            return info_string
        
        title_string = cleanse_string(title_string)
        author = cleanse_string(author)
        isbn = cleanse_string(isbn)

        name_string += title_string + "@"
        name_string += author + "@"
        name_string += isbn + "@"
        return name_string

    def post_init(self):
        if not self.data["unknown"]:
            self.filename = self.make_filename()
        else:
            self.filename = self.filename + time_ext()

   
    def make_pdf(self):
        out_path = os.path.join(self.output_path, self.filename) + ".pdf"
        create_pdf(out_path, owner=self.owner)


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
  
    owner = os.getenv("OWNER_TAG")  # ! MODIFY OWNER_TAG FOR NAME
    csv_path =  os.getenv("INCOMING_CSV") 
    dump_pdfs = os.getenv("DUMP_PDFS")

    hardcopies = get_books(csv_path=csv_path)
    for hardcopy in hardcopies:
        data = strip_book_data(hardcopy)
        book = BookPDF(data, folder_out=dump_pdfs, owner=owner)
        book.make_pdf()
        book.add_metadata()

if __name__ == '__main__':
    main()