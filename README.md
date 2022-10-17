# dmshd.github.io

My GitHub Pages website is using Pelican and Github-Pages to generate a static website.

## Usage

1. init a venv and activate it
2. pip install -r requirements.txt
3. pelican --listen --autoreload --port 8181
4. open http://localhost:8181


## TODO / Ideas

- [ ] Actually convert markdown images to raw proper responsive html tags with srcset.
- [ ] Document does not have a meta description
- [ ] 6 links does not have descriptive text
- [ ] Ship <code> css only when code is present ?

## TODO (already done)

- [*] Custom 404 page https://docs.getpelican.com/en/stable/tips.html#id1. DONE. See 404.html in gh-pages branch.
- [*] Search about "insert raw html in markdown pelican". DONE. Might be easier with RST or need to use a plugin.

### Notes

`ghp-import output -n -b gh-pages --cname=CNAME`
`pelican content -o output -s publishconf.py;ghp-import output -n -b gh-pages --cname=www.impavi.de;git checkout gh-pages`
