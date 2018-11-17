#!/usr/bin/env python3

class Date:
    def __init__(self,year,month,day):
         self.year = year
         self.month = month
         self.day = day
    @classmethod
    def create_date(cls,str_date):
        y,m,d = map(int, str_date.split('-'))
        instance = cls(y,m,d)
        return 	instance
    @staticmethod
    def is_date_valid(str_date):
        y, m, d = map(int, str_date.split('-'))
        return y < 4000 and 0 < m < 13 and 0 <  d < 32
     
if __name__ == '__main__':
    d1 = Date(2018,5,30)
    d2 = Date.create_date('2018-05-30') 
    print(d2.year)
    print(d1.year)
    print(Date.is_date_valid('2018-03-05'))
    print(Date.is_date_valid('2018-15-05'))

