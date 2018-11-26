#!/usr/bin/env python3

import requests
import os
import hashlib
import tarfile
from urllib import  request

def get_webdata(url):
    r = requests.get(url)
    return r.text

def download(url,fname):
    html = request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def deploy(app):
    os.chdir('/var/www/packages')
    tar = tarfile.open(app,'r:gz')
    tar.extractall()
    tar.close()
    src = app.replace('.tar.gz','')
    dst = '/var/www/html/mysite'
    if os.path.exists(dst):
        os.unlink(dst)
    os.symlink(src,dst)

def check_bb(live_fname,url):
    r = requests.get(url)
    a  = r.text.strip()
    if os.path.isfile(live_fname):
       with open(live_fname) as fobj:
           data = fobj.read().strip()
           if a   == data :
               return 'ok'
           else:
               return a
    else:
        return a

if __name__ == '__main__':

    live_fname='/var/www/deploy/live_version'
    live_url='http://192.168.1.12/deploy/live_version'
    live_bb = check_bb(live_fname,live_url).strip()
    print(live_bb)
    if live_bb == 'ok':
        print('不需要更新')
        exit(1)
    ver = get_webdata(live_url).strip()
    app_name = 'wpress_%s.tar.gz' % ver
    app_url =  'http://192.168.1.12/deploy/packages/' + app_name
    app_path = os.path.join('/var/www/packages',app_name)
    download(app_url,app_path)
    local_md5 = check_md5(app_path)
    remote_md5 = get_webdata(app_url + '.md5').strip()
    if local_md5 == remote_md5:
        with open(live_fname,'w') as fobj:
            fobj.write(live_bb)
        deploy(app_path)



