#!/usr/bin/env python3
import pymysql

# 连接数据库
#     创建连接是访问数据库的第一步
#  连接数据库的参数
conn = pymysql.connect(
host = '192.168.1.51',
port = 3306,
user = 'root',
passwd = 'Azsd1234.',
db = 'nsd1806',
charset = 'utf8'
)

# 游标
# •  游标(cursor)就是游动的标识
# •  通俗的说,一条sql取出对应n条结果资源的接口/句柄,就
# 是游标,沿着游标可以一次取出一行

cur = conn.cursor()        # 创建游标
query1 = 'select * from departments order by dep_id'
cur.execute(query1)
cur.scroll(1,mode='absolute')
result = cur.fetchall()
print(result)
cur.scroll(0,mode='absolute') 
# cur.scroll(1,mode='relative')  # 默认是相对的移动
result1 = cur.fetchone()
print(result1)
cur.close()
conn.close()





