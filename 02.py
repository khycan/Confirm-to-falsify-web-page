## python 3.4
"""
페이지 source에 들어있는
특정 문자열을 추출하는 문제
"""
import urllib.request as ur
import re

html = ur.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

source = html.read()

source = source.decode('utf-8')

source = source[source.find("<!--\n%%$"):]

source = re.sub("[^a-zA-Z0-9]","",source)

print (source)
