def main ():
    for page in pages: #loops through pages, you'll need to add every time you add to a page
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

def build_page(content_page,output,title):     
    template = open("templates/base.html").read() #reads in the base template
    template_replace = replacer(template,"{{title}}",title) #creates a temp version of template with title replaced
    content_middle = open(content_page).read() #reads in content
    finished_page = replacer(template_replace,"{{placeholder}}",content_middle) #replaces content from title-replaced template
    open(output, "w+").write(finished_page) #writes to an output file


def replacer(original_content, placeholder, replace_content): 
    finished = original_content.replace(placeholder,replace_content) #replaces old with new
    return finished

main()