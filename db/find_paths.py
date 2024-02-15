#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import sqlite3
import os

class SQLiteQuery:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb): 
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.cursor.close()
            self.conn.close()

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

def get_book_folders(db_path, tag1, tag2):
    paths = []
    with SQLiteQuery(db_path) as cursor:
        cursor.execute(query, (tag1, tag2))
        results = cursor.fetchall()
        
    for title, path in results:
        paths.append(path)
    return paths

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)

    # ut1 = os.getenv("USER_1_TAG")
    # ut2 = os.getenv("USER_2_TAG")
    # format_tag = "Hardcopy"
    # user_tag = ut1

    # db_path = os.getenv("TEST_CALIBRE_DB_PATH")

    # book_folders = get_book_folders(db_path, user_tag, format_tag)
    # print(book_folders)

if __name__ == '__main__':
    main()

