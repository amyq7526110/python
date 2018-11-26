#  JSON概述

#  •  JSON(JavaScript Object Notation) 是一种轻量级
#  的数据交换格式
#  •  易于人阅读和编写,同时也易于机器解析和生成
#  •  基于JavaScript Programming Language
#  •  JSON采用完全独立于语言的文本格式,但是也使用
#  了类似于C语言家族的习惯(包括C, C++, C#, Java,
#  JavaScript, Perl, Python等)
#  •  这些特性使JSON成为理想的数据交换语言


#  JSON结构
#  •  JSON主要有两种结构
#  –  “键/值”对的集合:python中主要对应成字典
#  –  值的有序列表:在大部分语言中,它被理解为数组

#  Python        JSON
#  dict          object
#  list,tuple    array
#  str           string
#  int,float     number
#  True          true
#  False         false
#  None          null

#  dumps方法

#  •  对编码后的json对象进行decode解码,得到原始数据,
#  需要使用的json.loads()函数
#  >>> importjson
#  >>> numberer=   json.dumps(100) 
#  >>> json.loads(number)  
#  100loads方法
#  •  使用简单的json.dumps方法对简单数据类型进行编码
#  >>> importjson
#  >>> json.dumps(100) 
#  '100'   
#  >>> json.dumps([1,  2,  3]) 
#  '[1,    2,  3]' 
#  >>> json.dumps({'name': 'zzg'}) 
#  '{"name":   "zzg"}' 
