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

cursor = conn.cursor()        # 创建游标
query1 = 'select * from departments order by dep_id'
#query2 = 'desc departments'
#cursor.execute(query2)
#result4 = cursor.fetchall()
cursor.execute(query1)
#print(result4)
result = cursor.fetchone()
print(result)
print('-' * 30 )
result2 =  cursor.fetchmany(2)
print(result2)
print('-' * 30 )
result3 = cursor.fetchall()
print(result3)
cursor.close()
conn.close()

#  (1, 'HR')
#  ((2, '运维部'), (3, '开发部'))
#  ((4, '财务部'),)







