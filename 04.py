## python 3.4
"""
페이지에 명시되어 있는
nothing 파라미터의 값을 추적하는 문제
"""
import urllib.request as ur
import re

nothing = "12345"
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

while True:
    text = ur.urlopen(base_url+nothing).read()
    text = text.decode('utf-8')

    print(text)

    try :
        nothing = "".join(re.findall("[\d]+",text)[-1])
    except :
        if bool(re.search("Yes+",text)) :     ##text : Yes. Divide by two and keep going
            nothing = str(int(nothing)/int(2))
            continue
        break
