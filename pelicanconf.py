#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'devcd.io'
SITENAME = u'DevCD 成都开发者'
SITEURL = u'http://dev:8001'

PATH = u'content'
STATIC_PATHS = ['img', 'files', 'extra/CNAME']
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
OUT_LINKS = (('蠎周刊', 'http://weekly.pychina.org', '主要翻译 Pycoder\'s Weekly（关于 Python 的信息)'),
         ('CDLUG', 'https://groups.google.com/group/cdlug_community', '成都 Linux 用户组，要翻墙，你懂的'),
         ('V2EX', 'https://v2ex.com', '国内有名的技术论坛, Python 气息浓厚'),)

# Social widget
SOCIAL = (('QQ 群号 312412351', 'http://qun.qzone.qq.com/group#!/312412351/home', 'qq'),
          ('Github', 'https://github.com/devcd'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# DELETE_OUTPUT_DIRECTORY = True

# ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_URL = '{slug}.html'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
# PAGE_SAVE_AS = 'kb/{slug}/index.html'



THEME = "pelican-bootstrap3"
# BOOTSTRAP_THEME = "readable"
BOOTSTRAP_THEME = "simplex"
# BOOTSTRAP_FLUID = True


DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh-cn': '%-m 月 %-d 日, %Y',
}


PLUGIN_PATHS = ["plugins", "plugins"]
PLUGINS = ['tag_cloud',]
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = "tags.html"
TAG_CLOUD_MAX_ITEMS = 10
