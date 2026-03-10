#To calculate a LCM of a given number
a=2
b=3
lcm=max(a,b)
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    lcm+=1