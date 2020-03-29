def main ():
    for page in pages: #loop function
        build_page(page["filename"],page["output"],page["title"]) 


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
   
#this shit sorta works
# def build_page(content_page,output,title):      # interate through pages list and extract content
#     template = open("templates/base.html").read() # reads in template with top/bottom html
#     content_middle = open(content_page).read()
#     finished_page = replacer(content_page,placeholder="{{placeholder}}",replace_content="content_middle")
#     new_title = replacer(finished_page,placeholder="{{title}}",replace_content=title)
#     open(output, "w+").write(finished_page) 

def build_page(content_page,output,title):     
    template = open("templates/base.html").read() 
    template_replace = replacer(template,"{{title}}",title)
    content_middle = open(content_page).read()
    finished_page = replacer(template_replace,"{{placeholder}}",content_middle)
    open(output, "w+").write(finished_page+"alpha") 


def replacer(original_content, placeholder, replace_content):
    finished = original_content.replace(placeholder,replace_content)
    return finished


main()