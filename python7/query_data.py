#!/usr/bin/env python3
from dbcccc  import Departments,Session

session = Session()

# 创建映射类的实例
# •  创建实例时,并不会真正在表中添加记录

#query2 = session.query(Departments.dep_id,Departments.dep_name)
#print(query2)
#for dep in query2:
#    print(dep)
#    print('%s -> %s') % (dep.dep_id,dep.dep_name)
#for dep_id,dep_name in query2:

# query3 = session.query(Departments.dep_name.label('部门'))
# print(query3)
# for dep in query3:
#     print(dep.部门)

# query4 = session.query(Departments).order_by(Departments.dep_id)
# print(query4)
# for dep in query4:
#     print(dep)
#     print('%s -> %s' % (dep.dep_id,dep.dep_name))

# query5 = session.query(Departments).order_by(Departments.dep_id)[1:3]
# print(query5)
# for dep in query5:
#     print(dep)
#     print('%s -> %s' % (dep.dep_id,dep.dep_name))


# query6 = session.query(Departments).filter(Departments.dep_id==3)
# print(query6)
# for dep in query6:
#     print('%s  -> %s'  % (dep.dep_id,dep.dep_name))

# 结果过滤(续1)
#    filter()函数可以叠加使用

# query7 = session.query(Departments).filter(Departments.dep_id>=2) \
#     .filter(Departments.dep_id<=4)
# print(query7)
# for dep in query7:
#     print('%s  -> %s'  % (dep.dep_id,dep.dep_name))
# query8 = session.query(Departments).filter(~Departments.dep_name.in_(['人事部','财务部']))
# print(query8)
# for dep in query8:
#     print('%s  -> %s'  % (dep.dep_id,dep.dep_name))

# query9 = session.query(Departments).filter(Departments.dep_name.in_(['人事部','财务部']))
# print(query9)
# for dep in query9:
#     print('%s  -> %s'  % (dep.dep_id,dep.dep_name))

from sqlalchemy import and_,or_

# query10 = session.query(Departments)\
#     .filter(and_(Departments.dep_id>=2,Departments.dep_id<=4))
# query11 = session.query(Departments)\
#     .filter(or_(Departments.dep_id==2,Departments.dep_id==4))
# for dep in query10:
#     print(dep.dep_id,dep.dep_name)
# print('-' * 30)
# for dep in query11:
#     print(dep.dep_id,dep.dep_name)

# query11 = session.query(Departments)
# print(query11)
# for i in query11.all():  # 返回列表 全部数据
#     print(i.dep_id,i.dep_name)
# print(query11.first())  # 返回第一条q\
#
# query12 = session.query(Departments.dep_id,Departments.dep_name).filter(Departments.dep_id>4)
# print(query12.one()) # one()取出所有记录,如果不是一条记录则抛出异常
# print(query12.scalar()) # •  scalar()调用one(),返回第一列的值
#SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name FROM departments
# [<dbcccc.Departments object at 0x7fdafc31d588>, <dbcccc.Departments object at 0x7fdafc31d5f8>, <dbcccc.Departments object at 0x7fdafc31d668>, <dbcccc.Departments object at 0x7fdafc31d6d8>, <dbcccc.Departments object at 0x7fdafc31d748>]



# query13 = session.query(Departments).count()
# print(query13)
# query14 = session.query(Departments)
# print(query14.count())

from dbcccc import Employees

# zmg = Employees(
#     emp_id=20,
#     emp_name='赵明钢',
#     gender='男',
#     birth_date='1993-12-20',
#     phone='13123121236',
#     email='zmg@tedu.cn',
#     dep_ip=2
# )
#
# zxx = Employees(
#     emp_id=21,
#     emp_name='朝夕相',
#     gender='男',
#     birth_date='1999-12-20',
#     phone='13123441236',
#     email='zxx@tedu.cn',
#     dep_ip=5
# )
# session.add_all([zxx,zmg])
# session.commit()
# 多表查询
# •  通过join()方法实现多表查询
query15 = session.query(Employees.emp_name,Departments.dep_name)\
    .join(Departments,Employees.dep_ip==Departments.dep_id)
print(query15.all())

 # query 括号中先写Employees.emp_name,join 的括号中就要写Departments
 # query 括号中先写Departments.dep_name,join 的括号中就要写Employees



#  常用过滤操作符
#  •  相等
#  query.filter(Employees.name=='john')
#  •  不相等
#  query.filter(Employees.name!='john')
#  •  模糊查询
#  query.filter(Employees.name.like(' %j '))常用过滤操作符(续1)
#  •  in
#  query.filter(new_emp.name.in_(['bob', 'john'])
#  •  not in
#  query.filter(~new_emp.name.in_(['bob', 'john'])
#  •  字段为空
#  query.filter(new_emp.name.is_(None))
#  •  字段不为空
#  query.filter(new_emp.name.isnot(None))常用过滤操作符(续2)
#  •  多重条件and
#  from sqlalchemy import and_
#  query.filter(and_(new_sal.basic>=10000,
#  new_sal.extra>=2000))
#  •  多重条件or
#  from sqlalchemy import or_
#  query.filter(or_(new_sal.basic>=10000,
#  new_sal.extra>=3000))


session.close()

#  查询操作基本查询
#  •  通过作用于session的query()函数创建查询对象
#  •  query()函数可以接收多种参数
#  frommyormimportSession, Departments
#
#  session=    Session()
#
#  forinstancein
#  session.query(Departments).order_by(Departments.dep_id):
#                  print(instance.dep_id,  instance.dep_name)  使用ORM描述符进行查询
#  •  使用ORM描述符进行查询
#  •  返回值是元组
#  frommyormimportEmployees,   Session(
#
#  session=    Session()
#
#  forname,    phone2numeric(insession.query(Employees.name,   Employees.phone):
#                  print(name, phone)  使用命名元组
#  •  查询对象返回的是一个命名元组
#  •  名称是类的名字,或是类中属性的名字
#  frommyormimportSession, Departments
#
#  session=    Session()
#
#  forrowinsession.query(Departments,Departments.dep_name):
#                  print(row.Departments,  row.dep_name)


#  修改显示字段名
#  •  显示的字段名可以通过label()函数进行修改
#  frommyormimportSession, Departments
#
#  session=    Session()
#
#  forrowinsession.query(Departments.dep_name.label('部门')):
#                  print(row.部门) 排序
#  •  通这order_by()函数可以实现按指定字段排序
#  frommyormimportSession, Departments
#
#  session=    Session()
#
#  forinstancein
#  session.query(Departments).order_by(Departments.dep_id):
#                  print(instance.dep_id,  instance.dep_name)



#  提取部分数据
#  •  通过“切片”的方式,实现部分数据的提取
#  from myorm import Session, Departments
#
#  session=Session()
#
#  for row in  session.query(Departments,  Departments.dep_name)[2:5]:
#       print(row.Departments,  row.dep_name)

#  结果过滤
#   •  通过filter()函数实现结果过滤



















