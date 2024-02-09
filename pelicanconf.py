AUTHOR = 'Tim Visser'
SITENAME = 'Cybersecurity Handbook'
SITEURL = ""
THEME = "themes\\pelican-alchemy\\alchemy"

HIDE_AUTHORS = True
HIDE_DATE = True
HIDE_CATEGORY = True

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Cybersecurity Handbook Repo", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True