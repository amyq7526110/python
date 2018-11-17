#!/usr/bin/env python3

#   异常

#   什么是异常
#   •  当python检测到一个错误时,解释器就会指出当前
#   流已经无法继续执行下去,这时候就出现了异常
#   •  异常是因为程序出现了错误而在正常控制流以外采取
#   的行为
#   •  这个行为又分为两个阶段:
#   –  首先是引起异常发生的错误
#   –  然后是检测(和采取可能的措施)阶段

#   python中的异常
#   •  当程序运行时,因为遇到未解的错误而导致中止运行,
#   便会出现traceback消息,打印异常
#   异常 描述
#   NameError           未声明/初始化对象
#   IndexError          序列中没有没有此索引
#   SyntaxError         语法错误
#   KeyboardInterrupt   用户中断执行
#   EOFError            没有内建输入,到达EOF标记
#   IOError             输入/输出操作失败

try:
   num = int(input('number: '))
   result = 100 / num 
except (ValueError,ZeroDivisionError):
   print('Invalid input')
except (KeyboardInterrupt,EOFError):
   print('\nBye-bye')
else:
   print(result)
finally:
   print('Done')

#   try-except语句
#   •  定义了进行异常监控的一段代码,并且提供了处理异
#   常的机制
#   带有多个expect的try语句
#   •  可以把多个except语句连接在一起,处理一个try块
#   中可能发生的多种异常

#   异常参数
#   •  异常也可以有参数,异常引发后它会被传递给异常处
#   理器
#   •  当异常被引发后参数是作为附加帮助信息传递给异常
#   处理器的

#   else子句
#   •  在try范围中没有异常被检测到时,执行else子句
#   •  在else范围中的任何代码运行前,try范围中的所有代
#   码必须完全成功

#   finally子句
#   •  finally子句是无论异常是否发生,是否捕捉都会执行
#   的一段代码
#   •  如果打开文件后,因为发生异常导致文件没有关闭,
#   可能会发生数据损坏。使用finally可以保证文件总是
#   能正常的关闭
