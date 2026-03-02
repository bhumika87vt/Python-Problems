#Fibonacci Series

#Recursive method
def fibonacci(a,b):
    print(a)
    print(b)
    for i in range(5):
        a,b=b,a+b
        print(b)
fibonacci(0,1)