import datetime
date =datetime.date.today()
currentYear =int(date.strftime("%Y"))
print("enter the last year")
endyear=int(input())
print("list of leap years:")
for year in range(currentYear,endyear):
 if ((year%4==0) and (year%100!=0) or (year%400==0)):
  print(year)       
