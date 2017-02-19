#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ray Alez'
SITENAME = 'Digital Mind'
SITEURL = '' # 'http://blog.digitalmind.io'

PATH = 'content'
STATIC_PATHS = [
    'static/portfolio.html',    
    'static/.htaccess',
    'static/CNAME',
    'images',
     ]


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml' #None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Menu
MENUITEMS = [# ('Browse', '/articles'),
             # ('Projects', '/projects'),
             ('Resources', 'http://webacademy.io'),
             ('Community', 'http://hackertribe.io'),
             ('About', '/about'),
             # ('Portfolio', '/portfolio'),                          
] # ('Portfolio', '/portfolio'),

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = 'post/{slug}'
ARTICLE_SAVE_AS = 'post/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

# Index as sub page.
# Looks like only index lists posts, so I need to save another template as index. Weird.
# INDEX_SAVE_AS = 'posts.html'
# HOME_SAVE_AS = 'index.html'
# INDEX_SAVE_AS = 'blog/index.html'
# INDEX_URL = 'blog/'

# TAG_URL = 'tag/{slug}/'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# TAGS_URL = 'tags/'
# TAGS_SAVE_AS = 'tags/index.html'

# PAGINATION_PATTERNS = (
#     (1, '{base_name}/posts/', '{base_name}/index.html'),
#     (2, '{base_name}/posts/{number}/', '{base_name}/posts/{number}/index.html'),
#)

# List a template here to generate it.
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives','projects','art','portfolio','portfolio_back', 'home',) #'about' #'home',

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

THEME = "/home/ray/projects/digitalmind/blog/themes/digitalmind"
# THEME = "/home/ray/projects/digitalmind/themes/orangemind"

# Plugins
PLUGIN_PATHS = ['/home/ray/projects/digitalmind/blog/pelican-plugins']
# PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.include_code', 'liquid_tags.notebook']

# for syntax highlighting
EXTRA_HEADER = open('_nb_header.html').read() #.encode('utf-8')
