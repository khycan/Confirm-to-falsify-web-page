## python 3.4

import pickle

banner = pickle.load(open("banner.p","rb"))

for j in banner:
    for i in j:
        ## i[0]:문자열 , i[1]:숫자
        ## 문자열*숫자 = 숫자만큼 문자열반복
        print("".join(i[0]*i[1]),end="")
    print("")
