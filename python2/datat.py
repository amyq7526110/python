#!/usr/bin/env python3

from datetime import datetime,timedelta

#  datetime模块方法
#  •  datetime.today():返回一个表示当前本地时间的
#  datetime对象
#  •  datetime.now([tz]):返回一个表示当前本地时间的
#  datetime对象,如果提供了参数tz,则获取tz参数
#  所指时区的本地时间
#  •  datetime.strptime(date_string, format):将格式
#  字符串转换为datetime对象
#  •  datetime.ctime(datetime对象):返回时间格式字
#  符串
#  •  datetime.strftime(format):返回指定格式字符串

dt = datetime.now()
print(dt.year)                    # 2018
print(dt.month)                   # 11
print(dt.day)                     # 13
print(dt + timedelta(days=100))  # 2019-02-21 16:51:36.993828
print(dt - timedelta(days=100))   # 2018-08-05 16:51:36.993828
                                  

print(datetime(2050, 6, 10, 20, 41, 20, 106546))

# 2050-06-10 20:41:20.106546







