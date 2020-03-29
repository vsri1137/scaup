def main ():
    for page in pages:
        apply_template(page["filename"],page["output"])


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
   

def apply_template(content,output):  # interate through pages list and extract content
    template = open("templates/base.html").read() # reads in template with top/bottom html
    content_middle = open(content).read() 
    finished_page = replacer(template,placeholder="{{placeholder}}",replace_content=content_middle)
    open(output, "w+").write(finished_page)

def replacer(original,placeholder,replace_content):
    finished_page = original.replace(placeholder,replace_content)
    return finished_page

main()