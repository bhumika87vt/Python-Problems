#Adding two numbers without using arithematic operator 

a=5
b=3
while b!=0:
    carry=a&b
    a=a^b
    b=carry<<1
print(a)