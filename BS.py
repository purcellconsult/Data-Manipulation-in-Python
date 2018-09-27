from bs4 import BeautifulSoup

with open("site.html", "r") as f:
    
    tags = f.read()
    soup = BeautifulSoup(tags, 'html')
       
    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)
