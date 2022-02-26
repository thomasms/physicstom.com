import os
from datetime import datetime

# blog details
entry_name = "prime_units"
long_title = "Prime units"
readtime = 3
tags = ["physics", "units"]

# default parameters
BLOG_FILE = "index.md"
BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
BLOG_DIR = os.path.join(BASE_DIR, "content", "blog")

# make the directory for the entry
# we should really check if it exists already first...
new_dir = os.path.join(BLOG_DIR, entry_name)
if os.path.isdir(new_dir):
    raise RuntimeError(
        f"Entry with name: {entry_name} already exists. Choose another name!"
    )

os.mkdir(new_dir)

# make the starting post
with open(os.path.join(new_dir, BLOG_FILE), "wt") as bf:
    tag_str = "[" + ",".join([f"'{t}'" for t in tags]) + "]"
    bf.write(
        f"""---
title: {long_title}
date: "{datetime.now().isoformat()}"
readtime: 3 mins
tags: {tag_str}
---

Content here....
"""
    )
