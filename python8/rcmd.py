import  paramiko
import  sys
import  getpass
import  re
import  threading
import  os
def rcmd(host,username='root',password=None,cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=username,password=password)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT: %s' % (host,out.decode()))
    if err:
        print('[%s] ERR: %s' % (host,err.decode()))
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage  %s  ipfile cmd '  % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    # host = '192.168.1.70'
    if not os.path.isfile(ipfile):
        print('no such file',ipfile )
        exit(2)
    password = getpass.getpass('Password= ')
    cmd = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = re.compile(r'(\d{1,3}.){3}\d{1,3}')
            ip = re.search(ip,line)
            if not ip:
                continue
            t = threading.Thread(target=rcmd,args=(ip.group(),'root',password,cmd))
            t.start()


    #rcmd(ip.group(), password=password, cmd=cmd)
    # [192.168.1.70] OUT: uid=1000(zhangsha) gid=1000(zhangsha) groups=1000(zhangsha)
    # cmd = 'id zhangsan'
    # [192.168.1.70] ERR: id: zhangsan: no such user
