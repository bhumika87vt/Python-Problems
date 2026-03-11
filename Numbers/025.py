#To calculate the GCD or HCF of a number
num1=16
num2=24  
if num1 > num2:    
    minimum = num2 
else:
    minimum = num1
for i in range(1, minimum+1):  
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i 
print("hcf/gcd of",num1,"and",num2,"=",hcf)