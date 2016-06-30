#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Aditia A. Pratama"
DOMAIN = 'aditia.pawitra.id'
BIO_TEXT = 'Instructor  and Developer from Bandung, Indonesia.'
FOOTER_TEXT = '<i class="fa fa-code"></i> with <i class="fa fa-heart"></i> | Powered by <a href="http://getpelican.com">Pelican</a>'

SITE_AUTHOR = 'Aditia A. Pratama'
TWITTER_USERNAME = '@aditia_ap'
GOOGLE_PLUS_URL = ''
INDEX_DESCRIPTION = 'Website and Blog of Aditia A. Pratama, an instructor and  developer from Bandung, Indonesia.'

SIDEBAR_LINKS = [
            '<a href="/about/">About</a>',
            '<a href="/archive/">Archive</a>',
        ]

ICONS_PATH = 'images/icons'

GOOGLE_FONTS = [
        "Raleway:400,600",
        "Source Code Pro",
        ]

SOCIAL_ICONS = [
            ('mailto:aditia@pawitra.id', 'Email (aditia@pawitra.id)', 'fa-envelope'),
            ('http://twitter.com/aditia_ap', 'Twitter', 'fa-twitter'),
            ('http://github.com/aditiapratama', 'GitHub', 'fa-github'),
            ('/atom.xml', 'Atom Feed', 'fa-rss'),

        ]

THEME_COLOR = '#FFC107'

# Pelican Settings
RELATIVE_URLS = True
SITEURL = 'http://localhost'
TIMEZONE = 'Asia/Jakarta'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

THEME = 'pneumatic'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True
MD_EXTENSIONS = ['admonition', 'codehilite(linenums=True)', 'extra']

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 'uploads', 'extra']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

extras = ['CNAME', 'favicon.ico', 'keybase.txt', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
            ('cache', False),
            ('manifest', False),
            ('url_expire', False),
            ('versions', False),

]

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
