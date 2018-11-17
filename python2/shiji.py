#!/usr/bin/env python3

import time 

#  时间表示方式
#  •  时间戳timestamp:表示的是从1970年1月1日
#  00:00:00开始按秒计算的偏移量

#  •  UTC(Coordinated Universal Time,世界协调时)
#  亦即格林威治天文时间,世界标准时间。在中国为
#  UTC+8。DST(Daylight Saving Time)即夏令时

#  •  元组(struct_time):由9个元素组成

print(time.time())


#  struct_time元组
#  索引 属性 值
#  0 tm_year 2000
#  1 tm_mon 1-12
#  2 tm_mday 1-31
#  3 tm_hour 0-23
#  4 tm_min 0-59
#  5 tm_sec 0-61
#  6 tm_wday 0-6(0表示周一)
#  7 tm_yday(一年中的第几天) 1-366
#  8 tm_isdst(是否为dst时间) 默认为-1

print(time.localtime())  # 当前时间九元组


#  time模块方法
#  •  time.localtime([secs]):将一个时间戳转换为当前
#  时区的struct_time。secs参数未提供,则以当前时
#  间为准
#  •  time.gmtime([secs]):和localtime()方法类似,
#  gmtime()方法是将一个时间戳转换为UTC时区(0
#  时区)的struct_time
#  •  time.time():返回当前时间的时间戳
#  •  time.mktime(t):将一个struct_time转化为时间戳


print(time.localtime(0))
print(time.time())      #  1542097699.2568095


#  time.struct_time(tm_year=2018, tm_mon=11, tm_mday=13, tm_hour=16, tm_min=28, tm_sec=19, tm_wday=1, tm_yday=317, tm_isdst=0)
#  time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

#  time模块方法(续1)
#  •  time.sleep(secs):线程推迟指定的时间运行。单
#  位为秒
#  •  time.asctime([t]):把一个表示时间的元组或者
#  struct_time表示为这种形式:‘Sun Jun 20
#  23:21:05 1993’。如果没有参数,将会将
#  time.localtime()作为参数传入
#  •  time.ctime([secs]):把一个时间戳(按秒计算的浮
#  点数)转化为time.asctime()的形式
print(time.asctime())                     # Tue Nov 13 16:31:44 2018
print(time.ctime(1542097699.2568095))     # Tue Nov 13 16:28:19 2018
print(time.ctime(0))                      # Thu Jan  1 08:00:00 1970


#   time模块方法(续2)
#   •  time.strftime(format[, t]):把一个代表时间的元
#   组或者struct_time(如由time.localtime()和
#   time.gmtime()返回)转化为格式化的时间字符串。
#   如果t未指定,将传入time.localtime()
#   •  time.strptime(string[, format]):把一个格式化时
#   间字符串转化为struct_time。实际上它和
#   strftime()是逆操作
#   time.str_ime('%Y-%m-%def%X',time.localtime())	


# 时间样式

# 格式         含义
# %A           本地完整星期名称
# %a           本地简化星期名称 
# %b           本地简化月份名称 
# %p           本地am或者pm的相应符
# %B           本地完整月份名称 
# %S           秒(01-61)
# %c           本地相应的日期和时间 
# %U           一年中的星期数(00–53,星期日是一个星期的开始)
# %d           一个月中的第几天(01-31)
# %w           一个星期中的第几天(0-6,0是星期天)
# %H           一天中的第几个小时(24小时制,00-23)  
# %x           本地相应日期
# %I           第几个小时(12小时制,01-12)         
# %X           本地相应时间
# %j           一年中的第几天(001-366) 
# %y           去掉世纪的年份(00-99)
# %Z           时区的名字 
# %Y           完整的年份
# %m           月份(01-12)
# %M           分钟数(00-59)


# yiyibooks.cn


