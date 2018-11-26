from bs4 import  BeautifulSoup as bs
from urllib import request
import re
import os
import  time
# with open('a.html') as fobj:
#     data = fobj.read()
# soup = BeautifulSoup(data, 'html.parser')
# # print(soup.prettify())
# for link in soup.find_all('a'):
#     print(link.get('href'))
def get_urls(url,baseurl,urls,header):
    req = request.Request(url, headers=header)
    with request.urlopen(req)  as f:
        data = f.read().decode()
    #    print(data)
        link = bs(data, 'html.parser').find_all('a')
        for i in link:
            suffix = i.get('href')
 #           print(suffix)
            # if suffix == '#' or suffix == '#carousel-example-generic' or 'javascript:void(0);' in suffix:
            #      continue
            # else:
            childurl = baseurl +  str(suffix)
            if childurl not in urls:
                urls.append(childurl)
    try:
        urls.pop(urls.index('javascript:;'))
        urls.pop(urls.index('None'))
        urls.pop(urls.index('javascript:void(0);'))
        urls.pop(urls.index('javascript:void(0)'))
    except ValueError:
        print()
    print(urls)
    return urls
def getallUrl(url, baseurl, urls,header):
    get_urls(url, baseurl, urls,header)
    end = len(urls)
    start = 0
    while(True):
        if start == end:
            break
        for i in range(start, end):
            get_urls(urls[i], baseurl, urls,header)
            time.sleep(1)
        start = end
        end = len(urls)

def mkdipath(basedir,helf):
    l = re.compile(r'tts.*')
    for i in helf:
        m = re.search(l,i)
        if m:
            dir_name = basedir + os.path.dirname(m.group())
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
def get_file(basedir,helf,header):
    l = re.compile(r'tts.*')
    h = re.compile(r'http:.*')
    #print(helf)
    try:
        helf.pop(helf.index('javascript:;'))
        helf.pop(helf.index('None'))
        helf.pop(helf.index('javascript:void(0);'))
        helf.pop(helf.index('javascript:void(0)'))
    except ValueError:
        print()
    # print(helf)
    for i in helf:
        print('%s' %  i)
        req = request.Request(i,headers=header)
        html = request.urlopen(req)
        #print(html.read())
        patt = re.compile(r'tts.*')
        m = re.search(patt,i)
        dest_fname = basedir + m.group()
        # print(dest_fname)
        with open(dest_fname,'wb') as f:
            while True:
                data = html.read(4096)
                if not data:
                    break
                f.write(data)
        #html = request(i)
        # m = re.search(l,i)
        # url = re.search(h,i)
        # print(url.group())
        # if url:
        #     html = request.urlopen(url.group())
        # if m :
        #     print(m.group())
        #     dest_fname = basedir + m.group()
        #     with open(dest_fname,'wb') as fobj:
        #          while True:
        #             data = html.read(4096)
        #             if not data:
        #                break
        #             fobj.write(data)
if __name__ == '__main__':
    url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'cookie':"Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542785050,1542799910,1542801754,1542845000; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542804274,1542845022,1542845029,1542846595; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae; TMOOC-SESSION=E43CCEEF31E1428C9C43C3FAC7CB7A7D; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542846570; sessionid=E43CCEEF31E1428C9C43C3FAC7CB7A7D|E_bfuijdf; JSESSIONID=8321C59B3F2CAAA3CD83BF135E164DB7; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542846595; isCenterCookie=yes"
        }
    baseurl = ''
    urls = []

    y = get_urls(url,baseurl,urls,header)

    get_file('/root/tedu/',y,header)

    #     #mkdipath('/root/tedu/',y)
    # url = 'http://tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ADMIN/DAY01/CASE/01/index.html'
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    #     'cookie':"Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542781160,1542785050,1542799910,1542801754; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542803902,1542803925,1542803937,1542804262; TMOOC-SESSION=DBBE3DE2CD42412DBE8198C1E04D2589; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542804243; sessionid=DBBE3DE2CD42412DBE8198C1E04D2589|E_bfuijdf; JSESSIONID=13845A7077A14678E775D4E83E7DA3DF; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542804262; isCenterCookie=yes; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae"}
    # req = request.Request(url, headers=header)
    # m = request.urlopen(req)
    # print(m)



