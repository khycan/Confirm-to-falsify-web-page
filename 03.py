## python 3.4
"""
02번과 비슷하게
특정 url의 페이지 소스를 열어서
조건에 맞는 문자열을 추출하는 문제
"""
import urllib.request as ur
import re

html = ur.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

source = html.read()

source = source.decode('utf-8')

source = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",source))

print (source)
