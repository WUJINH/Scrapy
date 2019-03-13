import requests, time, threading, re
from urllib import request

Problem = []

def parse_page(url):
    global Problem
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    request.urlretrieve(url, 'html/1.hmtl')
    text = response.text
    reTable = re.compile(r'<table.*?>(.*?)</table>', re.S)
    reScript = re.compile(r'<script language="javascript">(.*?)</script>', re.S)
    reP = re.compile(r'p\(.*?"(.*?)".*?\);',re.S)
    rePid = re.compile(r'p\(\d,(\d{4}).*?\);',re.S)

    tbody = re.findall(reTable, text)[2]
    Scriptx = re.findall(reScript, tbody)[0]
    title = re.findall(reP, Scriptx)
    pid = re.findall(rePid,Scriptx)
    for x, y in zip(title, pid):
        problem = {
            'title': x,
            'url': 'http://acm.hdu.edu.cn/showproblem.php?pid=%d'%int(y)
        }
        Problem.append(problem)




def main():
    for x in range(1, 5):
        url = 'http://acm.hdu.edu.cn/listproblem.php?vol=%d' % x
        parse_page(url)
    for x in Problem:
        print(x)


if __name__ == '__main__':
    main()
