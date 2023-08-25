import urllib.parse 
# take any url 
url = "http://www.dreamtechpress.com:80/engieering/computer-science.html"

# get the tuple with parse of the url 
tpl = urllib.parse.urlparse(url)

# display the content of the tuple
print(tpl)

# display different part of the url 
print("Scheme= ", tpl.scheme)
print("Net Location= ", tpl.netloc)
print("Path= ", tpl.path)
print("Parameters= ", tpl.params)
print("port number= ", tpl.port)
print("Total url= ", tpl.geturl()) 

