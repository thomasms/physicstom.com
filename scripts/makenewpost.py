import os
import time

# blog details
entry_name = "noifs"
long_title = "I don't like ifs"

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
date: "2021-01-13T21:52:24.284Z"
readtime: 4 mins
tags: ['software', 'SOLID', ']
---

Content here....
'''.format(long_title)
    )



