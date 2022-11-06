AUTHOR = 'Daniel Muyshond'
SITENAME = 'impavi.de'
SITEURL = 'http://localhost:8181'

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Archives (all articles)', 'http://localhost:8181/archives.html'),
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/')
)
LINKS_WIDGET_NAME = 'Links'

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/danielmuyshond/'),
    ('Twitter', 'https://twitter.com/_dmshd'),
    ('YouTube', 'https://www.youtube.com/c/DanielMuyshond'),
    ('Instagram', 'https://www.instagram.com/d.mshd_/')
)
SOCIAL_WIDGET_NAME = 'Social'

DEFAULT_PAGINATION = 7
THEME = 'themes/mycurrentidea'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'},}
