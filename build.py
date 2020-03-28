top = open("templates/top.html").read() 
bottom = open("templates/bottom.html").read()
content = [            
    "index.html",
    "about.html",
    "blog.html",
    "projects.html",
]

for page in content:
    middle_content = open("content/"+page).read() #opens each html in list, stores content for middle
    combined_html = top + middle_content + bottom
    open("docs/"+page,"w+").write(combined_html) #writes concatenated content to new file
