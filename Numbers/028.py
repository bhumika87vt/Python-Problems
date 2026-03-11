#Given year is leap year or not
year=2019
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")