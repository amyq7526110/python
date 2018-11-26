import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 回答yes
ssh.connect('192.168.1.70')  # ,username = root ,password = '123456'
a = ssh.exec_command('useradd zhangsha; id zhangsha;id lisi')
print(len(a))
print(a[1].read())
print(a[2].read())


ssh
ssh.close()

# 3
# b'uid=1000(zhangsha) gid=1000(zhangsha) groups=1000(zhangsha)\n'
# b"useradd: user 'zhangsha' already exists\nid: lisi: no such user\n"