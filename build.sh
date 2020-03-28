#!/bin/bash

cat templates/top.html content/index.html templates/bottom.html > docs/index.html
cat templates/top.html content/blog.html templates/bottom.html > docs/blog.html
cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html
cat templates/top.html content/about.html templates/bottom.html > docs/about.html
