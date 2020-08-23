#!/use/bin/env python

import sys # parsing command line
from urllib.parse import urlparse # used for the path
from tld import get_tld # used for the TLD, Domain and Hostname.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = sys.argv[1]           #https://www.askpython.com/python-programming
parsed = urlparse(url)

#URL part
res = get_tld( url , as_object=True)
tldPrint = str(res)
print('TLD: ' + tldPrint)       #com
domainPrint =res.domain +'.'+ tldPrint      
print('DOMAIN: ' + domainPrint)     #askpython.com
hostnamePrint = res.subdomain + '.' + domainPrint
print('HOSTNAME: ' + hostnamePrint)     #www.askpython.com
print('PATH: ' + parsed.path)       #/python-programming  
print('LINKS:\n\t Same hostname:\n')

# Obtaining the links
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
links = [] 
for link in soup.find_all('a'):
    links.append(link.get('href'))

linksSameHostname = []
for x in links:
    res2 = get_tld( x , as_object=True)
    tldPrint2 = str(res2)
    hostnamePrint2 = res2.subdomain + '.' + res2.domain +'.'+ tldPrint2 
    if hostnamePrint2 == hostnamePrint:         # hostname comparison 
        linksSameHostname.append(x)

for c in linksSameHostname:
    print(c)
    
print()
linksSameDomain = []
for p in links:
    res3 = get_tld( p , as_object=True)
    tldPrint3= str(res3)
    domainPrint2 = res3.domain +'.'+ tldPrint3  
    if domainPrint2 == domainPrint:         # Domain comparison 
        linksSameDomain.append(p)

print('Same domain:\n')
for o in linksSameDomain:
    print(o)
    
print()
linksDifferentDomain = []
for q in links:
    res4 = get_tld( q , as_object=True)
    tldPrint4= str(res4)
    domainPrint3 = res4.domain +'.'+ tldPrint4 
    if domainPrint3 != domainPrint:         # Domain comparison 
        linksDifferentDomain.append(q)

print('Different domain:\n')
for o in linksDifferentDomain:
    print(o)
