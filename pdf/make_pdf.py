#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
import os
from reportlab.pdfgen import canvas

def create_pdf(out_path):
    c = canvas.Canvas(out_path)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Hello, World!")
    c.save()

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    out_path = r"pdf\book_pdfs\test.pdf"
    create_pdf(out_path)

if __name__ == '__main__':
    main()