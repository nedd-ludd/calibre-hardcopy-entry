#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
from reportlab.pdfgen import canvas

def create_pdf(out_path, owner=""):
    msg = "This is a placeholder pdf representing real book"
    owner_string = f"Owner: {owner}" if owner else f"Owner: ?"
    text_lines = [msg, owner_string]

    c = canvas.Canvas(out_path)

    text = c.beginText(100, 750)
    c.setFont("Helvetica", 15)

    for line in text_lines:
        text.textLine(line)
    c.drawText(text)

    c.save()

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    out_path = r"pdf\book_pdfs\test.pdf"
    create_pdf(out_path, owner = "me")

if __name__ == '__main__':
    main()