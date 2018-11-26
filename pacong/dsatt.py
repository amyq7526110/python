from bs4 import  BeautifulSoup as bs
from urllib import request
import re
import os
import  time
#import  requests
#with open('a.html') as fobj:
#with open('/root/tedu/tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ADMIN/DAY02/COURSE/ppt.html') as fobj:
# with open('/root/tedu/tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ADMIN/DAY02/CASE/01/index.html')  as fobj:
#     data = fobj.read()
# soup = bs(data, 'html.parser')
# # print(soup.prettify())
# for tag in soup.find_all(re.compile("link")):
#     print(tag.get('href'))
# for tag in soup.find_all(re.compile("img")):
#     print(tag.get('src'))
# for tag in soup.find_all(re.compile("script")):
#     print(tag.get('src'))
def get_cis(url,header,basedir):
    urls = []
    req = request.Request(url,headers=header)
    html = request.urlopen(req)
    data = html.read()
    soup = bs(data, 'html.parser')
    for tag in soup.find_all(re.compile("link")):
        l = tag.get('href')
        if l:
            urls.append(l)
    for tag in soup.find_all(re.compile("img")):
        l = tag.get('src')
        if l:
            urls.append(l)
    for tag in soup.find_all(re.compile("script")):
        l = tag.get('src')
        if l:
            urls.append(l)
  #  print(urls)
    for i in urls:
        ce = re.compile(r'^http.*')
        m  = re.search(ce,i)
        if m:
            mkfile(basedir,m.group())
            wq = request.Request(m.group(),headers=header)
            html1 = request.urlopen(wq)
            patt = re.compile(r'tts.*')
            x = re.search(patt,m.group())
            dest_fname = basedir + x.group()
            print(dest_fname)
            with open(dest_fname, 'wb') as f:
                while True:
                    data = html1.read(4096)
                    if not data:
                        break
                    f.write(data)
        else:
            newurl = os.path.dirname(url) + '/' + str(i)
            print(newurl)
            mkfile(basedir,newurl)
            nwq = request.Request(newurl,headers=header)
            html2 = request.urlopen(nwq)
            patt = re.compile(r'tts.*')
            x = re.search(patt,newurl)
            dest2_fname = basedir + x.group()
            print(dest2_fname)
            with open(dest2_fname, 'wb') as f:
                while True:
                    data = html2.read(4096)
                    if not data:
                        break
                    f.write(data)
def mkfile(basedir,url):
    l = re.compile(r'tts.*')
    m = re.search(l,url)
    if m:
        dir_name = basedir + os.path.dirname(m.group())
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
    return dir_name
def get_source(url,header,basedir):
    mkfile(basedir,url)
  # get_csjsimg(basedir,url,header)
    get_cis(url,header,basedir)
    req = request.Request(url,headers=header)
    html = request.urlopen(req)
    patt = re.compile(r'tts.*')
    m = re.search(patt, url)
    dest_fname = basedir + m.group()
    with open(dest_fname, 'wb') as f:
        while True:
            data = html.read(4096)
            if not data:
                break
            f.write(data)
    with request.urlopen(req)  as f:
        data = f.read()
        link = bs(data, 'html.parser').find_all('a')
        css = bs(data, 'html.parser').find_all('a')
        for i in link:
            suffix = str(i.get('href'))
            cpatt = re.compile(r'^http.*')
            out = re.search(cpatt,suffix)
            if out:
                get_source(suffix,header,basedir)
#def get_csjsimg(basedir,url,header):
    # urls = []
    # req = request.Request(url,headers=header)
    # with request.urlopen(req) as f:
    #     data = f.read()
    #     soup = bs(data, 'html.parser')
    #     for tag in soup.find_all(re.compile("link")):
    #          l = tag.get('href')
    #          if l :
    #              urls.append(l)
    #     for tag in soup.find_all(re.compile("img")):
    #         l = tag.get('src')
    #         if l:
    #              urls.append(l)
    #     for tag in soup.find_all(re.compile("script")):
    #         l = tag.get('src')
    #         if l:
    #              urls.append(l)
    #     print(urls)
    #     for i in urls:
    #         patt = re.compile(r'^http.*')
    #         m = re.search(patt,str(i))
    #         if m:
    #             get_source(m.group(),header,basedir)
    #         else:
    #             cis = os.path.dirname(url) + str(i)
    #             print(cis)
    #             req = request.Request(cis, headers=header)
    #             html = request.urlopen(req)
    #             mkfile(basedir,cis)
    #             patt = re.compile(r'tts.*')
    #             m = re.search(patt, cis)
    #             dest_fname = basedir + m.group()
    #             with open(dest_fname, 'wb') as f:
    #                 while True:
    #                     data = html.read(4096)
    #                     if not data:
    #                         break
    #                     f.write(data)
if __name__ == '__main__':
    url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
    # url = 'http://tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ENGINEER/DAY01/CASE/01/index.html'
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'cookie':"Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542785050,1542799910,1542801754,1542845000; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542862325,1542862332,1542862867,1542862878; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae; TMOOC-SESSION=E43CCEEF31E1428C9C43C3FAC7CB7A7D; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542854219; sessionid=E43CCEEF31E1428C9C43C3FAC7CB7A7D|E_bfuijdf; JSESSIONID=9BED8D1B4058269C8017F1AD0920122E; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542862878; isCenterCookie=yes"
    }
    basedir = '/tmp/tedu/'
    # get_cis(url,header,basedir)
    get_source(url, header, basedir)