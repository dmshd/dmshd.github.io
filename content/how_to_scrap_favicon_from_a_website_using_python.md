Title: How to scrap favicon from a website using Python
Date: 2022-10-16 14:26
Category: Python tricks, automation and web scraping
Tags: python, web, favicon, scraping, article in english
Author: Daniel Muyshond
Summary: I was tired of having to manually download favicons from websites, so I made a small script to do it for me.
Lang: en
Translation: false

## The context of scraping favicons

During my work, I often have to initiate graphical themes for our clients and look for their assets (logo, favicon, etc.).
It doesn's take long time to connect to the website and download the favicon, but it's a bit boring to do it manually.
If it can be automated, why not?

## The script to scrap favicons

Here is the code snippet I just generated to scrap favicons from websites.
It takes a url as input and downloads the favicon in the current directory.

``` Python
"""
Scrap favicon asset from a website.
"""

import os
import sys
import urllib.request
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def scrap_favicon(url):
    """
    Scrap favicon from a website.
    """
    # Get the domain name
    domain_name = urlparse(url).netloc
    # Get the favicon url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_url = soup.find('link', rel='shortcut icon')['href']
    # Download the favicon
    urllib.request.urlretrieve(favicon_url, 'favicon' + '.ico')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 scrap_favicon.py <url>')
        sys.exit(1)
    url = sys.argv[1]
    scrap_favicon(url)
```

## Conclusion

I now have a script that scrap favicons from websites and so you are welcome to use or adjust it following your needs too.
