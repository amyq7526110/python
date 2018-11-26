
from urllib import request,error

url1 = 'http://127.0.0.1/abc/'  # 目录不存在
url2 = 'http://127.0.0.1/ban/'  # 目录无权限 700

try:
    html1 = request.urlopen(url1)
except error.HTTPError as e :
    print('错误',e)
try:
    html2 = request.urlopen(url2)
except error.HTTPError as e:
    print('错误',e)

# 错误 HTTP Error 404: Not Found
# 错误 HTTP Error 403: Forbidden