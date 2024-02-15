#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import sqlite3
import os
# TODO: copy new db
# TODO: Want book folder not image
# TODO: how do i combine tags searching in sqlite query
# TODO: context manager for sqlite query
# TODO: return list of folders


def get_book_folders(db_path, tag1, tag2):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query = '''
    SELECT b.title, b.path
    FROM books b
    JOIN books_tags_link btl ON b.id = btl.book
    JOIN tags t1 ON btl.tag = t1.id
    JOIN books_tags_link btl2 ON b.id = btl2.book
    JOIN tags t2 ON btl2.tag = t2.id
    WHERE t1.name = ? AND t2.name = ?
    GROUP BY b.id
    HAVING COUNT(DISTINCT t1.name) = 1 AND COUNT(DISTINCT t2.name) = 1
    '''
    c.execute(query, (tag1, tag2))
    results = c.fetchall()
    if results:
        for title, path in results:
            print(f"Title: {title}, Path: {path}")
    else:
        print(f"No books found with the tags '{tag1}' and '{tag2}'.")

    conn.close()

    return [1,2]

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    ut1 = os.getenv("USER_1_TAG")
    ut2 = os.getenv("USER_2_TAG")
    format_tag = "Hardcopy"
    user_tag = ut1

    db_path = os.getenv("TEST_CALIBRE_DB_PATH")

    book_folders = get_book_folders(db_path, user_tag, format_tag)
    print(book_folders)

if __name__ == '__main__':
    main()

