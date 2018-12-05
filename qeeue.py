#!/usr/bin/env python3
import  requests
import  os
import  re

# r = requests.get('http://www.baidu.com/link?url=AiTyGn50zm757-ZueNloTQeOfVHy1UkHeeRafklarVtLI3ACFMhnrCd2X3Zi_EsoVWhMu8TJueuf-cumDmP3ncGb6-by2l-q2sy9GlnZRMg-x26KKWL3Jnn4ovuMMgW_Zb3rNNXh39YytQCyNRXAb6AvMUh1e_uvyMfATq2L-riri4cFFEj54JOgWAyLCFz2jMNg8w8s1iQhDLtgrm8vzPYuJsslghKyNEtb6P3Z4OQxNNKyqKjFogYM0q1JjgO-PzGp4fGcPee0tyYgsYqQ-bWW8IS6smSslliEDeDFBuCCuL40KuBub8eaXOzc536lvzLK4W6ZMll92B--ax6ADpBQ66rdCpLDj9Kb07qEJjxLsiMI_f9zzFdfHALgHFa6Zs_q4zAMFjpxkV-nkYBt8bRM78Mf_X2VH4pMUI1H4u1U34Q3ZlpcL1_HojJ0RURMtDqVUUhcqGRWpHggaBC1iidnR5aXBueixUEL4FDl9HAsAlYt5xUH61ka1zLYXzz7xzqmnfsVRaGYkYnuFMlu_62qD_vriiaFE6FK5AQ-9ty&wd=&eqid=b66c39500001dcd5000000065bf6256f')
# with open('/tmp/1.jpg','wb') as f:
#     f.write(r.content)
# r = requests.get('http://127.0.0.1/')
# print(r.text)
#
# r = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
# print(r.encoding)
# r.encoding = 'utf8'
# print(r.json())
#
#
# r = requests.get('http://www.tmooc.cn/')
# r.encoding = 'utf8'
#r.cookieshttp://tts.tmooc.cn/studentCenter/toMyttsPage',cookies=

#  r = requests.get('http://www.baidu.com/s',params=param)
# with open('/tmp/by.html','wb') as fobj:
#     fobj.write(r.content)
#param = {'wd':'python'}
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'cookie': "Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542801754,1542845000,1542867493,1542868072; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542865719,1542867526,1542867533,1542868085; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae; TMOOC-SESSION=E6BC42E5EAF54743A86BAE22DA5ADDBF; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542868072; sessionid=E6BC42E5EAF54743A86BAE22DA5ADDBF|E_bfuijdf; JSESSIONID=95AF19C6550D2CC9B5E41B7D8201EA49; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542868085; isCenterCookie=yes"
}
# cookie="Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542799910,1542801754,1542845000,1542867493; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542862878,1542863880,1542865719,1542867526; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae; TMOOC-SESSION=C5BEDF4D93564E5B9C94DA2CA7F40C0B; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542867493; sessionid=C5BEDF4D93564E5B9C94DA2CA7F40C0B|E_bfuijdf; JSESSIONID=E1B1C89273C0E5E50EE831AA741DD875; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542867526; isCenterCookie=yes"
url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
r = requests.get(url,headers=header)
print(r.text)
print(r.status_code)
print(requests.codes.ok)
print(requests.codes.not_found)
print(requests.codes.forbidden)


def usr_ans(src_dir,header):
    ht = re.compile('tts.*')
    for path,folders,files in os.walk(src_dir):
        print(path)
        m  = re.search(ht,path)
        if m:
            usr = 'http://' + m.group() + '/index_answer.html'
            r = requests.get(usr,headers=header)
            if r.status_code == requests.codes.ok:
                dest_name = path + '/index_answer.html'
                with open(dest_name,'wb') as f:
                    f.write(r.content)
if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'cookie': "Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1542801754,1542845000,1542867493,1542868072; cloudAuthorityCookie=0; versionListCookie=NSDTN201801; defaultVersionCookie=NSDTN201801; versionAndNamesListCookie=NSDTN201801N22NLinux%25E4%25BA%2591%25E8%25AE%25A1%25E7%25AE%2597%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06; courseCookie=LINUX; stuClaIdCookie=611127; tedu.local.language=zh-CN; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1542865719,1542867526,1542867533,1542868085; UM_distinctid=167364767713e3-0b61b296f4480b-38694646-1fa400-167364767723ae; TMOOC-SESSION=E6BC42E5EAF54743A86BAE22DA5ADDBF; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1542868072; sessionid=E6BC42E5EAF54743A86BAE22DA5ADDBF|E_bfuijdf; JSESSIONID=95AF19C6550D2CC9B5E41B7D8201EA49; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1542868085; isCenterCookie=yes"
    }
    usr_ans('/tmp/tedu',header)




