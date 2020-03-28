#!/bin/bash

cat templates/top.html content/index.html templates/bottom.html > docs/index_combined.html
cat templates/top.html content/blog.html templates/bottom.html > docs/blog_combined.html
cat templates/top.html content/project.html templates/bottom.html > docs/project_combined.html
cat templates/top.html content/about.html templates/bottom.html > docs/about_combined.html
