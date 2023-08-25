import urllib.request 

# copy the image url 
url = "http://stuffpoint.com/nature/image/43322-nature-sandy-wallpaper.jpg"

# download the image 
download = urllib.request.urlretrieve(url, "myimage.jpg")


