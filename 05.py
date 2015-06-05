## python 3.4
"""
Python의 구조체들을
disk에 읽고 쓸 수 있는
[pickle] module을 이용하여
banner.p파일을 읽어들여서
파일내용을 화면에 출력하는 문제
"""
import pickle

banner = pickle.load(open("banner.p","rb"))

for j in banner:
    for i in j:
        ## i[0]:문자열 , i[1]:숫자
        ## 문자열*숫자 = 숫자만큼 문자열반복
        print("".join(i[0]*i[1]),end="")
    print("")
