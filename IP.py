import socket 

# take the server name 
host = 'www.google.co.in'

try:
   # know the IP address  of the website
   addr = socket.gethostbyname(host)
   print("IP address= ", addr)
except socket.gaierror:
   print("The website does not exist") 
   
 
