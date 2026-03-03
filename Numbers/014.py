#Finding a prime factor of a given integer

fac=12
for i in range(2,13):
    if fac%i==0:
        print(i)
        fac=fac//i