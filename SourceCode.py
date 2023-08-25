import urllib.request

# store the url of the page into file object 
file = urllib.request.urlopen("https://www.python.org/")

# read data from file and display 
print(file.read())


