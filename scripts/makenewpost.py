import os
import time

# blog details
entry_name = "linemeetsplane"
long_title = "When a line meets a plane"

# default parameters
BLOG_FILE = "index.md"
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
BLOG_DIR = os.path.join(BASE_DIR, 'content', 'blog')

# make the directory for the entry
# we should really check if it exists already first...
new_dir = os.path.join(BLOG_DIR, entry_name)
os.mkdir(new_dir)

# make the starting post
with open(os.path.join(new_dir, BLOG_FILE), 'wt') as bf:
    bf.write(
'''---
title: {}
date: "2019-01-19T22:12:03.284Z"
readtime: 10 mins
tags: []
---

Content here....
'''.format(long_title)
    )



