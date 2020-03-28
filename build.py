def main():
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


pages = [
    {
        "filename" : "content/index.html",
        "output" : "docs/index.html",
        "title" : "Home",
    }   
    {
        "filename" : "content/about.html",
        "output" : "docs/about.html",
        "title" : "About me",
    }
    {
        "filename" : "content/blog.html",
        "output" : "docs/blog.html",
        "title" : "Blog",
    }
    {
        "filename" : "content/projects.html",
        "output" : "docs/projects.html",
        "title" : "Projects",
    }

]




main()
