def main():
    # top = open("templates/top.html").read() 
    # bottom = open("templates/bottom.html").read()
    template = open("templates/base.html").read()

    pages = [
        {
            "filename" : "content/index.html",
            "output" : "docs/index.html",
            "title" : "Home",
        } ,  
        {
            "filename" : "content/about.html",
            "output" : "docs/about.html",
            "title" : "About me",
        },
        {
            "filename" : "content/blog.html",
            "output" : "docs/blog.html",
            "title" : "Blog",
        },
        {
            "filename" : "content/projects.html",
            "output" : "docs/projects.html",
            "title" : "Projects",
        },

    ]

    for page in pages:
        middle_content = open(page["filename"]).read() #read from pages list
        finished_page = template.replace("{{placeholder}}",middle_content) + "test"
        open(page["output"], "w+").write(finished_page) #writes concatenated content to new file

main()
