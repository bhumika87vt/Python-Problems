#Swapping a number without using third variable
a=10
b=20
print("Before Swapping")
print(a,b)
a=a+b
b=a-b
a=a-b
print("After Swapping")
print(a,b)

#or

a,b=5,10                                              
print("Before swapping:",a,b)
a,b=b,a
print("After swapping:",a,b)