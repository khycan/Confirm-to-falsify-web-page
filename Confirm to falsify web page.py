# Pyhon 3.4
"""
zerocert.org에 POST방식으로 요청하여
결과값을 얻는 프로그램
"""
import http.client
import urllib.parse
import multiprocessing as mp
import re
from datetime import datetime
import time

def Scan_URL(url, number, log_name, lk):

    ## HTTP packet parameters (for zerocert)
    params = '&pattern=&referer=&proxy=&port=&code=&chk_level=1&language=ko&uagent=msie&work=malware'
    # 함수인자로 넘겨받은 URL을 패킷파라미터에 붙임.
    params = 'url=' + url + params

    ## HTTP packet headers (for zerocert)
    headers = {"Host":"zerocert.org","Connection": "keep-alive", "Content-Length": "102", "Accept": "*/*", "Origin": "http://zerocert.org", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Referer": "http://zerocert.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4", "Cookie": "PHPSESSID=3br5er2i010bpvnctedoqt2sa7"}

    ## try to connect to zerocert and wait untill recieving response
    conn = http.client.HTTPConnection("zerocert.org")

    while True:
        conn.request("POST","/tools/sitecheck.html",params,headers)
        response = conn.getresponse()
        ## check omission
        if response.status == 500:    # 500 에러가 날 경우 request를 다시 보냄 
            print(response.status, response.reason)
            time.sleep(2.0)
        else:
            break
    
    data = response.read()
    result_str = data.decode('utf-8','ignore')

    ## output 문자열 추출 (Extract string)
    result_str = result_str[result_str.find('<b>Latest detected Domain</b>'):]
    result_str = result_str[:result_str.find('Relation domain')]
    result_str = re.sub("<.[a-zA-Z]*>","",result_str)
    result_str = re.sub("<t.*>","",result_str)
    result_str = result_str.replace("Latest detected Domain","")

    while True:
        # lock을 건다
        acquired = lk.acquire()
        try:
            if acquired == True:
                f = open(log_name,'a')
                f.write('<p>'+str(number)+' '+url+'</br>')
                f.write(result_str)
                f.write('</p>')
            else:
                # lock을 실패할 경우 1초 멈춤
                time.sleep(2.0)
        except:
            print("Error Occurred")
        finally:
            if acquired == True:
                # lock을 해제
                lk.release()
                break

    f.close()
    conn.close()
    print(str(number)+' finished')
    return

if __name__ == '__main__':

    ## After judge your input, it control stream of program
    while 1:
     a = input('Scan URLs? (y/n) :')
     if a=='y':
      break
     elif a=='n':
      print("Exit program. bye!")
      exit()
     else :
      print("It is not valid. Please, try again.\n")
     continue

    # lock 객체 생성
    lock = mp.Lock() ## for synchronization

    # 프로그램 실행날짜를 얻음(로그파일명)
    today = datetime.now()
    log_name = str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + str(today.hour) + '-' + str(today.minute)
    log_name = log_name + '.html'
    
    fh = open('list_of_homepage(origin).txt', 'r')
    ct=0
    while 1:
     ct=ct+1
     line = fh.readline()
     if not line : break
     urls = line
     p = mp.Process(target=Scan_URL, args=(urls,ct,log_name,lock))  ## 다중 프로세스
     p.start()

    fh.close()
