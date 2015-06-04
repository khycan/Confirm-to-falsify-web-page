## python 3.4

import urllib.request as ur
import re

html = ur.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

source = html.read()

source = source.decode('utf-8')

source = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",source))

print (source)
