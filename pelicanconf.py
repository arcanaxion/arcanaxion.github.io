from pathlib import Path
import datetime as dt

AUTHOR = 'Zaccheus Sia'
SITENAME = 'Zaccheus'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disable caching when generating output
LOAD_CONTENT_CACHE = False

# Themes
# https://github.com/notcraig/Pelican-StartBootstrap-Agency
THEME = Path(__file__).parent / "Pelican-StartBootstrap-Agency"

SITETITLE = "Zaccheus Sia"  # (also used in menu navigation)
SITESUBTITLE = "Portfolio"
INTRO_LG = "Zaccheus Sia"  # (top line of landing page)
INTRO_SM = "A Portfolio"  # (second line of landing page)
PORTFOLIO_TITLE = "Portfolio" 
PORTFOLIO_SUBTITLE = "Projects I've worked on."
CURRYEAR = dt.datetime.now().year

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
