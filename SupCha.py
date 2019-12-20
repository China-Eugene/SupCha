#_*_ coding:utf-8 _*-
# Python 3.6
#
# SupCha v1.0
# Author:Eugene

import requests
import json
import re


banner = '''
  ____               ____ _           
 / ___| _   _ _ __  / ___| |__   __ _ 
 \___ \| | | | '_ \| |   | '_ \ / _` |
  ___) | |_| | |_) | |___| | | | (_| |
 |____/ \__,_| .__/ \____|_| |_|\__,_|
             |_|

Manual:
1.Information
2.Subdomain
3.Whois
4.Port

0.Exit

----------------Tell me your needs----------------
'''

headers={
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
}
cookies = {"UM_distinctid":"16f1e25f3fd323-038a47f9ee79e2-5701732-144000-16f1e25f3fe853","CNZZDATA1277897461":"1260803527-1576758801-https%253A%252F%252Fblog.csdn.net%252F%7C1576758801"}

#Information from bugscaner (Verification code appears in multiple requests in a short period of time)
def Cms():
    url = input("Please input url：")
    print("Wait for...\n")
    first = requests.post("http://whatweb.bugscaner.com/what.go",  headers=headers, data = {"url":url}, timeout=10)
    a = json.loads(first.text)
    try:
        for k,v in a.items():
            print(k+' : '+str(v))
    except Exception as e:
        print(e)
        print("Maybe your IP is screened😳")

#Subdomain from dnsscan
def Subdomain():
    url = input("Please input url(Example:baidu.com)：")
    print("Wait for...")
    try:
        Second = requests.post("https://www.dnsscan.cn/dns.html", headers=headers, cookies=cookies, data = {"ecmsfrom":'8.8.8.8', "show":'none', "keywords":url}, timeout=10)
        b = Second.text
        pattern = re.compile( r'rel="nofollow" target="_blank">(.*?)</a></td>')
        domain = re.findall(pattern,b)
        try:
            for subdomain in domain:
                print('\n'+subdomain,end="")
        except:
            print('\n'"No found Subdomain")
    except:
        print('\n'"Error")

#Whois from aite
def Whois():
    url = input("Please input url：")
    print("Wait for...")
    try:
        Third = requests.get("https://whois.aite.xyz/?ajax&domain={}".format(url), headers=headers ,timeout=10)
        c = Third.content
    except:
        print("You can check proxy server..\n")
        return
    # 正则匹配
    try:
        r_name = r'Registrant: (.*?)<br />'
        r_email = r'Registrant Contact Email: (.*?)<br />'
        r_idc = r'Sponsoring Registrar: (.*?)<br />'
        # 以utf-8编码输出
        name = re.findall(r_name,c.decode('utf-8'))
        email = re.findall(r_email, c.decode('utf-8'))
        idc = re.findall(r_idc, c.decode('utf-8'))
        print('\n' + 'Url:' + url + '\n' + 'Registrant:' + name[0] + '\n' + 'Email:' + email[0] + '\n' + 'IDC:' + idc[0])
    except:
        print('\n'"The website has opened a privacy screen") #信息隐藏判断

#Port from fofa
def Port():
    url = input("Please input ip：")
    print("Wait for...")
    try:
        Fourth = requests.get("https://fofa.so/hosts/{}".format(url), headers=headers, timeout=10)
        d = Fourth.text
    except:
        print("Site is dead!!!\n")
        return
    #正则匹配
    r_port = r'<i class="label"><a href="#port_link_(.*?)">'
    port = re.findall(r_port, d)
    print('\n'"Port: ",end="")
    for i in port:
        print(i+'  ',end="")
#


#----------------------------------------------------------------------start----------------------------------------------------------------------

if __name__ == '__main__':
    print(banner)
    while 1:
        userneed = input('\n' + 'Please enter a code：')
        if userneed == '0' :
            print('\n'"Bye~~")
            break #退出
        elif userneed == '1' :
            Cms()
        elif userneed == '2' :
            Subdomain()
        elif userneed == '3':
            Whois()
        elif userneed == '4':
            Port()