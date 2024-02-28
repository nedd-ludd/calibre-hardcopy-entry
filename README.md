# Calibre Hardcopy Entry
A tool to add and represent hardcopies on the Open Source Calibre library software.
<!-- TODO: Remove add metadata -->
<!-- TODO: Check what packages are used -->
<!-- TODO: What recreation steps for pipenv-->
<!-- TODO: -->
<!-- TODO: -->
<!-- TODO: -->
<!-- TODO: -->
## Contents

[Project Overview](#project-overview) |
[Getting Started](#getting-started) |
[Testing](#testing) |
[Project Brief & Timeframe](#project-brief) |
[Technologies Used](#technologies-used) |
[Result](#result) |
[Development Lifecycle](#development-lifecycle) |
[Wins](#wins) |
[Challenges](#challenges) |
[Bugs & Future Improvements](#bugs-and-future-improvements) |
[Key Learnings](#key-learnings) |


## Project overview

Calibre is an open-ebook management system, for which, this project enables adding records for physical copies. It relies on libib (another opensource library management app) for use of its barcorde scanner and .csv export function. Once .csv file has been exported a placeholder .pdf is created to be imported into calibre along with book info.

Calibre has a useful metadata function that can "fill in the blanks" of ISBNs, publisher info etc to make a comprehensive record if there is missing info.

The project then has a secondary function to stamp "HARDCOPY" and "Owner's" for a certain owner, on the .jpg file represented in the calibre package. This enables distinguising 


## Getting Started

To recreate this project please do the following:

### Have pre-requisites

- Libib account
- Download Calibre 

### Follow Steps

- Clone or download the this repo:

```
git@github.com:nedd-ludd/calibre-hardcopy-entry.git
```
- Install Calibre
- Download libib app on mobile device.
- Create collection on libib
- Scan in book barcodes and export .csv
- Create .env file with the following variables:
    - "INCOMING_CSV="
    - "DUMP_PDFS="
    - "CALIBRE_LIBRARY_PATH="
    - "CALIBRE_DB_PATH="
    - "USER_1_TAG=" ... 2, 3, -> n as appropriate
    - "OWNER_TAG="
- Create folder for pdfs and add to DUMP_PDFS
- Add location of Calibre Library, Calibre sqlite db to .env vars
- Add user name to user tag in .env
- Add name of ownder to .env

# Technologies Used

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-bottom: 1px solid #ddd;">Operating Systems</td>
      <td style="border-bottom: 1px solid #ddd;">
        <ul>
          <li>Windows</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="border-bottom: 1px solid #ddd;">Languages / Formats / Packaging</td>
      <td style="border-bottom: 1px solid #ddd;">
        <ul>
          <li>Python</li>
          <li>csv</li>
          <li>pip</li>
          <li>pip env</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="border-bottom: 1px solid #ddd;">Python</td>
      <td style="border-bottom: 1px solid #ddd;">
        <ul>
          <li>reportlab</li>
          <li>pypdf</li>
          <li>Pillow</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="border-bottom: 1px solid #ddd;">Code Editors</td>
      <td style="border-bottom: 1px solid #ddd;">
        <ul>
          <li>Visual Studio Code</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="border-bottom: 1px solid #ddd;">Project Management / Version Control</td>
      <td style="border-bottom: 1px solid #ddd;">
        <ul>
          <li>GitHub</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>



Two scripts:
ingest_hardcopies.py
*calibre add book actions here*
modify_covers.py

Future Improvements
USER_?_TAG and OWNER_TAG not DRY, they represent same data and are two places to make changes. Neet to combine as one, maybe have user input as "Name" for name of ownder in pdf, then can add "'s" for ownership stamp on cover.