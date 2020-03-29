def main ():
    template = open("templates/base.html").read() # reads in template with top/bottom html
    apply_template("content/index.html","docs/index.html",template)


pages = [  # list with metadata on pages
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About me",
    },
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Blog",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
]
   

def apply_template(content,output, template):  # interate through pages list and extract content
    content = open(content).read() 
    finished_page = template.replace("{{placeholder}}",content)
    open(output, "w+").write(finished_page + "trash")

main()