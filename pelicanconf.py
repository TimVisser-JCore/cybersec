AUTHOR = 'Tim Visser'
SITENAME = 'Cybersecurity Reference Guide'
SITEURL = 'https://cybersec.timvisser.nl'
THEME = 'themes/pelican-alchemy/alchemy'

PATH = 'content'

STATIC_PATHS = ['images']

RFG_FAVICONS = True

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

HIDE_ARCHIVES = True
HIDE_CATEGORIES = True
HIDE_AUTHORS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Repository (Github)", "https://github.com/TimVisser-JCore/cybersec"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
