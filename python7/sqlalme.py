#!/usr/bin/env python3

# SQLAlchemy概述

# iSQLAlchemy安装
# •  SQLAlchemy由官方收录,可以直接安装
# pip3 install sqlalchemy

# SQLAlchemy简介

# •  SQLAlchemy是Python编程语下的一款开源软件。
# 提供 SQL 具包及对象关系映 射(ORM) 工具,使用
# MIT许可证发

# •  SQLAlchemy“采用简单的Python语言,为高效和
# 高性能的数据库访问设计,实现了完整的企业级持久
# 模型”

# •  SQLAlchemy的理念是,SQL数据库的量级和性能重
# 要于对象集合;而对象集合的抽象又重要于表和行

# •  目标是提供能兼容众多数据库(如 SQLite、MySQL、
# Postgresql、Oracle、MS-SQL、SQLServer 和
# Firebird)的企业级持久性模型

# ORM模型
# •  ORM即对象关系映射
# •  数据库表是一个二维表,包含多行多列。把一个表的
# 内容用Python的数据结构表示出来的话,可以用一
# 个list表示多行,list的每一个元素是tuple,表示一行
# 记录
# [   
#                 ('1',   'Michael'), 
#                 ('2',   'Bob'), 
#                 ('3',   'Adam') 
# ]   ORM模型(续1)
# •  用tuple表示一行很难看出表的结构。如果把一个
# tuple用class实例来表示,就可以更容易地看出表的
# 结构来
# classUser(object):  
#     def__init__(self,   id, name):  
#         self.id=    id(
#         self.name=  names
#     
# [   
#     User('1',   'Michael'), 
#     User('2',   'Bob'), 
#     User('3',   'Adam') 
# ]   

