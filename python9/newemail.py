import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getpass
# 邮件正文 纯文本 字符编码
def inetmail(msg,subject,sender,receivers,server,username,password):
    message = MIMEText(msg,'plain','utf8')  # 正文
    message ['From'] = Header(sender,'utf8')           # 收件人
    message['To'] = Header(receivers[0],'utf8')     # 主题
    message['Subject'] = Header(subject,'utf8')             #  发件人
    smtp = smtplib.SMTP()
    smtp.connect(server,port=25)
    smtp.starttls()
    smtp.login(username,password)
    sender = sender
    receivers = receivers
    smtp.sendmail(sender,receivers,message.as_string())

if __name__ == '__main__':
    sender = 'm13268275527@163.com'
    receivers = [ 'm13268275527@163.com' ]
    msg = 'python 测试\n'
    username = 'm13268275527@163.com'
    passwd = getpass.getpass('Password= ')
    subject = '测试邮件'
    inetmail(msg,subject,sender,receivers,'smtp.163.com',username,passwd)

