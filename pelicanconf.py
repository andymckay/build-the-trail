AUTHOR = 'Andy McKay'
SITENAME = 'Build the Trail'
SITEURL = 'https://andymckay.github.io/build-the-trail/'


PATH = 'content'
THEME = 'themes/Papyrus'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'search', 'neighbors']

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index':None,'tag':None,'category':None,'author':None,'archives':24,}

SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
TOC = {}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)

DEFAULT_PAGINATION = False
FAVICON_URLS = (
    ('icon', 'images/icon.svg'),
)

SHOW_BREADCRUMBS = False
SHOW_SUBSCRIBE = False