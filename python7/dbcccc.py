#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import  sessionmaker



# 数据库对象管理连接mysql
# •  通过create_engine实现数据库的连接
engine = create_engine(
    # mysql+pymsyql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:Azsd1234.@192.168.1.51/tedu1806?charset=utf8',
    encoding='utf8',
 #   echo = True  # 开启日志输出 默认为false

)
# 声明映射
# •  当使用ORM的时候,配置过程从描述数据库表开始
# •  通过自定义类映射相应的表
# •  通过声明系统实现类映射
# •  首先通过声明系统,定义基类
# 创建会话类
# •  ORM访问数据库的句柄被称作Session
Session  = sessionmaker(bind=engine)
Base = declarative_base()
# 创建映射类
# •  一旦创建了基类,就可以创建自定义映射类了

class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True,nullable=False)
    # 创建架构
    # •  类构建完成后, 表的信息将被写入到表的元数据

#   __repr__ 是可选项
    def __str__(self):
        return "<部门: %s>" % self.dep_name
    #def __repr__(self):
    #    return "<Department(dep_name='%s')>" % self.dep_name
class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20),nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    phone  = Column(String(11))
    email  = Column(String(50))
    dep_ip = Column(Integer,ForeignKey('departments.dep_id'))
    def __str__(self):
        return '<员工: %s>' % self.emp_name
class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer,primary_key=True)
    basic = Column(Integer)
    salary_date = Column(Date)
    awards  = Column(Integer)
    emp_ip = Column(Integer,ForeignKey('employees.emp_id'))
    def __str__(self):
        return '<收入: %s>' % self.basic + self.awards

if __name__ == '__main__':
    # (metadata)
    # 如果库中不存在表则创建,以存在不会重复创建创建架构(续1)
    # •  通过表的映射类,在数据库中创建表
    Base.metadata.create_all(engine)
