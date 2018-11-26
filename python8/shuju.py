
from urllib import request
import  webbrowser

url = 'http://www.baidu.com/s?wd=' + request.quote('你好')
webbrowser.open_new_tab(url)
# https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD

#  数据编码
#  •  一般来说,URL标准中只会允许一部分ASCII字符,
#  比如数字、字母、部分符号等
#  •  而其他的一些字符,比如汉字等,>是不符合URL标
#  准的。此时,我们需要编码。
#  •  如果要进行编码,可以使用urllib.request.quote()进
#  行
#  >>> urllib.request.quote('helloworld!') 
#  'hello%20world%21'  
#  >>> urllib.request.unquote('hello%20world%21')  
#  'helloworld!'   

# HTTP异常处理
# •  如果访问的页面不存在或拒绝访问,程序将抛出异常
# •  捕获异常需要导入urllib.error模块
# >>> html=   urllib.request.urlopen('hep://172.40.50.116/a.html')    
# urllib.error.HTTPError: HTTP(Error404:  NotImplementedFound
# >>> html=   urllib.request.urlopen('hep://172.40.50.116/aaa')   
# urllib.error.HTTPError: HTTP(Error403:  Forbidden
