import readtime
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
BLOG_DIR = os.path.join(BASE_DIR, 'content', 'blog')
BLOG_FILE = "index.md" 

entries = []
for d, sd, _ in os.walk(BLOG_DIR):
    for dir in sd:
        with open(os.path.join(BLOG_DIR, dir, BLOG_FILE), 'rt') as file:
            contentasstr = file.read()
        entries.append((dir, readtime.of_markdown(contentasstr)))

for e, t in entries:
    print("{:>50}:".format(e), t)
