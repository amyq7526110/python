#!/usr/bin/env python3

  #  简化除法判断
try: 
    num = float(input('请输入一个除数: '))
    result = 100  / num 
except (EOFError,KeyboardInterrupt):
    print('bye-bye')
except (ValueError):
    print('请你输入一个数字') 
except (ZeroDivisionError):
    print('0不能是除数')
else: 
    print(result)
finally:
    print('done')
