#!/usr/bin/env python3
from dbcccc  import Departments,Session

session =Session()

# 创建映射类的实例
# •  创建实例时,并不会真正在表中添加记录
hr = Departments(dep_id=1,dep_name='人事部')
ops = Departments(dep_id=2,dep_name='运维部')
dev = Departments(dep_id=3,dep_name='开发部')
devops = Departments(dep_id=4,dep_name='运维开发部')
finance = Departments(dep_id=5,dep_name='财务部')
deps = [ ops,devops,dev,finance ]
session.add(hr)
session.add_all(deps)
session.commit()
session.close()


