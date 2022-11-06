Title: How to prind out text from a generated pdf file in Python with pdfplumber
Date: 2022-10-16 14:20
Category: Python tricks, automation and web scraping
Tags: pdfplumber, pdf, python, automation, text extraction, pdf text extraction, pdf text extraction python, pdf text extraction python pdfplumber, article in english
Author: Daniel Muyshond
Summary: How to print out text from a generated pdf file in Python with pdfplumber
Lang: en
Translation: false

## How to print out text from a generated pdf file in Python with pdfplumber

### The context of me need to extract text from a pdf

I would like to extract the data from my account statements in PDF.

After searching, it seems that [pdfplumber](https://github.com/jsvine/pdfplumber) is strong enough to extract the text from generated pdf.

Here's a quick try with [a sample pdf file I found on the web](https://static.societegenerale.fr/pri/PRI/Repertoire_par_type_de_contenus/Fichier_a_telecharger/nouveau-releve-compte.pdf).

### The code I just generated to extract text from a pdf

Here is a small code snippet I just made to print out text from a generated pdf file in Python with pdfplumber :

``` python
"""
Takes a pdf file prints out the text of it
"""

import pdfplumber
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='pdf file to extract text from', required=True)
    args = parser.parse_args()
    pdf_file = args.file
    if not os.path.exists(pdf_file):
        print('File does not exist')
        sys.exit(1)
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            print(page.extract_text())

if __name__ == '__main__':
    main()
```

## Conclusion

I now have all the text printing in the terminal.

All that would be left to do is to identify the lines corresponding to the transactions (at first sight starting with a date and containing numbers, perhaps confirming with `startswith()` or a neat regex and you have the beginnings of a trick to classify your transactions.
