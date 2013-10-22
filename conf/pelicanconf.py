#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Personal Info

AUTHOR = u'Tiago'
SITENAME = u"Network Padawan's ::1"
SITEURL = 'https://tiagoasousa.pt'
TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = u'en'
LOCALE = ('en_US.UTF-8')

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# Custom Feeds
FEED_ATOM = 'rss.xml'

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/networkpadawan'),
	  ('Linkedin', 'http://linkedin.com/in/tiagoasousa'),)

DEFAULT_PAGINATION = 10

#Comments
DISQUS_SITENAME = "tiagoasousa"
DISQUS_SECRET_KEY = u''
DISQUS_PUBLIC_KEY = u''

#Settings
THEME = '/root/peliboo'
PLUGIN_PATH = '/opt/blog/plugins'
PLUGINS = ['assets', 'pelican_youtube']
MD_EXTENSIONS = ['codehilite', 'extra', 'video']
MARKUP = ('rst', 'md')
PATH = '/root/blog/'
OUTPUT_PATH = '/var/www/'
ARTICLE_URL = '{date:%Y}/{date:%m}/{title}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{title}/index.html'
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_EXCLUDES = ('pages',)
PAGE_URL = 'pages/{title}.html'
PAGE_SAVE_AS = 'pages/{title}.html'
USE_FOLDER_AS_CATEGORY = False
ARCHIVES_URL = 'archives.html'
COPYRIGHT = 'Tiago Sousa, 2013'
DEFAULT_CATEGORY = 'blog'
DISPLAY_CATEGORIES_ON_MENU = 'False'
STATIC_PATHS = ["media", "stuff"]
