import os
from datetime import datetime

# blog details
entry_name = "epics"
long_title = "The epic software controlling an accelerator near you"

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
title: {0}
date: "{1}"
readtime: 4 mins
tags: ['software', 'physics']
---

Content here....
'''.format(long_title, datetime.now().isoformat())
    )



