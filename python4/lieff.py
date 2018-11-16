#!/usr/bin/env python3

class Date:
    def __init__(self,year,month,date):
       self.year = year
       self.month = month 
       self.date = date

    @classmethod
    def create_date(cls,string_date):
       year,month,date = map(int,string_date.split('-'))
       instance = cls(year,month,date)
       return instance 
if __name__ == '__main__':
   d2 = Date.create_date('2018-05-04')
   print(d2.year)
   print(d2.month)
   print(d2.date)

 

