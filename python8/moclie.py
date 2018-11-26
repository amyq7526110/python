
from urllib import request
import re
import os
# 模拟客户端
# •  有些网页为了防止别人恶意采集其信息所以进行了一
# 些反爬虫的设置,而我们又想进行爬取
# •  可以设置一些Headers信息(User-Agent),模拟
# 成浏览器去访问这些网站
# import urllib.request
#


def get_file(url,dest_fname):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'cookie':"Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542781160,1542785050,1542799910,1542801754; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542803902,1542803925,1542803937,1542804262; TMOOC-SESSION=DBBE3DE2CD42412DBE8198C1E04D2589; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542804243; sessionid=DBBE3DE2CD42412DBE8198C1E04D2589|E_bfuijdf; JSESSIONID=13845A7077A14678E775D4E83E7DA3DF; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542804262; isCenterCookie=yes; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae"}
    req = request.Request(url, headers=header)
    html = request.urlopen(req)
    with open(dest_fname,'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    return dest_fname

def guolv(dest_fname,charset='utf8'):
    with open(dest_fname,'r',encoding=charset) as fobj:
        d = []
        cpatt = re.compile(r'(http|https)://[\w./-]+\.html')
        for line in fobj:
        #    print(line)
            m = re.search(cpatt,line)
            if m:
                d.append(m.group())
  #              print(m.group())
        return d
if __name__ == '__main__':
   #get_file('http://tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ADMIN/DAY01/CASE/01/index.html','/root/tedu/a.html')
    # url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    #     'cookie': 'TMOOC-SESSION=2652A4C8E5074B9C82E6D7B767FB87F1; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1541981899,1542423997,1542623366,1542781177; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542787335; sessionid=2652A4C8E5074B9C82E6D7B767FB87F1|E_bfuijdf; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; JSESSIONID=9C3EAFE4451EEB1E7B880F7026969F58; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542623378,1542629465,1542781185,1542787342; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542787419; isCenterCookie=yes'}
    # req = request.Request(url, headers=header)
    # html = request.urlopen(req)
    # with open('a.html', 'w', encoding='utf-8') as f:
    #     f.write(html.read().decode('utf-8'))
 #   get_file('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%89%E5%9B%BD%E5%BF%97','/tmp/zg.html')
    x = guolv('a.html')

    print(x)

   # get_file('http://tts.tmooc.cn/ttsPage/LINUX/NSDTN201801/ADMIN/DAY01/CASE/01/index.html','/root/tedu/b.html')













#url='hep://www.tedu.cn' 
#hearder={   
#  'User-Agent':'Mozilla/5.0(X11;  Fedora; Linuxx86_64)    AppleWebKit/
#537.36(KHTML,   likeGecko)  Chrome/58.0.3029.110Safari/537.36'  
#}   
#html=urllib.request.Request(url,headers=header) 
#data=urllib.request.urlopen(request).read() 













