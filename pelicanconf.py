#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# from markdown.extensions.codehilite import CodeHiliteExtension
# from markdown.extensions.toc import TocExtension

SITENAME = "Aditia A. Pratama"
DOMAIN = 'aditia.pawitra.id'
BIO_TEXT = 'Co-Founder and Technical Director at <a href="http://pawitrastudio.com">Pawitra Studio</a>. CG Instructor, Developer from Bandung, Indonesia.'
FOOTER_TEXT = '<i class="octicon octicon-code"></i> with <i class="octicon octicon-heart"></i> | Powered by <a href="http://getpelican.com">Pelican</a>'

SITE_AUTHOR = 'Aditia A. Pratama'
TWITTER_USERNAME = '@aditia_ap'
GOOGLE_PLUS_URL = ''
INDEX_DESCRIPTION = 'Random Thoughts and Technical Notes from Aditia A. Pratama, a Technical Director, CG instructor and  developer from Bandung, Indonesia.'

SIDEBAR_LINKS = [
            ('/', 'Home', 'octicon octicon-home'),
            ('/about/', 'About', 'octicon octicon-repo'),
            ('/commit-logs', 'Commit Logs', 'bf bf-blender'),
            ('/archive/', 'Archive', 'octicon octicon-file-zip')
        ]

ICONS_PATH = 'images/icons'

GOOGLE_FONTS = [
        "Raleway:400,700",
        "Inconsolata",
        ]

SOCIAL_ICONS = [
            ('mailto:aditia@pawitra.id', 
                'Email (aditia@pawitra.id)', 
                'fa-envelope'),
            ('http://twitter.com/aditia_ap', 
                'Twitter', 
                'fa-twitter'),
            ('http://github.com/aditiapratama', 
                'GitHub',
                'fa-github'),
            ('/atom.xml', 
                'Atom Feed', 
                'fa-rss'),
        ]

THEME_COLOR = '#455A64'

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
DIRECT_TEMPLATES = ['index', 
                    'archives']
CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True
PYGMENTS_STYLE = 'monokai'
MARKDOWN = {
        'extension_configs':{
            'markdown.extensions.admonition':{},
            'markdown.extensions.fenced_code':{},
            'markdown.extensions.codehilite': {'linenums': True},
            'markdown.extensions.extra':{}
            },
        'output_format': 'html5',
        }
# MD_EXTENSIONS = [
#     CodeHiliteExtension(css_class='highlight'),
#     TocExtension(permalink=True),
#     'markdown.extensions.extra',
# ]

GOOGLE_ANALYTICS = 'UA-80719674-1'

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images', 
                'uploads', 
                'extra']
IGNORE_FILES = ['.DS_Store', 
                'main.css', 
                'pneumatic.scss', 
                'pygments.css', 
                'main.scss', 
                '_octicons.scss', 
                '_variables.scss', 
                'css', 
                'js-dev']

extras = ['CNAME', 
        'favicon.ico', 
        'keybase.txt', 
        'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % file: {'path': file} for file in extras}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets',
            'neighbors',
            'render_math',
            'pelican_youtube']
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
