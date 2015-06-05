## python 3.4
"""
zipfile module을 이용하여
.zip파일을 열어서 각 파일 목록에 있는
'설명' 칼럼의 문자열을 모아서 출력하는 문제
"""
import zipfile
import re

nothing = "90052"
comment = ""

zf = zipfile.ZipFile("channel.zip","r")

while True :
    text = zf.read(nothing+".txt").decode("utf-8")
    print(text)
    info = zf.getinfo(nothing+".txt")
    char = info.comment.decode("utf-8")
    if char != " " and char != "*":
        comment += char

    try :
        nothing = "".join(re.findall("[\d]+",text)[-1])
    except :
        break
        

print(comment)
