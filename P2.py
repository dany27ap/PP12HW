listHtml = ["index.html", "home.html", "header.html"]

combinedFiles = ""

for file in listHtml:
    with open(file, "r") as html_file:
        data = html_file.read()
        html_file.close()
        combinedFiles += data[data.find("<body>")+7:data.find("</body>")-1] + "\n"

file_names = "\n".join(listHtml)

f = open("fisier.html", "w+")

f.write("<html>\n<head>\n%s\n</head>\n<body>\n%s</body>\n</html>" % (file_names, combinedFiles))

f.close()

