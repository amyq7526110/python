#!/usr/bin/env python3
import  time 
import  os 
import  hashlib 
import  tarfile
import  pickle  as p

def md5file(fname):
    a = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            a.update(data)
    return a.hexdigest()

def filename(file_dir):
    md5zhi = {}
    for path,folders,files in os.walk(file_dir):
        x = [ path+'/'+i for i in files ]
        for key in x:
            values = md5file(key)
            md5zhi[key]  = values
    return md5zhi
def full_backup(src_dir,dst_dir,md5_file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()
    a  =  filename(src_dir)
    with open(md5_file,'wb') as wf:
         p.dump(a,wf)
def incr_backup(src_dir,dst_dir,md5_file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    newmd5  =  filename(src_dir)
    with open(md5_file,'rb') as wf:
         oldmd5 = p.load(wf)
    with open(md5_file,'wb') as wf:
         p.dump(newmd5,wf)
    tar = tarfile.open(fname,'w:gz')
    for i in newmd5:
            if i not in oldmd5:
                tar.add(i)
            else:
                if  newmd5[i] != oldmd5[i]:
                    tar.add(i)
    tar.close()
if __name__ == '__main__':

    src_dir =  '/root/tees'
    dst_dir =  '/tmp/backup/'
    md5_file =  '/tmp/backup/md5.data'

    if time.strftime('%a') == 'Mon':

        full_backup(src_dir,dst_dir,md5_file)

    else:

        incr_backup(src_dir,dst_dir,md5_file)
  
