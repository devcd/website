#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Too'
SITENAME = u'Python User Group Chengdu'
SITEURL = u'http://dev:8001'

PATH = u'content'
STATIC_PATHS = ['img', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = u'Asia/Shanghai'

DEFAULT_LANG = u'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# DELETE_OUTPUT_DIRECTORY = True

# ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_URL = '{slug}.html'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
# PAGE_SAVE_AS = 'kb/{slug}/index.html'



THEME = "/Users/too/ws/pycd/pelican-bootstrap3"
BOOTSTRAP_THEME = "paper"
BOOTSTRAP_FLUID = False


DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh-cn': '%-m 月 %-d 日, %Y',
}
