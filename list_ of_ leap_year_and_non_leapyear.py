from datetime import date, datetime
import datetime
year1 = int(input("Enter Starting year : "))
month1 = int(input("Enter Starting month : "))
date1 = int(input("Enter Starting date : "))
d = date(year1,month1,date1)
year2 = int(input("Enter Ending year : "))
month2 = int(input("Enter Ending month : "))
date2 = int(input("Enter Ending date : "))
b= date(year2,month2,date2)
l1=[]
l2=[]
print("Range: ")
print(d,"To",b)
for year in range(year1,year2):
  if(year%400==0)and(year%100==0):
    l1=l1+[year,]
  elif(year%4==0)and(year%100!=0):
    l1=l1+[year,]
  else:
    l2=l2+[year,]
print("list of leap year: ")
print(l1)
print("list of non leap: ",)
print(l2)
  
