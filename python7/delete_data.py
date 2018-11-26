from dbcccc import Session,Departments

session = Session()


q1 = session.query(Departments).filter(Departments.dep_name=='开发部')
dep = q1.one()
session.delete(dep)
session.commit()
session.close()