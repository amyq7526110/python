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
delete1 = 'delete from departments where dep_id=%s'
data = (1,)
cur.execute(delete1,data)
conn.commit()
cur.close()
conn.close()




