import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 邮件正文 纯文本 字符编码

message = MIMEText('python 邮件发送测试\n','plain','utf8')  # 正文
message ['From'] = Header('mhw@tedu.cn','utf8')           # 收件人
message['To'] = Header('m13268275527@163.com','utf8')     # 主题
message['Subject'] = Header('测试邮件','utf8')             #  发件人
smtp = smtplib.SMTP('localhost')
sender = 'mhw@tedu.cn'
receivers = ['m13268275527@163.com','root@localhost']
smtp.sendmail(sender,receivers,message.as_string())

#  邮件编程SMTP概述

#  •  SMTP(Simple Mail Transfer Protocol)即简单邮
#  件传输协议,使用TCP协议25端口
#  •  它是一组用于由源地址到目的地址传送邮件的规则,
#  由它来控制信件的中转方式
#  •  python的smtplib提供了一种很方便的途径发送电子
#  邮件。它对smtp协议进行了简单的封装


#  SMTP对象

#  •  Python发送邮件,第一步是创建SMTP对象
#  smtp_obj=   smtplib.SMTP([hosts[,   portal[,    local_hostname]]]   )   
#  •  创建SMTP对象也可以不给定参数,之后再通过对象
#  的其他方法进行绑定

#  设置邮件
#  •  标准邮件需要三个头部信息
#  –  From:发件人
#  –  To:收件人
#  –  Subject:主题

# sendmail方法
# •  Python SMTP 对象使用 sendmail 方法发送邮件
# SMTP.sendmail(from_addr,	to_addrs,	msg[,	mail_opPons,	rcpt_opPons])
# •  sendmail方法三个必须的参数有:
# –  收件人
# –  发件人
# –  消息主体msg是一个字符串,表示邮件

# sendmail方法(续1)
# •  将准备好的邮件发送
# sender	=	'from@runoob.com'
# receivers	=	['root@localhost']
# smtp_obj	=	smtplib.SMTP('localhost')
# smtp_obj.sendmail(sender,	receivers,	message.as_string())