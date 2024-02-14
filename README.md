# calibre-hardcopy-entry
processes .csv from Libib for hardcopy entry in Calibre

utilises libib barcode scanning and .csv export to represent physical copies of books then to be added to calibre open source database

uses blank book pdfs to represent physical copy of books

packages:
reportlab
pypdf

Pillow - image modification

Two scripts:
ingest_hardcopies.py
*calibre add book actions here*
modify_covers.py